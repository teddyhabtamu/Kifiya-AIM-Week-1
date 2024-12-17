# Kifiya AIM WEEK-1
# Sentiment and Publisher Analysis of Financial News Headlines

## Project Overview

This project analyzes financial news headlines to uncover sentiment trends and publisher contributions. Using tools like the VADER sentiment analyzer, TA-Lib, PyNance, and custom Python scripts, it provides insights into:

- Sentiment distribution of news headlines (positive, neutral, negative).
- Publisher activity and their contribution to sentiment trends.
- Common keywords and topics extracted from headlines.
- Correlation between news sentiment and stock movements.

The project is designed for financial analysts, traders, and researchers aiming to make data-driven decisions in stock market analysis.

## Table of Contents

- [Project Overview](#project-overview)
- [Table of Contents](#table-of-contents)
- [Installation](#installation)
- [Usage](#usage)
- [Functions](#functions)
  - [analyze_sentiment](#analyze_sentiment)
  - [plot_distribution](#plot_distribution)
  - [get_common_keywords](#get_common_keywords)
  - [get_topics](#get_topics)
- [Publisher Analysis](#publisher-analysis)
- [Stock Analysis](#stock-analysis)
- [Correlation Analysis](#correlation-analysis)
- [License](#license)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Install the VADER lexicon for sentiment analysis:
    ```python
    import nltk
    nltk.download('vader_lexicon')
    ```

## Usage

### Task 1: Sentiment and Publisher Analysis

1. Load your dataset:
    ```python
    import pandas as pd
    data = pd.read_csv('your_file.csv')
    ```

2. Perform sentiment analysis:
    ```python
    from data_processing import analyze_sentiment
    sentiment_data = analyze_sentiment(data)
    ```

3. Plot the distribution of sentiment scores:
    ```python
    from visualization import plot_distribution
    plot_distribution(sentiment_data['sentiment'], bins=50, color='blue', title='Sentiment Distribution', xlabel='Sentiment Score', ylabel='Frequency')
    ```

4. Perform publisher analysis:
    ```python
    # Extract domain from email addresses
    sentiment_data['domain'] = sentiment_data['publisher'].apply(lambda x: x.split('@')[-1] if '@' in x else x)

    # Count articles by domain
    domain_counts = sentiment_data['domain'].value_counts()
    print("Number of Articles per Domain:")
    print(domain_counts)

    # Group by domain and calculate mean sentiment
    domain_sentiment = sentiment_data.groupby('domain')['sentiment'].mean().sort_values(ascending=False)
    print("Mean Sentiment per Domain:")
    print(domain_sentiment)
    ```

### Task 2: Quantitative Analysis Using PyNance and TA-Lib

1. Load stock price data:
    ```python
    import pandas as pd
    data = pd.read_csv('your_stock_data.csv')
    ```

2. Calculate technical indicators using TA-Lib:
    ```python
    import talib

    data['SMA'] = talib.SMA(data['Close'], timeperiod=30)
    data['EMA'] = talib.EMA(data['Close'], timeperiod=30)
    data['RSI'] = talib.RSI(data['Close'], timeperiod=14)
    data['MACD'], data['MACD_Signal'], data['MACD_Hist'] = talib.MACD(data['Close'], fastperiod=12, slowperiod=26, signalperiod=9)

    data = data.dropna()
    ```

3. Visualize the data:
    ```python
    import matplotlib.pyplot as plt

    # Plot Closing Price and Moving Averages
    plt.figure(figsize=(14, 7))
    plt.plot(data['Close'], label='Close Price')
    plt.plot(data['SMA'], label='SMA (30)')
    plt.plot(data['EMA'], label='EMA (30)')
    plt.title('Stock Price and Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

    # Plot RSI
    plt.figure(figsize=(14, 7))
    plt.plot(data['RSI'], label='RSI (14)')
    plt.title('Relative Strength Index (RSI)')
    plt.xlabel('Date')
    plt.ylabel('RSI')
    plt.legend()
    plt.show()

    # Plot MACD
    plt.figure(figsize=(14, 7))
    plt.plot(data['MACD'], label='MACD')
    plt.plot(data['MACD_Signal'], label='MACD Signal')
    plt.bar(data.index, data['MACD_Hist'], label='MACD Hist', color='gray')
    plt.title('MACD')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    plt.show()
    ```

### Task 3: Correlation Between News and Stock Movement

1. Normalize dates and merge datasets:
    ```python
    import pandas as pd
    from textblob import TextBlob

    # Load news data
    news_data = pd.read_csv('news_data.csv')

    # Load stock data
    stock_data = pd.read_csv('stock_data.csv')

    # Convert date columns to datetime
    news_data['date'] = pd.to_datetime(news_data['date'])
    stock_data['date'] = pd.to_datetime(stock_data['date'])

    # Calculate daily returns in stock_data
    stock_data['daily_return'] = stock_data['close'].pct_change()

    # Drop rows with NaN values in stock_data
    stock_data = stock_data.dropna()

    # Merge datasets on date
    merged_data = pd.merge(news_data, stock_data, on='date')

    # Function to get sentiment
    def get_sentiment(text):
        analysis = TextBlob(text)
        return analysis.sentiment.polarity

    # Apply sentiment analysis
    merged_data['sentiment'] = merged_data['headline'].apply(get_sentiment)

    # Aggregate sentiment scores by date
    daily_sentiment = merged_data.groupby('date')['sentiment'].mean().reset_index()

    # Merge daily sentiment with stock data
    correlation_data = pd.merge(daily_sentiment, stock_data[['date', 'daily_return']], on='date')

    # Calculate Pearson correlation coefficient
    correlation = correlation_data['sentiment'].corr(correlation_data['daily_return'])
    print(f'Pearson correlation coefficient: {correlation}')
    ```

2. Visualize the correlation:
    ```python
    import matplotlib.pyplot as plt

    # Plot Sentiment Scores Over Time
    plt.figure(figsize=(14, 7))
    plt.plot(daily_sentiment['date'], daily_sentiment['sentiment'], label='Daily Sentiment')
    plt.title('Daily Sentiment Scores Over Time')
    plt.xlabel('Date')
    plt.ylabel('Sentiment Score')
    plt.legend()
    plt.show()

    # Plot Daily Returns Over Time
    plt.figure(figsize=(14, 7))
    plt.plot(stock_data['date'], stock_data['daily_return'], label='Daily Returns')
    plt.title('Daily Stock Returns Over Time')
    plt.xlabel('Date')
    plt.ylabel('Daily Return')
    plt.legend()
    plt.show()

    # Scatter Plot of Sentiment vs. Daily Returns
    plt.figure(figsize=(14, 7))
    plt.scatter(correlation_data['sentiment'], correlation_data['daily_return'], alpha=0.5)
    plt.title('Sentiment vs. Daily Returns')
    plt.xlabel('Sentiment Score')
    plt.ylabel('Daily Return')
    plt.show()
    ```

## Functions

### `analyze_sentiment`
Processes the dataset to add a `sentiment` column based on VADER sentiment analysis.
- **Input**: DataFrame with a `headline` column.
- **Output**: DataFrame with an added `sentiment` column.

### `plot_distribution`
Generates a histogram to visualize the distribution of sentiment scores.
- **Parameters**:
  - `data`: Data to plot.
  - `bins`: Number of bins in the histogram.
  - `color`, `title`, `xlabel`, `ylabel`: Customization options.

### `get_common_keywords`
Extracts the most common keywords from the specified column in the dataset.
- **Input**: DataFrame with a text column.
- **Output**: DataFrame with common keywords and their counts.

### `get_topics`
Performs topic modeling on the specified column in the dataset.
- **Input**: DataFrame with a text column.
- **Output**: Dictionary with topics and their associated keywords.

## Publisher Analysis

1. **Most Active Publishers**:
   - Identifies publishers with the most contributions to the dataset.
   - Provides insights into the type of content published.

2. **Domain Analysis**:
   - Extracts domains from email-based publisher names.
   - Highlights domain-level activity and average sentiment scores.

## Stock Analysis

1. **Technical Indicators**:
   - Calculates various technical indicators such as SMA, EMA, RSI, and MACD using TA-Lib.
   - Provides insights into stock price trends and movements.

## Correlation Analysis

1. **Sentiment and Stock Returns**:
   - Calculates the Pearson correlation coefficient between daily news sentiment scores and stock daily returns.
   - Provides insights into the relationship between news sentiment and stock movements.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Feel free to contribute to this project by submitting issues or pull requests!