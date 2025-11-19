🧠 Natural Language to SQL Query App (Gemini + Streamlit)

This project allows users to type questions in plain English, and the app automatically converts them into SQL queries using Google Gemini (2.5 Flash).
The SQL query is then executed on a local SQLite database, and results are displayed instantly.

Perfect for beginners, data analysts, and anyone exploring AI + SQL automation.

🚀 Features

✔ Convert natural-language questions into SQL
✔ Automatically generate SQL using Gemini 2.5 Flash
✔ Execute SQL queries on a SQLite database
✔ Display results cleanly in a Streamlit web interface
✔ Easy and intuitive UI

📂 Project Structure
project/
│
├── employee.db               # SQLite database file
├── app.py                    # Main Streamlit application
└── README.md                 # Documentation

🔧 Tech Stack
Component	Technology
Frontend	Streamlit
Backend	Python
Database	SQLite
LLM Model	Google Gemini 2.5 Flash
🛠 Requirements

Before running the project, install the required dependencies:

pip install streamlit google-generativeai sqlite3


(Note: sqlite3 is included by default in Python.)

🔑 Setup API Key

Replace this line in your code:

genai.configure(api_key="AIz.........................txI")


with your actual Google Gemini API key.

You can get an API key at:
👉 https://ai.google.dev/

▶️ How to Run the App
1. Make sure your database exists

Your SQLite database file must be named:

employee.db


And must contain a table:

employee(employee_name, employee_role, employee_salary)

2. Run the Streamlit app
streamlit run app.py


This will open the app in your browser at:

http://localhost:8501

💬 How It Works
1. User enters a natural-language question

Example:

"Show all employees in Data Science role"

2. Gemini converts the question into SQL

Example SQL produced:

SELECT * FROM employee WHERE employee_role = "Data Science";

3. SQL is executed on SQLite

Python runs the query and retrieves rows.

4. Streamlit displays the output

User sees all matching employee records.

🧩 Code Overview
🔹 Generate SQL from natural language
response = model.generate_content([prompt[0], question])
return response.text

🔹 Execute SQL on SQLite database
cur.execute(sql)
rows = cur.fetchall()

🔹 Show results in Streamlit
st.header(row)

📌 Notes & Limitations

Gemini must generate correct SQL (prompting matters).

Ensure your table and column names match the prompt.

SQL injection is not an issue here because the SQL is AI-generated.

⭐ Future Improvements

Add better error handling for invalid SQL

Add support for multiple tables

Show full query output in a formatted table

Add history of queries

Add charts based on SQL results
