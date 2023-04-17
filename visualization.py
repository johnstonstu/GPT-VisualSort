import random
import time
import matplotlib.pyplot as plt
from sorting_algorithms import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort

def plot_sorting_algorithm(arr, func, title):
    plt.figure()
    plt.title(title)
    plt.bar(range(len(arr)), arr)
    start_time = time.time()
    func(arr, 0, len(arr)-1)
    end_time = time.time()
    plt.bar(range(len(arr)), arr)
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.text(0.5, 0.95, f"Time taken: {end_time - start_time:.6f} seconds", horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)
    plt.show()

arr = [random.randint(1, 100) for _ in range(20)]
plot_sorting_algorithm(arr.copy(), bubble_sort, 'Bubble Sort')
plot_sorting_algorithm(arr.copy(), selection_sort, 'Selection Sort')
plot_sorting_algorithm(arr.copy(), insertion_sort, 'Insertion Sort')
plot_sorting_algorithm(arr.copy(), merge_sort, 'Merge Sort')
plot_sorting_algorithm(arr.copy(), quick_sort, 'Quick Sort')
