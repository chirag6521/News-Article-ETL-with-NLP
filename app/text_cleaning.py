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

if __name__ == "__main__":
    # Sample text for demonstration
    sample_text = "Millions in the U.S. could face massive consequences unless McCarthy can navigate the debt trap set by Biden."
    
    # Clean the text
    cleaned_tokens = clean_text(sample_text)
    print("Cleaned text:", cleaned_tokens)
    
    # Lemmatize the cleaned tokens
    lemmatized_tokens = lemmatize_text(cleaned_tokens)
    print("Lemmatized text:", lemmatized_tokens)
    
    # Vectorize the lemmatized tokens
    vectorized_array, feature_names = vectorize_text(lemmatized_tokens)
    
    # Print the vectorized array and feature names
    print("Vectorized text:\n", vectorized_array)
    print("Feature names:\n", feature_names)
