import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

class CombinedApp:
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

        # Load background images
        self.bg_image1 = Image.open("bg2.png")
        self.bg_photo1 = ImageTk.PhotoImage(self.bg_image1)

        self.bg_image2 = Image.open("bg3.png")
        self.bg_photo2 = ImageTk.PhotoImage(self.bg_image2)

        # Set backgrounds for frames
        self.set_background(self.frame1, self.bg_photo1)
        self.set_background(self.frame2, self.bg_photo2)

        self.setup_frame1()
        self.setup_frame2()

    def set_background(self, frame, bg_photo):
        bg_label = tk.Label(frame, image=bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Knapsack algorithm implementation
    def knapsack(max_weight, weights, values, n):
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

    def visualize_knapsack(weights, values, selected_items):
        n = len(weights)
        selected = [0] * n
        for i in selected_items:
            selected[i] = 1

        fig, ax = plt.subplots()
        bar_width = 0.35
        index = range(n)

        bar1 = plt.bar(index, values, bar_width, alpha=0.4, color='b', label='Value')
        bar2 = plt.bar(index, [w * s for w, s in zip(weights, selected)], bar_width, alpha=0.4, color='r', label='Weight')

        plt.xlabel('Items')
        plt.ylabel('Value / Weight')
        plt.title('Knapsack Problem Visualization')
        plt.xticks(index, [f'Item {i+1}' for i in index])
        plt.legend()

        plt.tight_layout()
        plt.show()

        
    def setup_frame1(self):
        self.budget_label = ttk.Label(self.frame1, text="Enter Budget:")
        self.budget_label.pack(pady=10)
        self.budget_entry = ttk.Entry(self.frame1)
        self.budget_entry.pack(pady=10)

        self.employees1 = []
        
        self.name_label1 = ttk.Label(self.frame1, text="Enter Employee Name:")
        self.name_label1.pack(pady=10)
        self.name_entry1 = ttk.Entry(self.frame1)
        self.name_entry1.pack(pady=10)

        self.cost_label1 = ttk.Label(self.frame1, text="Enter Cost:")
        self.cost_label1.pack(pady=10)
        self.cost_entry1 = ttk.Entry(self.frame1)
        self.cost_entry1.pack(pady=10)

        self.performance_label1 = ttk.Label(self.frame1, text="Enter Performance:")
        self.performance_label1.pack(pady=10)
        self.performance_entry1 = ttk.Entry(self.frame1)
        self.performance_entry1.pack(pady=10)

        self.add_button1 = ttk.Button(self.frame1, text="Add Employee", command=self.add_employee1)
        self.add_button1.pack(pady=10)

        self.calculate_button1 = ttk.Button(self.frame1, text="Calculate Allocation", command=self.calculate_allocation1)
        self.calculate_button1.pack(pady=10)

        self.result_label1 = ttk.Label(self.frame1, text="")
        self.result_label1.pack(pady=10)

        self.visualize_button1 = ttk.Button(self.frame1, text="Visualize Allocation", command=self.visualize_allocation1)
        self.visualize_button1.pack(pady=10)

    def add_employee1(self):
        try:
            name = self.name_entry1.get()
            cost = int(self.cost_entry1.get())
            performance = int(self.performance_entry1.get())
            
            self.employees1.append((name, cost, performance))
            
            self.name_entry1.delete(0, tk.END)
            self.cost_entry1.delete(0, tk.END)
            self.performance_entry1.delete(0, tk.END)
            
            messagebox.showinfo("Success", f"Employee {name} added successfully!")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid cost and performance values.")
    
    def calculate_allocation1(self):
        try:
            budget = int(self.budget_entry.get())
            if not self.employees1:
                messagebox.showwarning("No Employees", "Please add at least one employee.")
                return

            names = [emp[0] for emp in self.employees1]
            costs = [emp[1] for emp in self.employees1]
            performances = [emp[2] for emp in self.employees1]

            self.max_value1, self.selected_indices1 = knapsack(budget, costs, performances, len(self.employees1))
            selected_employees = [names[i] for i in self.selected_indices1]
            
            result_text = f"Maximum Performance: {self.max_value1}\nSelected Employees: {', '.join(selected_employees)}"
            self.result_label1.config(text=result_text)
        
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid budget.")

    def visualize_allocation1(self):
        if hasattr(self, 'max_value1') and hasattr(self, 'selected_indices1'):
            costs = [emp[1] for emp in self.employees1]
            performances = [emp[2] for emp in self.employees1]
            visualize_knapsack(costs, performances, self.selected_indices1)
        else:
            messagebox.showwarning("No Calculation", "Please calculate the allocation first.")

    def setup_frame2(self):
        self.capacity_label = ttk.Label(self.frame2, text="Enter Shift Capacity (hours):")
        self.capacity_label.pack(pady=10)
        self.capacity_entry = ttk.Entry(self.frame2)
        self.capacity_entry.pack(pady=10)

        self.employees2 = []
        
        self.name_label2 = ttk.Label(self.frame2, text="Enter Employee Name:")
        self.name_label2.pack(pady=10)
        self.name_entry2 = ttk.Entry(self.frame2)
        self.name_entry2.pack(pady=10)

        self.hours_label = ttk.Label(self.frame2, text="Enter Availability (hours):")
        self.hours_label.pack(pady=10)
        self.hours_entry = ttk.Entry(self.frame2)
        self.hours_entry.pack(pady=10)

        self.efficiency_label = ttk.Label(self.frame2, text="Enter Efficiency:")
        self.efficiency_label.pack(pady=10)
        self.efficiency_entry = ttk.Entry(self.frame2)
        self.efficiency_entry.pack(pady=10)

        self.add_button2 = ttk.Button(self.frame2, text="Add Employee", command=self.add_employee2)
        self.add_button2.pack(pady=10)

        self.calculate_button2 = ttk.Button(self.frame2, text="Calculate Schedule", command=self.calculate_schedule)
        self.calculate_button2.pack(pady=10)

        self.result_label2 = ttk.Label(self.frame2, text="")
        self.result_label2.pack(pady=10)

        self.visualize_button2 = ttk.Button(self.frame2, text="Visualize Schedule", command=self.visualize_schedule)
        self.visualize_button2.pack(pady=10)

    def add_employee2(self):
        try:
            name = self.name_entry2.get()
            hours = int(self.hours_entry.get())
            efficiency = int(self.efficiency_entry.get())
            
            self.employees2.append((name, hours, efficiency))
            
            self.name_entry2.delete(0, tk.END)
            self.hours_entry.delete(0, tk.END)
            self.efficiency_entry.delete(0, tk.END)
            
            messagebox.showinfo("Success", f"Employee {name} added successfully!")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid hours and efficiency values.")
    
    def calculate_schedule(self):
        try:
            capacity = int(self.capacity_entry.get())
            if not self.employees2:
                messagebox.showwarning("No Employees", "Please add at least one employee.")
                return

            names = [emp[0] for emp in self.employees2]
            hours = [emp[1] for emp in self.employees2]
            efficiencies = [emp[2] for emp in self.employees2]

            self.max_value2, self.selected_indices2 = knapsack(capacity, hours, efficiencies, len(self.employees2))
            selected_employees = [names[i] for i in self.selected_indices2]
            
            result_text = f"Maximum Efficiency: {self.max_value2}\nSelected Employees: {', '.join(selected_employees)}"
            self.result_label2.config(text=result_text)
        
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid shift capacity.")

    def visualize_schedule(self):
        if hasattr(self, 'max_value2') and hasattr(self, 'selected_indices2'):
            hours = [emp[1] for emp in self.employees2]
            efficiencies = [emp[2] for emp in self.employees2]
            visualize_knapsack(hours, efficiencies, self.selected_indices2)
        else:
            messagebox.showwarning("No Calculation", "Please calculate the schedule first.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CombinedApp(root)
    root.mainloop()
