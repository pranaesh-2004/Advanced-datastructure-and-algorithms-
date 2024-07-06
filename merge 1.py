import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def __repr__(self):
        return f"Employee(ID: {self.id}, Name: {self.name}, Salary: {self.salary})"

def merge_sort_employees(employees):
    if len(employees) > 1:
        mid = len(employees) // 2
        left_half = employees[:mid]
        right_half = employees[mid:]

        merge_sort_employees(left_half)
        merge_sort_employees(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i].salary <= right_half[j].salary:
                employees[k] = left_half[i]
                i += 1
            else:
                employees[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            employees[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            employees[k] = right_half[j]
            j += 1
            k += 1

def visualize_employee_salaries(employees):
    salaries = [emp.salary for emp in employees]
    fig, ax = plt.subplots()
    ax.set_title("Employee Salary Visualization")
    ax.bar(range(len(employees)), salaries, color='skyblue')

    def update_fig(salaries, rects):
        for rect, val in zip(rects, salaries):
            rect.set_height(val)

    n = len(employees)
    rects = ax.bar(range(n), salaries, color='skyblue')
    plt.draw()

    for i in range(n):
        for j in range(n-i-1):
            if salaries[j] > salaries[j+1]:
                salaries[j], salaries[j+1] = salaries[j+1], salaries[j]
                employees[j], employees[j+1] = employees[j+1], employees[j]
                update_fig(salaries, rects)
                plt.pause(0.1)

def add_employee():
    try:
        id = int(entry_id.get())
        name = entry_name.get()
        salary = float(entry_salary.get())
        employees.append(Employee(id, name, salary))
        display_employees()
        entry_id.delete(0, tk.END)
        entry_name.delete(0, tk.END)
        entry_salary.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid data.")

def display_employees():
    text_area.delete('1.0', tk.END)
    for emp in employees:
        text_area.insert(tk.END, f"{emp}\n")

def sort_employees():
    merge_sort_employees(employees)
    display_employees()
    visualize_employee_salaries(employees.copy())

# Create the main window
root = tk.Tk()
root.title("Employee Payroll System")

# List to store employees
employees = []

# Create input fields and labels
tk.Label(root, text="Employee ID:").grid(row=0, column=0, padx=10, pady=5)
entry_id = tk.Entry(root)
entry_id.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Employee Name:").grid(row=1, column=0, padx=10, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Employee Salary:").grid(row=2, column=0, padx=10, pady=5)
entry_salary = tk.Entry(root)
entry_salary.grid(row=2, column=1, padx=10, pady=5)

# Create buttons
btn_add = tk.Button(root, text="Add Employee", command=add_employee)
btn_add.grid(row=3, column=0, columnspan=2, pady=10)

btn_sort = tk.Button(root, text="Sort by Salary", command=sort_employees)
btn_sort.grid(row=4, column=0, columnspan=2, pady=10)

# Create text area for output
text_area = tk.Text(root, height=15, width=50)
text_area.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

plt.ion()  # Turn on interactive mode
plt.show()

root.mainloop()
