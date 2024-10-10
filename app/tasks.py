import sqlite3

db_path = r'D:\Projects\News-Article-ETL-with-NLP\app\news_articles.db'  # Update this path

try:
    conn = sqlite3.connect(db_path)
    print("Database connection successful.")
except sqlite3.OperationalError as e:
    print(f"Error connecting to database: {e}")
finally:
    if 'conn' in locals():
        conn.close()
