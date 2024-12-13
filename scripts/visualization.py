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
