import pandas as pd
def normalizeAndMerge_data(data1, data2):
  data1['date'] = pd.to_datetime(data1['date'], format='ISO8601', errors='coerce')
  
  data2['date'] = pd.to_datetime(data2['Date'], format='ISO8601', errors='coerce')
  
  data1['date'] = data1['date'].dt.tz_localize(None)
  data2['date'] = data2['date'].dt.tz_localize(None)
  
  merged_data = pd.merge(data1, data2, on='date')
  return merged_data

def calculate_correlation(daily_sentiment, stock_data):
  correlation_data = pd.merge(daily_sentiment, stock_data[['date', 'daily_return']], on='date')
  return correlation_data