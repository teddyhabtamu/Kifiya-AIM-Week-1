import matplotlib.pyplot as plt
import seaborn as sns

def plot_top_publishers(publisher_counts, top_n=10):
    top_publishers = publisher_counts.head(top_n)
    top_publishers.plot(kind='bar', color='green', alpha=0.8)
    plt.title('Top Publishers by Article Count')
    plt.xlabel('Publisher')
    plt.ylabel('Number of Articles')
    plt.show()

def plot_distribution(data, column, bins=50, color='blue', title='', xlabel='', ylabel=''):
    plt.hist(data[column], bins=bins, color=color, alpha=0.7)
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
