# app/nlp_processing.py

import sqlite3
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK resources if not already downloaded
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def preprocess_text(text):
    # Tokenization
    tokens = word_tokenize(text)

    # Lowercasing
    tokens = [token.lower() for token in tokens]

    # Removing stop words and punctuation
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token.isalpha() and token not in stop_words]

    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]

    return tokens

def analyze_articles(db_path):
    # Connect to the database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Fetch articles from the database
    cursor.execute("SELECT id, content FROM articles")  # Adjust column names as needed
    articles = cursor.fetchall()

    # Check if any articles are retrieved
    if not articles:
        print("No articles found in the database.")
    else:
        for article_id, content in articles:
            # Preprocess the article content
            tokens = preprocess_text(content)

            # Print tokens for debugging
            print(f"Article ID: {article_id}, Tokens: {tokens}")

    # Close the database connection
    conn.close()
