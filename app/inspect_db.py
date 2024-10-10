import sqlite3

db_path = r'D:\Projects\News-Article-ETL-with-NLP\app\news_articles.db'  # Adjust path if necessary

def inspect_db(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Get the schema for the articles table
    cursor.execute("PRAGMA table_info(articles)")
    columns = cursor.fetchall()

    for column in columns:
        print(column)

    conn.close()

if __name__ == "__main__":
    inspect_db(db_path)
