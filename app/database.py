from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String

# Database connection string
DATABASE_URL = "sqlite:///news_articles.db"  # Update this based on your database

# Create an engine
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a Base class
Base = declarative_base()

# Define the Article model
class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    link = Column(String, nullable=False)
    description = Column(String, nullable=True)

# Create the tables in the database
Base.metadata.create_all(engine)
