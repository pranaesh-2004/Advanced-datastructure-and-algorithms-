class EmployeeManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Management System")
        self.employees = []

        self.setup_gui()
    
    def setup_gui(self):
        self.budget_label = tk.Label(root, text="Enter Budget:")
        self.budget_label.pack()
        self.budget_entry = tk.Entry(root)
        self.budget_entry.pack()

        self.department_label = tk.Label(root, text="Enter Department:")
        self.department_label.pack()
        self.department_entry = tk.Entry(root)
        self.department_entry.pack()

        self.name_label = tk.Label(root, text="Enter Employee Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        self.cost_label = tk.Label(root, text="Enter Cost:")
        self.cost_label.pack()
        self.cost_entry = tk.Entry(root)
        self.cost_entry.pack()

        self.performance_label = tk.Label(root, text="Enter Performance:")
        self.performance_label.pack()
        self.performance_entry = tk.Entry(root)
        self.performance_entry.pack()

        self.add_button = tk.Button(root, text="Add Employee", command=self.add_employee)
        self.add_button.pack()

        self.calculate_button = tk.Button(root, text="Calculate Allocation", command=self.calculate_allocation)
        self.calculate_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def add_employee(self):
        try:
            name = self.name_entry.get()
            cost = int(self.cost_entry.get())
            performance = int(self.performance_entry.get())
            department = self.department_entry.get()
            
            employee = {"name": name, "cost": cost, "performance": performance, "department": department}
            self.employees.append(employee)
            
            self.name_entry.delete(0, tk.END)
            self.cost_entry.delete(0, tk.END)
            self.performance_entry.delete(0, tk.END)
            self.department_entry.delete(0, tk.END)
            
            messagebox.showinfo("Success", f"Employee {name} added successfully!")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid cost and performance values.")
    
    def calculate_allocation(self):
        try:
            budget = int(self.budget_entry.get())
            if not self.employees:
                messagebox.showwarning("No Employees", "Please add at least one employee.")
                return

            total_max_value, overall_selected_employees = divide_and_conquer_budget(self.employees, budget)
            result_text = f"Total Maximum Performance: {total_max_value}\nSelected Employees: {', '.join(overall_selected_employees)}"
            self.result_label.config(text=result_text)
        
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid budget.")

if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeManagementApp(root)
    root.mainloop()
