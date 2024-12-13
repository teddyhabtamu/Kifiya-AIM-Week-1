# Scripts Folder

This folder contains modular Python scripts designed to support the functionality of the project. Each script focuses on a specific aspect of data processing, analysis, or visualization to keep the codebase organized and maintainable.

## Contents

### `data_processing.py`
- Functions for data loading, cleaning, and preprocessing.
- Example Functions:
  - `load_data(filepath)`: Loads a dataset from a given filepath.
  - `preprocess_data(data)`: Cleans and preprocesses the dataset for analysis.
  - `analyze_sentiment(data)`: Performs sentiment analysis on the dataset headlines.

### `visualization.py`
- Functions for generating visualizations to understand and present data insights.
- Example Functions:
  - `plot_top_publishers(publisher_data)`: Creates a bar chart of the most active publishers.
  - `plot_distribution(data, bins, title, xlabel, ylabel)`: Plots a histogram for data distributions.
  - `plot_time_series(data, title, xlabel, ylabel)`: Plots time-series data for trend analysis.

### `text_analysis.py`
- Functions for textual analysis and keyword/topic extraction.
- Example Functions:
  - `analyze_word_frequency(data)`: Identifies the most frequent words in headlines.
  - `extract_domain(publisher_column)`: Extracts domain information from email addresses in publisher data.

## How to Use

1. Import the required functions from the respective scripts into your main notebook or script.
    ```python
    from data_processing import load_data, analyze_sentiment
    from visualization import plot_distribution
    ```

2. Ensure the `scripts` folder is included in the Python path if accessing from another directory:
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
