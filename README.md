# 🌱 Ecovia Backend

Ecovia is a gamified eco-awareness platform that rewards users for completing daily eco-friendly challenges.  
Built with **FastAPI**, **MySQL**, and **SQLAlchemy**, the backend powers features like user registration, challenge tracking, eco-coin rewards, biomes & animals purchase, and a leaderboard system.

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/ecovia-backend.git
cd ecovia-backend
```

### 2️⃣ Create and activate a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure the database connection  
Open `app/database.py` and update this line with **your own MySQL username, password, host, and database name**:
```python
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://<username>:<password>@<host>/<database>"
```
Example for local setup:
```python
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:mypassword@localhost/ecovia"
```
**Note:** If your MySQL password contains special characters like `@`, `#`, or `$`, you must URL-encode them (e.g., `@` becomes `%40`).

Make sure you have MySQL installed and running locally.

### 5️⃣ Create the database  
In MySQL:
```sql
CREATE DATABASE ecovia;
```

### 6️⃣ Import the database schema  
```bash
mysql -u root -p ecovia < ecovia.sql
```
This will create all required tables and seed initial data.

### 7️⃣ Run the server
```bash
uvicorn app.main:app --reload
```

The API will now be available at: **http://127.0.0.1:8000**

---

## 📂 Project Structure
```
ecovia/
│
├── app/
│   ├── crud/            # Database CRUD operations
│   ├── models/          # SQLAlchemy models
│   ├── routes/          # API endpoints
│   ├── schemas/         # Pydantic schemas
│   ├── utils/           # Helper functions
│   ├── database.py      # Database connection setup
│   └── main.py          # FastAPI application entry
│
├── static/
│   └── uploads/         # Uploaded files (ignored by git)
│
├── ecovia.sql           # Database schema & seed data
├── .gitignore           # Ignored files and folders
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## 🛠 Tech Stack
- **Backend**: FastAPI
- **Database**: MySQL + SQLAlchemy ORM
- **Auth**: JWT Tokens
- **Image Processing**: gradio_client + Hugging Face Space
- **Deployment**: Uvicorn

---

## 📌 Notes
- All uploaded files go into `static/uploads/` and are ignored by Git.
- Always run the backend in a **virtual environment** to avoid dependency conflicts.
- The database credentials are stored directly in `app/database.py` for local development — change them as per your local MySQL setup.
