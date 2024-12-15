import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from tqdm import tqdm

def load_data(filepath):
    return pd.read_csv(filepath)

def preprocess_data(data):
    data['headline_length'] = data['headline'].apply(len)
    data['date'] = pd.to_datetime(data['date'], errors='coerce')
    data['day_of_week'] = data['date'].dt.day_name()
    data['hour'] = data['date'].dt.hour
    return data

def analyze_sentiment(data, chunk_size=1000):
    sid = SentimentIntensityAnalyzer()
    
    def get_sentiment(text):
        return sid.polarity_scores(text)['compound']
    
    chunks = []
    for start in tqdm(range(0, len(data), chunk_size)):
        chunk = data.iloc[start:start + chunk_size].copy()
        chunk['sentiment'] = chunk['headline'].apply(get_sentiment)
        chunks.append(chunk)
    
    combined_data = pd.concat(chunks)
    print(combined_data.columns)  # Debug: Verify sentiment column exists in the result
    return combined_data
