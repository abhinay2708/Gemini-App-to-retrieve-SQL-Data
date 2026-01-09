import streamlit as st
import pandas as pd
import sqlite3
import google.generativeai as genai
import io

# --- 1. API CONFIGURATION ---
# Replace with your key or use st.sidebar for user input
API_KEY = "AI........................xI" 
genai.configure(api_key=API_KEY)

class DataAgent:
    def __init__(self):
        self.model = genai.GenerativeModel('gemini-2.5-flash')
        self.conn = sqlite3.connect(":memory:", check_same_thread=False)

    def load_data(self, file):
        """Loads CSV or Excel into an in-memory SQL database."""
        try:
            if file.name.endswith('.csv'):
                df = pd.read_csv(file)
            else:
                df = pd.read_excel(file)
            
            # Clean column names for SQL (remove spaces and special chars)
            df.columns = [c.replace(' ', '_').replace('.', '') for c in df.columns]
            df.to_sql("dataset", self.conn, index=False, if_exists="replace")
            return df, None
        except Exception as e:
            return None, str(e)

    def get_schema(self):
        cursor = self.conn.cursor()
        cursor.execute("PRAGMA table_info(dataset);")
        columns = [f"{col[1]} ({col[2]})" for col in cursor.fetchall()]
        return ", ".join(columns)

    def get_sql_and_query(self, user_query):
        schema = self.get_schema()
        prompt = f"""
        You are an expert SQL dev. The table is named 'dataset'.
        Columns: {schema}
        Task: Convert the question to a valid SQLite query.
        Output ONLY the raw SQL. No backticks.
        Question: {user_query}
        """
        response = self.model.generate_content(prompt)
        sql = response.text.strip().replace('```sql', '').replace('```', '')
        
        try:
            res_df = pd.read_sql_query(sql, self.conn)
            return sql, res_df, None
        except Exception as e:
            return sql, None, str(e)

# --- 2. STREAMLIT UI ---
st.set_page_config(page_title="SQL Data Retriever", layout="wide")
st.title("SQL Data Retriever")
st.write("Upload a file and ask questions from the dataset")

agent = DataAgent()

# File Uploader
uploaded_file = st.file_uploader("Upload CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file:
    df, error = agent.load_data(uploaded_file)
    
    if df is not None:
        st.subheader("Preview of Dataset")
        st.dataframe(df.head(5), use_container_width=True)
        
        st.divider()
        
        # User Question
        user_question = st.text_input("Ask a question about this data:", placeholder="e.g., What is the average salary?")
        
        if st.button("Analyze"):
            if user_question:
                with st.spinner("Analyzing..."):
                    sql_query, result_df, query_error = agent.get_sql_and_query(user_question)
                    
                    # Box 1: Show SQL Query
                    st.subheader("💻 Generated SQL Query")
                    st.code(sql_query, language="sql")
                    
                    # Box 2: Show Results
                    st.subheader("✅ Answer")
                    if query_error:
                        st.error(f"Error running query: {query_error}")
                    else:
                        if result_df.empty:
                            st.warning("Query returned no results.")
                        else:
                            st.dataframe(result_df, use_container_width=True)
            else:
                st.warning("Please enter a question.")
    else:
        st.error(f"Error loading file: {error}")