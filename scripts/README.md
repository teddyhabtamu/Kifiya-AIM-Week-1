# Scripts Folder

This folder contains modular Python scripts designed to support the functionality of the project. Each script focuses on a specific aspect of data processing, analysis, or visualization to keep the codebase organized and maintainable.

## Contents

### `data_processing.py`
- Functions for data loading, cleaning, and preprocessing.
- Example Functions:
  - `load_data(filepath)`: Loads a dataset from a given filepath.
  - `preprocess_data(data)`: Cleans and preprocesses the dataset for analysis.
  - `analyze_sentiment(data, chunk_size=1000)`: Performs sentiment analysis on the dataset headlines in chunks to handle large datasets efficiently.

### `visualization.py`
- Functions for generating visualizations to understand and present data insights.
- Example Functions:
  - `plot_top_publishers(publisher_data)`: Creates a bar chart of the most active publishers.
  - `plot_distribution(data, bins, title, xlabel, ylabel)`: Plots a histogram for data distributions.
  - `plot_time_series(data, title, xlabel, ylabel)`: Plots time-series data for trend analysis.
  - `plot_sentiment_vs_returns(sentiment_data, returns_data)`: Creates a scatter plot to visualize the relationship between sentiment scores and stock returns.

### `text_analysis.py`
- Functions for textual analysis and keyword/topic extraction.
- Example Functions:
  - `analyze_word_frequency(data)`: Identifies the most frequent words in headlines.
  - `extract_domain(publisher_column)`: Extracts domain information from email addresses in publisher data.
  - `get_common_keywords(data, column, top_n=10)`: Extracts the most common keywords from the specified column in the dataset.
  - `get_topics(data, column, n_topics=5)`: Performs topic modeling on the specified column in the dataset.

### `correlation.py`
- Functions for performing correlation analysis between news sentiment and stock movements.
- Example Functions:
  - `calculate_daily_returns(stock_data)`: Calculates daily percentage changes in stock prices.
  - `aggregate_sentiment_by_date(news_data)`: Aggregates sentiment scores by date.
  - `calculate_correlation(sentiment_data, returns_data)`: Calculates the Pearson correlation coefficient between sentiment scores and stock returns.

## How to Use

1. Import the required functions from the respective scripts into your main notebook or script.
    ```python
    from data_processing import load_data, analyze_sentiment
    from visualization import plot_distribution
    from text_analysis import get_common_keywords, get_topics
    from correlation import calculate_daily_returns, aggregate_sentiment_by_date, calculate_correlation
    ```

2. Ensure the [scripts](http://_vscodecontentref_/3) folder is included in the Python path if accessing from another directory:
    ```python
    import sys
    import os
    scripts_path = os.path.abspath("../scripts")
    if scripts_path not in sys.path:
        sys.path.append(scripts_path)
    ```

3. Use the modular functions in your workflow to keep the code organized and reusable.

---

For any issues or contributions, please refer to the main project documentation or submit a pull request.