# 💬 Chat with SQL Database using LangChain, Groq, and Streamlit

A conversational AI interface that connects to your **SQL database (MySQL or SQLite)** and lets you **ask natural language questions** powered by **LLMs (Groq Llama3)**. Uses LangChain's SQL agent and SQL toolkit to generate, execute, and respond with results — all inside a **Streamlit app**.

---

## 🚀 Features

- 🔗 Choose between **SQLite** or **MySQL** connection
- 🧠 Uses **Groq’s Llama3 model** for intelligent SQL generation
- ⚙️ Built on **LangChain SQLDatabaseToolkit + SQL Agent**
- 🛡️ Secure input of API keys and DB credentials
- 🧾 See live query generation and reasoning via LangChain callbacks
- 💬 Chat-style interface with persistent message history

---

## 📦 Installation

```bash
git clone https://github.com/your-username/chat-with-sql-db.git
cd chat-with-sql-db
pip install -r requirements.txt
```

## 🧠 Setup
- ✅ 1. Groq API Key : Get your key from https://console.groq.com/keys

- ✅ 2. MySQL DB (optional)
   If you're using MySQL:

- Ensure MySQL is running locally

- Create a user with appropriate privileges

- Example database: student
  ✅ Alternatively, just use the default students.db SQLite file.

## ▶️ Run the App
```
streamlit run app.py
```

## 📁 Project Structure
```
chat-with-sql-db/
│
├── students.db               # Sample SQLite database
├── app.py                    # Streamlit application
├── requirements.txt          # Python dependencies
└── README.md                 # Project readme

