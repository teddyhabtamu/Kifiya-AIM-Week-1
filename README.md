# Kifiya AIM WEEK-1
# Sentiment and Publisher Analysis of Financial News Headlines

## Project Overview

This project analyzes financial news headlines to uncover sentiment trends and publisher contributions. Using tools like the VADER sentiment analyzer and custom Python scripts, it provides insights into:

- Sentiment distribution of news headlines (positive, neutral, negative).
- Publisher activity and their contribution to sentiment trends.
- Common keywords and topics extracted from headlines.

The project is designed for financial analysts, traders, and researchers aiming to make data-driven decisions in stock market analysis.

## Table of Contents

- [Project Overview](#project-overview)
- [Table of Contents](#table-of-contents)
- [Installation](#installation)
- [Usage](#usage)
- [Functions](#functions)
  - [analyze_sentiment](#analyze_sentiment)
  - [plot_distribution](#plot_distribution)
- [Publisher Analysis](#publisher-analysis)
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

## Publisher Analysis

1. **Most Active Publishers**:
   - Identifies publishers with the most contributions to the dataset.
   - Provides insights into the type of content published.

2. **Domain Analysis**:
   - Extracts domains from email-based publisher names.
   - Highlights domain-level activity and average sentiment scores.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Feel free to contribute to this project by submitting issues or pull requests!
