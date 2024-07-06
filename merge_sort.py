import tkinter as tk
import cx_Oracle

class Employee:
    def __init__(self, employee_id, designation, name, age, gender, email, hiredlocation, address, doj, dob, experience, proofid, contactno, status, month, year, basicsalary, totaldays, absents, medical, convence, providentfund, manager_id):
        self.employee_id = employee_id
        self.designation = designation
        self.name = name
        self.age = age
        self.gender = gender
        self.email = email
        self.hiredlocation = hiredlocation
        self.address = address
        self.doj = doj
        self.dob = dob
        self.experience = experience
        self.proofid = proofid
        self.contactno = contactno
        self.status = status
        self.month = month
        self.year = year
        self.basicsalary = basicsalary
        self.totaldays = totaldays
        self.absents = absents
        self.medical = medical
        self.convence = convence
        self.providentfund = providentfund
        self.manager_id = manager_id

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i].name < right_half[j].name:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def merge_sort_employee_details(cursor):
    cursor.execute("SELECT * FROM employee_details")
    employee_details = []
    for row in cursor.fetchall():
        employee_details.append(Employee(*row))  # Pass all row elements as arguments to Employee constructor

    merge_sort(employee_details)
    return employee_details

def display_sorted_employee_details(sorted_employee_details):
    root = tk.Tk()
    root.title("Employee Details Sorter")
    root.geometry("800x600")  # Set window size to 800x600

    text_area = tk.Text(root)
    text_area.pack(fill=tk.BOTH, expand=True)

    for employee in sorted_employee_details:
        text_area.insert(tk.END, f"Employee ID: {employee.employee_id}\n")
        text_area.insert(tk.END, f"Name: {employee.name}\n")
        text_area.insert(tk.END, f"Designation: {employee.designation}\n")
        text_area.insert(tk.END, f"Age: {employee.age}\n")
        text_area.insert(tk.END, f"Gender: {employee.gender}\n")
        text_area.insert(tk.END, f"Email: {employee.email}\n")
        text_area.insert(tk.END, f"Hired Location: {employee.hiredlocation}\n")
        text_area.insert(tk.END, f"Address: {employee.address}\n")
        text_area.insert(tk.END, f"Date of Joining: {employee.doj}\n")
        text_area.insert(tk.END, f"Date of Birth: {employee.dob}\n")
        text_area.insert(tk.END, f"Experience: {employee.experience}\n")
        text_area.insert(tk.END, f"Proof ID: {employee.proofid}\n")
        text_area.insert(tk.END, f"Contact Number: {employee.contactno}\n")
        text_area.insert(tk.END, f"Status: {employee.status}\n")
        text_area.insert(tk.END, f"Month: {employee.month}\n")
        text_area.insert(tk.END, f"Year: {employee.year}\n")
        text_area.insert(tk.END, f"Basic Salary: {employee.basicsalary}\n")
        text_area.insert(tk.END, f"Total Days: {employee.totaldays}\n")
        text_area.insert(tk.END, f"Absents: {employee.absents}\n")
        text_area.insert(tk.END, f"Medical: {employee.medical}\n")
        text_area.insert(tk.END, f"Convenience: {employee.convence}\n")
        text_area.insert(tk.END, f"Provident Fund: {employee.providentfund}\n")
        text_area.insert(tk.END, f"Manager ID: {employee.manager_id}\n")
        text_area.insert(tk.END, "\n")

    root.mainloop()

def merge_sort_and_display(cursor):
    sorted_employee_details = merge_sort_employee_details(cursor)
    display_sorted_employee_details(sorted_employee_details)

if __name__ == "__main__":
    connection = cx_Oracle.connect('system', '1234', 'localhost:1521/ORCL')
    cursor = connection.cursor()
    merge_sort_and_display(cursor)


    cursor.close()
    connection.close()
