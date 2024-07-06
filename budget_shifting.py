import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import cx_Oracle

class CombinedApp2:
    def __init__(self, root):
        self.root = root
        self.root.title("Combined Knapsack Problem Application")
        self.root.geometry("800x600")

        self.notebook = ttk.Notebook(self.root)

        self.frame1 = ttk.Frame(self.notebook)
        self.frame2 = ttk.Frame(self.notebook)

        self.notebook.add(self.frame1, text="Budget Allocation")
        self.notebook.add(self.frame2, text="Shift Scheduling")
        self.notebook.pack(expand=1, fill='both')

        # Load background image for tab 1
        self.bg_image1 = Image.open("bg2.png")
        self.bg_photo1 = ImageTk.PhotoImage(self.bg_image1)

        # Set background for frame 1
        self.set_background(self.frame1, self.bg_photo1)

        self.setup_frame1()

    def set_background(self, frame, bg_photo):
        bg_label = tk.Label(frame, image=bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Establish a connection to the Oracle database
    connection = cx_Oracle.connect('system', '1234', 'localhost:1521/ORCL')

    # Query to fetch Employee IDs, names, and salaries from the "Employee_details" table
    cursor = connection.cursor()
    cursor.execute("SELECT employee_id, name, basicsalary FROM Employee_details")
    employee_data = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    connection.close()

    # Use the fetched data to create dictionaries for quick access
    employee_details = {emp[0]: (emp[1], emp[2]) for emp in employee_data}

    def setup_frame1(self):
        tk.Label(self.frame1, text="Enter Budget:").grid(row=0, column=0, padx=10, pady=10)
        self.budget_var = tk.IntVar()
        self.budget_entry = tk.Entry(self.frame1, textvariable=self.budget_var)
        self.budget_entry.grid(row=0, column=1, padx=10, pady=10)

        # Lock the budget entry after input
        self.budget_entry.bind("<FocusOut>", self.lock_budget_entry)

        tk.Label(self.frame1, text="Employee ID:").grid(row=1, column=0, padx=10, pady=10)
        self.employee_id_var = tk.StringVar()
        self.employee_id_entry = tk.Entry(self.frame1, textvariable=self.employee_id_var)
        self.employee_id_entry.grid(row=1, column=1, padx=10, pady=10)
        self.employee_id_entry.focus()

        tk.Label(self.frame1, text="Employee Name:").grid(row=2, column=0, padx=10, pady=10)
        self.employee_name_var = tk.StringVar()
        self.employee_name_entry = tk.Entry(self.frame1, textvariable=self.employee_name_var, state='readonly')
        self.employee_name_entry.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(self.frame1, text="Basic Salary:").grid(row=3, column=0, padx=10, pady=10)
        self.employee_salary_var = tk.StringVar()
        self.employee_salary_entry = tk.Entry(self.frame1, textvariable=self.employee_salary_var, state='readonly')
        self.employee_salary_entry.grid(row=3, column=1, padx=10, pady=10)

        tk.Button(self.frame1, text="Fill Details", command=self.fill_details).grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        tk.Label(self.frame1, text="Enter Performance:").grid(row=5, column=0, padx=10, pady=10)
        self.performance_var = tk.IntVar()
        self.performance_entry = tk.Entry(self.frame1, textvariable=self.performance_var)
        self.performance_entry.grid(row=5, column=1, padx=10, pady=10)

        tk.Button(self.frame1, text="Add Employee", command=self.add_employee).grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        # Add the "Calculate Allocation" button
        tk.Button(self.frame1, text="Calculate Allocation", command=self.calculate_allocation).grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    def lock_budget_entry(self, event):
        self.budget_entry.config(state='disabled')

    def add_employee(self):
        # Code to add employee to the database
        # After successful addition, clear the fields
        self.clear_fields()

    def clear_fields(self):
        self.employee_id_var.set("")
        self.employee_name_var.set("")
        self.employee_salary_var.set("")

    def fill_details(self):
        employee_id = self.employee_id_var.get()
        if employee_id in self.employee_details:
            name, salary = self.employee_details[employee_id]
            self.employee_name_var.set(name)
            self.employee_salary_var.set(salary)
        else:
            messagebox.showerror("Error", "Invalid Employee ID!")

    def knapsack(self, max_weight, weights, values, n):
        K = [[0 for x in range(max_weight + 1)] for x in range(n + 1)]

        for i in range(n + 1):
            for w in range(max_weight + 1):
                if i == 0 or w == 0:
                    K[i][w] = 0
                elif weights[i-1] <= w:
                    K[i][w] = max(values[i-1] + K[i-1][w-weights[i-1]], K[i-1][w])
                else:
                    K[i][w] = K[i-1][w]

        # Trace back to find selected items
        res = K[n][max_weight]
        w = max_weight
        selected_items = []

        for i in range(n, 0, -1):
            if res <= 0:
                break
            if res == K[i-1][w]:
                continue
            else:
                selected_items.append(i-1)
                res -= values[i-1]
                w -= weights[i-1]

        return K[n][max_weight], selected_items

    def calculate_allocation(self):
        budget = self.budget_var.get()
        performance = self.performance_var.get()

        if budget <= 0:
            messagebox.showerror("Error", "Budget should be a positive integer!")
            return

        if performance <= 0:
            messagebox.showerror("Error", "Performance should be a positive integer!")
            return

        # Prepare data for knapsack algorithm
        employee_ids = list(self.employee_details.keys())
        salaries = [salary for _, (_, salary) in self.employee_details.items()]
        performances = [performance for _ in range(len(employee_ids))]

        # Calculate maximum allocation
        max_allocation, selected_indices = self.knapsack(budget, salaries, performances, len(employee_ids))
        selected_employee_ids = [employee_ids[i] for i in selected_indices]

        # Display result
        messagebox.showinfo("Maximum Allocation", f"Maximum Allocation: {max_allocation}\nSelected Employee IDs: {selected_employee_ids}")


        def visualize_knapsack(self, salaries, performances, selected_employee_ids):
            n = len(salaries)
            selected = [0] * n
            for i in selected_employee_ids:
                selected[i] = 1

            fig, ax = plt.subplots()
            bar_width = 0.35
            index = range(n)

            bar1 = plt.bar(index, salaries, bar_width, alpha=0.4, color='b', label='Salaries')
            bar2 = plt.bar(index, [w * s for w, s in zip(salaries, selected)], bar_width, alpha=0.4, color='r', label='performsnces')

            plt.xlabel('Items')
            plt.ylabel('salaries / performances')
            plt.title('Knapsack Problem Visualization')
            plt.xticks(index, [f'Item {i+1}' for i in index])
            plt.legend()

            plt.tight_layout()
            plt.show()

        visualize_knapsack(self, salaries, performances, selected_employee_ids)


root = tk.Tk()
app = CombinedApp2(root)
root.mainloop()
