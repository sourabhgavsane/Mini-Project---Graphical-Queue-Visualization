import tkinter as tk
from tkinter import messagebox

# Queue implementation
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

# GUI setup
root = tk.Tk()
root.title("Graphical Queue Visualization")

# Create a canvas to display the queue
canvas = tk.Canvas(root, width=400, height=200)
canvas.pack()

# Create input field for enqueue
entry = tk.Entry(root)
entry.pack()

# Create labels for queue elements
labels = []

# Queue object
queue = Queue()

# Enqueue function
def enqueue():
    item = entry.get()
    if item:
        queue.enqueue(item)
        update_queue_display()
        entry.delete(0, "end")
    else:
        messagebox.showwarning("Empty Input", "Please enter an item to enqueue.")

# Dequeue function
def dequeue():
    if not queue.is_empty():
        dequeued_item = queue.dequeue()
        update_queue_display()
        messagebox.showinfo("Dequeued", f"Dequeued item: {dequeued_item}")
    else:
        messagebox.showwarning("Empty Queue", "The queue is empty.")

# Update the queue display
def update_queue_display():
    canvas.delete("all")
    x, y = 50, 100
    for item in queue.items:
        canvas.create_rectangle(x, y - 20, x + 40, y, outline="black", fill="lightblue")
        canvas.create_text(x + 20, y - 10, text=item)
        x += 50

# Create GUI buttons
enqueue_button = tk.Button(root, text="Enqueue", command=enqueue)
dequeue_button = tk.Button(root, text="Dequeue", command=dequeue)

enqueue_button.pack()
dequeue_button.pack()

# Start the GUI main loop
root.mainloop()
