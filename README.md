# 💬 QueryMate: Natural Language Interface for SQL & NoSQL Databases

QueryMate is a Flask-based web application that allows users to interact with **MySQL** and **MongoDB** databases using **natural language** queries. It uses Google's **Gemini API** to convert user input into valid SQL or MongoDB commands, then executes them and displays results in a modern chat-like UI.

---

## 📌 Features

- 🔍 Schema Exploration: Ask "What tables exist?" or "Show me fields in employees"
- 📄 Sample Data Fetching
- 🧠 Natural Language to:
  - ✅ SQL Queries (SELECT, JOIN, INSERT, UPDATE, DELETE)
  - ✅ MongoDB Queries (find, aggregate, insertOne, updateOne, deleteOne)
- 📊 Table-based response display
- 💾 Session-based chat history
- ✅ Support for both RDBMS (MySQL) and NoSQL (MongoDB)

---

## ⚙️ Prerequisites

Make sure the following are installed on your system:

- Python ≥ 3.9
- pip
- Flask
- MySQL Server running locally
- MongoDB Server (local)
- A valid **Gemini API Key** from Google (https://makersuite.google.com/app/apikey)

---

## 🗝️ Environment Variables (API Key Setup)

Create a `.env` file in the project root directory with the following content:

```env
GEMINI_API_KEY=your_gemini_api_key_here
MYSQL_HOST=localhost
MYSQL_USER=your_mysql_username
MYSQL_PASSWORD=your_mysql_password
MYSQL_DB=your_mysql_database_name
MONGO_URI=mongodb://localhost:27017/
MONGO_DB=your_mongodb_database_name
```



---

## 📦 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/paarthsoni/Dsci551_repository.git
cd Dsci551_repository
```

### 2. Create & activate virtual environment

```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Running the App

```bash
flask run
```

Then open [http://localhost:5000](http://localhost:5000) in your browser.

---

## 🧾 `requirements.txt`

```txt
Flask
pymongo
python-dotenv
google-generativeai
PyMySQL
```

Generate this anytime using:
```bash
pip freeze > requirements.txt
```

---

