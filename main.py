import tkinter as tk
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from sorting import bubble_sort, selection_sort, insertion_sort

# Define a dictionary of sorting algorithms
sorting_algorithms = {
    "Bubble Sort": bubble_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort
}

# Define a function to update the plot with the sorted data
def update_fig(data_tuple, bars, annotation):
    sorted_data, i, j = data_tuple
    for k, bar in enumerate(bars):
        if k == i or k == j:
            bar.set_color('red')
        else:
            bar.set_color('blue')
        bar.set_height(sorted_data[k])
    annotation.set_text(f"Swapping {sorted_data[j]} and {sorted_data[i]}")

# Define a function to start the animation for the selected algorithm
def start_animation(algorithm_name):
    sorting_algorithm = sorting_algorithms[algorithm_name]
    data = np.random.rand(10)
    fig, ax = plt.subplots()
    bars = ax.bar(range(len(data)), data)
    annotation = ax.annotate("", xy=(0.05, 0.95), xycoords="axes fraction")
    anim = animation.FuncAnimation(fig, update_fig, frames=sorting_algorithm(data), fargs=(bars, annotation), save_count=len(data), repeat=False)
    ax.set_title(algorithm_name)
    plt.show()

# Create the GUI
root = tk.Tk()
root.title("Sorting Algorithm Visualizer")

# Create a label to display instructions
label = tk.Label(root, text="Choose a sorting algorithm:")
label.pack()

# Create a button for each sorting algorithm
for algorithm_name in sorting_algorithms.keys():
    button = tk.Button(root, text=algorithm_name, command=lambda name=algorithm_name: start_animation(name))
    button.pack()

# Run the GUI
root.mainloop()
