from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

def analyze_word_frequency(data, column='headline', stop_words='english', top_n=20):
    vectorizer = CountVectorizer(stop_words=stop_words)
    X = vectorizer.fit_transform(data[column])
    word_counts = pd.DataFrame(X.sum(axis=0), columns=vectorizer.get_feature_names_out()).T
    word_counts.columns = ['count']
    return word_counts.sort_values(by='count', ascending=False).head(top_n)

def extract_domain(data, publisher_column='publisher'):
    data['domain'] = data[publisher_column].apply(lambda x: x.split('@')[-1] if '@' in x else x)
    return data
