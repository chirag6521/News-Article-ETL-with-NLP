import sqlite3

db_path = r'D:\Projects\News-Article-ETL-with-NLP\app\news_articles.db'

def check_articles(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Update to select the correct columns
    cursor.execute("SELECT id, title, link, description FROM articles")
    articles = cursor.fetchall()

    if articles:
        for article in articles:
            print(f"ID: {article[0]}, Title: {article[1]}, Link: {article[2]}, Description: {article[3]}")
    else:
        print("No articles found.")

    conn.close()

if __name__ == "__main__":
    check_articles(db_path)
