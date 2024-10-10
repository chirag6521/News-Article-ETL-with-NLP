from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class NewsArticle(Base):
    __tablename__ = 'news_articles'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String)
    publication_date = Column(DateTime)
    source_url = Column(String)

# Example of creating an engine and session
engine = create_engine('your_database_connection_string_here')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# models.py
from sqlalchemy import Column, Integer, String, DateTime, LargeBinary
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Article(Base):
    __tablename__ = 'articles'  # Table name in the database

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    publication_date = Column(DateTime, nullable=False)
    source_url = Column(String, nullable=False)
    vectorized_content = Column(LargeBinary)  # Store the vectorized content

    def __repr__(self):
        return f"<Article(title={self.title}, publication_date={self.publication_date})>"
