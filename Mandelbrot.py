import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import font

def update_values():
    global mandlCValue, mandlZ2modValue, mandlIterationValue
    
    # Default values
    default_c_value = 1.0
    default_z_value = 2
    default_iteration_value = 50

    try:
        mandlCValue = float(c_value_entry.get()) if c_value_entry.get() != "" else default_c_value
    except ValueError:
        mandlCValue = default_c_value

    try:
        mandlZ2modValue = float(z_value_entry.get()) if z_value_entry.get() != "" else default_z_value
    except ValueError:
        mandlZ2modValue = default_z_value

    try:
        mandlIterationValue = int(i_value_entry.get()) if i_value_entry.get() != "" else default_iteration_value
    except ValueError:
        mandlIterationValue = default_iteration_value
    
    # Close the input window
    root.destroy()
    
    plot_mandelbrot()

def plot_mandelbrot():
    # Define the dimensions of the plot
    width, height = 1600, 1600
    x = np.linspace(-2.5, 1.5, width)
    y = np.linspace(-2, 2, height)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y

    # Initialize the Mandelbrot set
    c = Z
    mandelbrot_set = np.zeros(Z.shape, dtype=int)

    # Iterate to determine membership in the Mandelbrot set
    max_iterations = mandlIterationValue
    for k in range(max_iterations):
        Z = Z**mandlZ2modValue + c**mandlCValue
        mask = (np.abs(Z) < 2)
        mandelbrot_set += mask

    # Plot the Mandelbrot set
    plt.imshow(mandelbrot_set, extent=(-2.5, 1.5, -2, 2), cmap='turbo_r')
    plt.colorbar()
    plt.title('Mandelbrot Set')
    plt.show()

root = tk.Tk()
custom_font = font.Font(family="Helvetica", size=16, weight="bold")
root.title('Define your mandelbrot')
window_width = 800
window_height = 1000
root.resizable(False, False)


# Try removing or adjusting the transparency attribute
root.attributes('-alpha', 0.5)

# Get the screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the center point
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

# Set the window geometry to center it on the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

mandlCValue = tk.StringVar()
mandlCValue.set("")
mandlZ2modValue = tk.StringVar()
mandlZ2modValue.set("")
mandlIterationValue = tk.StringVar()
mandlIterationValue.set("")
signin = tk.Frame(root)
#equation label
equation_label = tk.Label(root, font=custom_font, text ="zn+1=zn2+c")
equation_label.pack(fill='x', expand=True)
# z value
z_value_label = tk.Label(root, text="Z Value",)
z_value_label.pack(fill='x', expand=True)

z_value_entry = tk.Entry(root, textvariable=mandlZ2modValue)
z_value_entry.pack(fill='x', expand=True)
z_value_entry.focus()

# c value
c_value_label = tk.Label(root, text="C Value")
c_value_label.pack(fill='x', expand=True)

c_value_entry = tk.Entry(root, textvariable=mandlCValue)
c_value_entry.pack(fill='x', expand=True)

# iteration value
iteration_value_label = tk.Label(root, text="# of iterations")
iteration_value_label.pack(fill='x', expand=True)

i_value_entry = tk.Entry(root, textvariable=mandlIterationValue)
i_value_entry.pack(fill='x', expand=True)

# start
start_button = tk.Button(root, text="Start", command=update_values)
start_button.pack(fill='x', expand=True, pady=10)

root.mainloop()
