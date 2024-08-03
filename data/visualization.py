import matplotlib.pyplot as plt

def plot_results(results):
    plt.bar(results.keys(), results.values())
    plt.xlabel('Category')
    plt.ylabel('Count')
    plt.title('Results')
    plt.show()

if __name__ == "__main__":
    # Example usage
    results = {'Category A': 10, 'Category B': 20}
    plot_results(results)
