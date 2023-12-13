import tkinter as tk

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        operation = operation_var.get()

        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            if num2 == 0:
                result = "Error! Division by zero"
            else:
                result = num1 / num2
        elif operation == "Modulus":
            result = num1 % num2        

        result_label.config(text="Result: " + str(result))
    except ValueError:
        result_label.config(text="Invalid input! Please enter valid numbers.")
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x200")
L1 =tk.Label(root, text="FIRST INPUT")
L1.grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)
L2 =tk.Label(root, text="SECOND INPUT")
L2.grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1,column=1)
operations = ["Addition", "Subtraction", "Multiplication", "Division","Modulus"]
operation_var = tk.StringVar(root)
operation_var.set(operations[0])

operation_dropdown = tk.OptionMenu(root, operation_var, *operations)
operation_dropdown.grid(row=2,column=1)

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=3,column=1)

result_label = tk.Label(root)
result_label.grid(row=4,column=1)

root.mainloop()