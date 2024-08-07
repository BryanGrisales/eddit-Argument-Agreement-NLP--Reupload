import pandas as pd
import matplotlib.pyplot as plt

def plot_results(data):
    label_counts = data['label'].value_counts()
    plt.bar(label_counts.index, label_counts.values)
    plt.xlabel('Category')
    plt.ylabel('Count')
    plt.title('Argument Categories')

    unique_labels = label_counts.index.tolist()
    plt.xticks(ticks=label_counts.index, labels=unique_labels)
    
    plt.show()

if __name__ == "__main__":
    data = pd.read_csv('data/processed/cleaned_data.csv')
    plot_results(data)
