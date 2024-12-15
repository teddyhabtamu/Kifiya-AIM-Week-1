import matplotlib.pyplot as plt
import seaborn as sns

def barchart(data, top_n=10, title='', xlabel='', ylabel=''):
    top_publishers = data.head(top_n)
    top_publishers.plot(kind='bar', color='green', alpha=0.8)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def plot_distribution(column, bins=50, color='blue', title='', xlabel='', ylabel=''):
    plt.hist(column, bins=bins, color=color, alpha=0.7)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def plot_time_series(series, title, xlabel, ylabel, color='blue'):
    series.plot(color=color, alpha=0.7, figsize=(12, 6))
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
    
def plot_relation_of_varibles(dailySentimentDate, dailySentimentSentiment, label, title, xlabel, ylabel):
    plt.figure(figsize=(12, 6))
    plt.plot(dailySentimentDate, dailySentimentSentiment, label=label,)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.show()
    
def scatter_plot(sentiment, daily_return, alpha, title, xlabel, ylabel):
    plt.figure(figsize=(14, 7))
    plt.scatter(sentiment, daily_return, alpha= alpha)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
