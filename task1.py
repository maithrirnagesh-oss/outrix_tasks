import tkinter as tk

def calculate():
    """
    Performs the calculation based on the selected operation and
    displays the result.
    """
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()
        result = 0

        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            # Handle division by zero
            if num2 == 0:
                result_label.config(text="Error: Division by zero", fg="red")
                return
            result = num1 / num2
        
        result_label.config(text=f"Result: {result}", fg="blue")

    except ValueError:
        result_label.config(text="Error: Invalid input", fg="red")
        
# Create the main window
root = tk.Tk()
root.title("Basic Calculator")
root.geometry("300x250")

# Input fields for the numbers
label_num1 = tk.Label(root, text="Enter first number:")
label_num1.pack(pady=5)
entry_num1 = tk.Entry(root)
entry_num1.pack()

label_num2 = tk.Label(root, text="Enter second number:")
label_num2.pack(pady=5)
entry_num2 = tk.Entry(root)
entry_num2.pack()

# Dropdown menu for operations
operations = ["Addition", "Subtraction", "Multiplication", "Division"]
operation_var = tk.StringVar(root)
operation_var.set(operations[0])  # Set default value

operation_menu = tk.OptionMenu(root, operation_var, *operations)
operation_menu.pack(pady=10)

# Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack(pady=10)

# Label to display the result
result_label = tk.Label(root, text="Result: ", font=("Helvetica", 12, "bold"))
result_label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()