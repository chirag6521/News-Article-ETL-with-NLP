import feedparser
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Article
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer

# Ensure you download the necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Database setup
DATABASE_URL = "postgresql://user:password@localhost:5432/news_db"  # Update with your actual DB credentials
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def clean_text(text):
    # Tokenize the text
    tokens = word_tokenize(text.lower())
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    cleaned_tokens = [token for token in tokens if token.isalnum() and token not in stop_words]
    return cleaned_tokens

def lemmatize_text(tokens):
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return lemmatized_tokens

def vectorize_text(lemmatized_tokens):
    # Join tokens back into a single string
    lemmatized_text = ' '.join(lemmatized_tokens)
    
    # Create a CountVectorizer
    vectorizer = CountVectorizer()
    
    # Fit and transform the lemmatized text
    vectorized_text = vectorizer.fit_transform([lemmatized_text])
    
    # Convert the vector to an array
    return vectorized_text.toarray(), vectorizer.get_feature_names_out()

def fetch_and_store_articles():
    # List of RSS feeds
    feeds = [
        "http://rss.cnn.com/rss/cnn_topstories.rss",
        "http://qz.com/feed",
        "http://feeds.foxnews.com/foxnews/politics",
        "http://feeds.reuters.com/reuters/businessNews",
        "http://feeds.feedburner.com/NewshourWorld",
        "https://feeds.bbci.co.uk/news/world/asia/india/rss.xml"
    ]

    for feed in feeds:
        # Parse the feed
        parsed_feed = feedparser.parse(feed)
        
        for entry in parsed_feed.entries:
            title = entry.title
            content = entry.summary  # Use entry.content or entry.description if needed
            publication_date = entry.published
            source_url = entry.link
            
            # Clean, lemmatize, and vectorize the article content
            cleaned_tokens = clean_text(content)
            lemmatized_tokens = lemmatize_text(cleaned_tokens)
            vectorized_array, feature_names = vectorize_text(lemmatized_tokens)

            # Create an Article object (assuming you have an Article model)
            article = Article(
                title=title,
                content=content,
                publication_date=publication_date,
                source_url=source_url,
                vectorized_content=vectorized_array.tobytes()  # Store as bytes or handle appropriately
            )
            
            # Store the article in the database
            session.add(article)
        
    session.commit()

if __name__ == "__main__":
    fetch_and_store_articles()
