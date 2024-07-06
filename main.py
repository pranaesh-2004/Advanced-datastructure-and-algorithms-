from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
import random
import time
import os
import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import tempfile
from tkcalendar import *
from tkinter import messagebox
import bfs import login

class PayrollApp():
    def __init__(self,root):
        self.root=root
        self.root.title("Employee Payroll Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

##################################### Frame 1 Variable
        self.employeecode=StringVar()
        self.designation = StringVar()
        self.name = StringVar()
        self.age = StringVar()
        self.gender = StringVar()
        self.email= StringVar()
        self.hiredlocation = StringVar()
        self.txt_address = StringVar()

        ##################################### Frame 2 Variable
        self.doj = StringVar()
        self.dob = StringVar()
        self.experience = StringVar()
        self.proofid = StringVar()
        self.contactno = StringVar()
        self.status= StringVar()

        ##################################### Frame 3 Variable
        self.month = StringVar()
        self.year = StringVar()
        self.basicsalary = StringVar()
        self.totaldays = StringVar()
        self.absents = StringVar()
        self.medical= StringVar()
        self.convence = StringVar()
        self.providentfund = StringVar()
        self.operator=StringVar()



        title1 = Label(self.root, text="EMPLOYEE PAYROLL MANAGEMENT SYSTEM",font=("times new roman", 20), bd=20, bg="green", fg="white",relief=GROOVE,anchor=W).pack(side=TOP,fill=X)
        btn_logout=Button(title1,text="LOGOUT",bg="red",fg="white",bd=1,height=1,width=10,command=self.logout).place(x=1250,y=25)
        btn_allemployee = Button(title1, text="All Employee's", font=("times new roman",12, "bold"),bg="green", command=self.employee_frame,fg="white", bd=1, height=1, width=15).place(x=1100, y=23)

#######################################################################################################

        frame1=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        frame1.place(x=5,y=70,width=790,height=575)
        title2=Label(frame1,text="Employee Details",font=("times new roman",20),bd=1,bg="lightgray",relief=GROOVE).pack(side=TOP,fill=X)
####ROW1 Label
        lbl_code = Label(frame1, text="Employee code:", font=("times new roman",15),bg="white").place(x=10,y=50)
        lbl_designation = Label(frame1, text="Designation:", font=("times new roman", 15), bg="white").place(x=10, y=100)
        lbl_name = Label(frame1, text="Name:", font=("times new roman", 15), bg="white").place(x=10,y=150)
        lbl_age = Label(frame1, text="Age:", font=("times new roman", 15), bg="white").place(x=10, y=200)
        lbl_gender = Label(frame1, text="Gender:", font=("times new roman", 15), bg="white").place(x=10,y=250)
        lbl_email = Label(frame1, text="Email:", font=("times new roman", 15), bg="white").place(x=10,y=300)
        lbl_hiredlocation = Label(frame1, text="Hired Location:", font=("times new roman", 15), bg="white").place(x=10, y=350)
        lbl_address = Label(frame1, text="Address:", font=("times new roman", 15), bg="white").place(x=10,y=400)

        ####ROW1 Entry Text
        self.txt_code=Entry(frame1,fg="black",bg="lightyellow",font=("times new roman",12),textvariable=self.employeecode,width=50)
        self.txt_code.place(x=150,y=50)
        btn_search=Button(frame1,text="Search",bg="white",fg="black",height=1,width=8,command=self.search).place(x=560,y=50)

        txt_designation=Entry(frame1,fg="black",bg="lightyellow",font=("times new roman",12),textvariable=self.designation,width=30).place(x=150,y=100)
        txt_name = Entry(frame1, fg="black", bg="lightyellow", font=("times new roman", 12),textvariable=self.name, width=30).place(x=150, y=150)
        txt_age = Entry(frame1, fg="black", bg="lightyellow", font=("times new roman", 12),textvariable=self.age, width=30).place( x=150, y=200)
        txt_gender = Entry(frame1, fg="black", bg="lightyellow", font=("times new roman", 12),textvariable=self.gender, width=30).place(x=150, y=250)
        txt_email = Entry(frame1, fg="black", bg="lightyellow", font=("times new roman", 12),textvariable=self.email, width=30).place(x=150, y=300)
        txt_hiredlocation = Entry(frame1, fg="black", bg="lightyellow", font=("times new roman", 12),textvariable=self.hiredlocation, width=30).place(x=150,y=350)
        self.txt_address = Text(frame1, fg="black", bg="lightyellow", font=("times new roman", 12), width=70,height=8)
        self.txt_address.place( x=150, y=400)
#######################################################################################################
####ROW2 Label

        lbl_doj = Label(frame1, text="D.O.J:", font=("times new roman", 15), bg="white").place(x=410, y=100)
        lbl_dob= Label(frame1, text="D.O.B:", font=("times new roman", 15), bg="white").place(x=410,y=150)
        lbl_experience = Label(frame1, text="Experience:", font=("times new roman", 15), bg="white").place(x=410, y=200)
        lbl_proofid = Label(frame1, text="Proof ID:", font=("times new roman", 15), bg="white").place(x=410,y=250)
        lbl_contactno = Label(frame1, text="Contact No:", font=("times new roman", 15), bg="white").place(x=410,y=300)
        lbl_status= Label(frame1, text="Status:", font=("times new roman", 15), bg="white").place(x=410, y=350)


        ####ROW2 Entry Text
        txt_doj = Entry(frame1, fg="black", bg="lightyellow", font=("times new roman", 12),textvariable=self.doj, width=30).place( x=530, y=100)
        txt_dob = Entry(frame1, fg="black", bg="lightyellow", font=("times new roman", 12),textvariable=self.dob, width=30).place(x=530, y=150)
        txt_experience = Entry(frame1, fg="black", bg="lightyellow", font=("times new roman", 12),textvariable=self.experience, width=30).place(x=530, y=200)
        txt_proofid= Entry(frame1, fg="black", bg="lightyellow", font=("times new roman", 12),textvariable=self.proofid, width=30).place(x=530, y=250)
        txt_contactno = Entry(frame1, fg="black", bg="lightyellow", font=("times new roman", 12),textvariable=self.contactno, width=30).place(x=530, y=300)
        txt_status = Entry(frame1, fg="black", bg="lightyellow", font=("times new roman", 12),textvariable=self.status, width=30).place(x=530,y=350)

        frame2=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        frame2.place(x=800,y=70,width=545,height=575)
        title3=Label(frame2,text="Employee Salary Details",font=("times new roman",20),bd=1,bg="lightgray",relief=GROOVE).pack(side=TOP,fill=X)




        lbl_month = Label(frame2, text="Month:", font=("times new roman",15),bg="white").place(x=10,y=50)
        lbl_year = Label(frame2, text="Year:", font=("times new roman", 15), bg="white").place(x=10, y=100)
        lbl_basicsalary = Label(frame2, text="Basic Salary:", font=("times new roman", 15), bg="white").place(x=10,y=150)
        lbl_totaldays = Label(frame2, text="Total Days:", font=("times new roman", 15), bg="white").place(x=10, y=200)
        lbl_absents = Label(frame2, text="Absents:", font=("times new roman", 15), bg="white").place(x=10,y=250)
        lbl_medical = Label(frame2, text="Medical:", font=("times new roman", 15), bg="white").place(x=10,y=300)
        lbl_convence = Label(frame2, text="Convence:", font=("times new roman", 15), bg="white").place(x=10, y=350)
        lbl_providentfund = Label(frame2, text="Provident Fund:", font=("times new roman", 15), bg="white").place(x=10,y=400)
        lbl_knapsack = Label(frame2, text="Knapsack:", font=("times new roman", 15), bg="white").place(x=10,y=450)


        txt_month = Entry(frame2, fg="black", bg="lightyellow", font=("times new roman", 12),textvariable=self.month, width=25).place(x=150, y=50)
        txt_year = Entry(frame2, fg="black", bg="lightyellow", font=("times new roman", 12),textvariable=self.year, width=25).place(x=150,y=100)
        txt_basicsalary = Entry(frame2, fg="black", bg="lightyellow", font=("times new roman", 12),textvariable=self.basicsalary, width=25).place( x=150, y=150)
        txt_tataldays = Entry(frame2, fg="black", bg="lightyellow", font=("times new roman", 12),textvariable=self.totaldays, width=25).place(x=150, y=200)
        txt_absents = Entry(frame2, fg="black", bg="lightyellow", font=("times new roman", 12),textvariable=self.absents, width=25).place(x=150, y=250)
        txt_medical = Entry(frame2, fg="black", bg="lightyellow", font=("times new roman", 12),textvariable=self.medical, width=25).place( x=150, y=300)
        txt_convence = Entry(frame2, fg="black", bg="lightyellow", font=("times new roman", 12),textvariable=self.convence, width=25).place(x=150, y=350)
        txt_providentfund = Entry(frame2, fg="black", bg="lightyellow", font=("times new roman", 12),textvariable=self.providentfund, width=25).place(x=150, y=400)
        #txt_netsalary = Entry(frame2, fg="black", bg="lightyellow", font=("times new roman", 12),textvariable=self.netsalary, width=13,state=DISABLED).place(x=365, y=200)
        

        btn_calculate=Button(frame2,text="Calculate Net Salary",bg="yellow",fg="black",height=1,width=20,command=self.calculate_knapsack).place(x=125,y=450)

        self.btn_insert = Button(frame2, text="Insert", bg="lightgreen", fg="black", height=1, width=8,command=self.add)
        self.btn_insert.place(x=125, y=515)

        self.btn_clear = Button(frame2, text="Clear", bg="lightgray", fg="black", height=1, width=8,command=self.clear)
        self.btn_clear.place(x=225, y=515)

        self.btn_update = Button(frame2, text="Update", bg="lightblue", fg="black", height=1, width=8,command=self.update)
        self.btn_update.place(x=325, y=515)

        self.btn_delete = Button(frame2, text="Delete", bg="red", fg="black", height=1, width=8,command=self.delete)
        self.btn_delete.place(x=425, y=515)


########################################################################################################Calculator
    def calculate_knapsack(self):
        root.destroy()
        from budget_shifting import CombinedApp1

###############################################################################

    def check_connection(self):
        try:
            sqlplus_cmd = 'sqlplus system/1234@localhost:1521/ORCL'
            query = "SELECT * FROM employee_details;"
            
            result = subprocess.check_output(f'echo "{query}" | {sqlplus_cmd}', shell=True).decode()
            rows = result.split('\n')
            
            if len(rows) < 3:
                messagebox.showerror("Error", "No data found in the employee_details table")
            else:
                # Process the retrieved rows as needed
                for row in rows[2:]:
                    data = row.split()
                    # Process each row data as required

        except subprocess.CalledProcessError as ex:
            messagebox.showerror("Error", f"SQL*Plus command failed with error: {str(ex)}")
        except Exception as ex:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(ex)}")

######################################################################################################
        
    def add(self):
        # Establish a connection to the Oracle database
        try:
            connection = cx_Oracle.connect('system', '1234', 'localhost:1521/ORCL')
            cursor = connection.cursor()
            
            # Prepare the INSERT statement
            insert_query = "INSERT INTO employee_details (employee_ID, designation, name, age, gender, email, hiredlocation, address, doj, dob, experience, proofid, contactno, status, month, year, Basicsalary, totaldays, absents, medical, providentfund, convence) VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12, :13, :14, :15, :16, :17, :18, :19, :20, :21, :22)"
            
            # Retrieve values from entry widgets
            values = (
                self.employeecode.get(), self.designation.get(), self.name.get(), self.age.get(),
                self.gender.get(), self.email.get(), self.hiredlocation.get(), self.txt_address.get("1.0", END),
                self.doj.get(), self.dob.get(), self.experience.get(), self.proofid.get(), self.contactno.get(),
                self.status.get(), self.month.get(), self.year.get(), self.basicsalary.get(), self.totaldays.get(),
                self.absents.get(), self.medical.get(), self.convence.get(), self.providentfund.get()
            )

            # Execute the INSERT statement with values
            cursor.execute(insert_query, values)
            
            # Commit the transaction
            connection.commit()
            
            # Close the cursor and connection
            cursor.close()
            connection.close()
            
            messagebox.showinfo("Success", "Employee details inserted successfully.")
            
        except cx_Oracle.Error as error:
            messagebox.showerror("Error", f"Error while inserting employee details: {error}")

                
######################################################################################################

    def show(self):
        print("Show")

######################################################################################################
        
    def search(self):
        try:
            # Establish a connection to the Oracle database
            connection = cx_Oracle.connect('system', '1234', 'localhost:1521/ORCL')
            cursor = connection.cursor()
            
            # Get employee code
            employee_id = self.employeecode.get()
            if not employee_id:
                messagebox.showerror("Error", "Employee code must not be empty.")
                return
            
            queue = [employee_id]
            visited = set()
            
            while queue:
                current_employee_id = queue.pop(0)
                if current_employee_id in visited:
                    continue
                visited.add(current_employee_id)
                
                # Prepare and execute the SELECT statement to fetch employee details
                select_query = """
                    SELECT employee_ID, designation, name, age, gender, email, hiredlocation, address,
                           doj, dob, experience, proofid, contactno, status, month, year, basicsalary,
                           totaldays, absents, medical, convence, providentfund, manager_ID
                    FROM employee_details
                    WHERE employee_ID = :1
                """
                cursor.execute(select_query, (current_employee_id,))
                row = cursor.fetchone()
                
                if row:
                    # Populate the entry fields with the retrieved data
                    self.designation.set(row[1])
                    self.name.set(row[2])
                    self.age.set(row[3])
                    self.gender.set(row[4])
                    self.email.set(row[5])
                    self.hiredlocation.set(row[6])
                    self.txt_address.delete('1.0', END)
                    self.txt_address.insert(END, row[7])
                    self.doj.set(row[8])
                    self.dob.set(row[9])
                    self.experience.set(row[10])
                    self.proofid.set(row[11])
                    self.contactno.set(row[12])
                    self.status.set(row[13])
                    self.month.set(row[14])
                    self.year.set(row[15])
                    self.basicsalary.set(row[16])
                    self.totaldays.set(row[17])
                    self.absents.set(row[18])
                    self.medical.set(row[19])
                    self.convence.set(row[20])
                    self.providentfund.set(row[21])
                    
                    # Fetch employees managed by the current employee
                    cursor.execute("SELECT employee_ID FROM employee_details WHERE manager_ID = :1", (current_employee_id,))
                    managed_employees = cursor.fetchall()
                    
                    for emp in managed_employees:
                        queue.append(emp[0])
                else:
                    messagebox.showerror("Error", f"No data found for employee ID {current_employee_id}")
            
            # Close the cursor and connection
            cursor.close()
            connection.close()
            
        except cx_Oracle.Error as error:
            #messagebox.showerror("Error", f"Error while fetching employee details: {error}")
            print(error)

#UPDATE####################################################################################################

    def update(self):
        try:
            connection = cx_Oracle.connect('system', '1234', 'localhost:1521/ORCL')
            cursor = connection.cursor()
            
            # Prepare the UPDATE statement
            update_query = """
                UPDATE employee_details
                SET designation = :1, name = :2, age = :3, gender = :4, email = :5, hiredlocation = :6, address = :7,
                    doj = :8, dob = :9, experience = :10, proofid = :11, contactno = :12, status = :13,
                    month = :14, year = :15, Basicsalary = :16, totaldays = :17, absents = :18, medical = :19,
                    providentfund = :20, convence = :21
                WHERE employee_ID = :22
            """
            
            # Retrieve values from entry widgets
            values = (
                self.designation.get(), self.name.get(), self.age.get(), self.gender.get(), self.email.get(),
                self.hiredlocation.get(), self.txt_address.get("1.0", END), self.doj.get(), self.dob.get(),
                self.experience.get(), self.proofid.get(), self.contactno.get(), self.status.get(),
                self.month.get(), self.year.get(), self.basicsalary.get(), self.totaldays.get(),
                self.absents.get(), self.medical.get(), self.convence.get(), self.providentfund.get(),
                self.employeecode.get()
            )
            
            # Execute the UPDATE statement with values
            cursor.execute(update_query, values)
            
            # Commit the transaction
            connection.commit()
            
            # Close the cursor and connection
            cursor.close()
            connection.close()
            
            messagebox.showinfo("Success", "Employee details updated successfully.")
        
        except cx_Oracle.Error as error:
            messagebox.showerror("Error", f"Error while updating employee details: {error}")


######################################################################################################
    def clear(self):
        self.btn_insert.config(state=NORMAL)
        self.btn_update.config(state=DISABLED)
        self.btn_delete.config(state=DISABLED)
        self.txt_code.config(state=NORMAL)

        self.employeecode.set("")
        self.designation.set("")
        self.name.set("")
        self.age.set("")
        self.gender.set("")
        self.email.set("")
        self.hiredlocation.set("")
        self.txt_address.delete('1.0',END)
        self.doj.set("")
        self.dob.set("")
        self.experience.set("")
        self.proofid.set("")
        self.contactno.set("")
        self.status.set("")

        ############################################
        self.month.set("")
        self.year.set("")
        self.basicsalary.set("")
        self.totaldays.set("")
        self.absents.set("")
        self.medical.set("")
        self.convence.set("")
        self.providentfund.set("")
        


######################################################################################################
    def delete(self):
        try:
            # Establish a connection to the Oracle database
            connection = cx_Oracle.connect('system', '1234', 'localhost:1521/ORCL')
            cursor = connection.cursor()
            
            # Prepare the DELETE statement to remove the employee row based on the employee ID
            delete_query = "DELETE FROM employee_details WHERE employee_ID = :1"
            
            # Execute the DELETE statement with the employee code
            cursor.execute(delete_query, (self.employeecode.get(),))
            # Commit the transaction
            connection.commit()
            
            # Close the cursor and connection
            cursor.close()
            connection.close()
            
            messagebox.showinfo("Success", "Employee details deleted successfully.")
        
        except cx_Oracle.Error as error:
            messagebox.showerror("Error", f"Error while deleting employee details: {error}")
            
###########################################################################################################################

    def logout(self):
        logout= messagebox.askyesno("Employee Payroll Management", "Confirm if you want to exit")
        if logout > 0:
            root.destroy()
            return

 ###################################### EMPLOYEE GRID VIEW OR TREE VIEW ################################################################
    '''def employee_frame(self):
        self.root2=Toplevel(self.root)
        self.root2.title("Employee Payroll Management System")
        self.root2.geometry("1000x500+120+60")
        self.root2.config(bg="white")
        title=Label(self.root2,text="All Employee Details",font=("times new roman",20,"bold"),fg="white",bg="green",anchor=W).pack(side=TOP,fill=X)
        self.root2.focus_force()
 ######################################################################################################

        scrolly=Scrollbar(self.root2, orient=VERTICAL)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx=Scrollbar(self.root2, orient=HORIZONTAL)
        scrollx.pack(side=BOTTOM, fill=X)

        self.Employee_tree = ttk.Treeview(self.root2,columns=("employee_ID", "designation", "name", "age", "gender",
                                                              "email", "hiredlocation", "address", "doj", "dob",
                                                              "experience", "proofid", "contactno", "status","month",
                                                              "year", "Basicsalary", "totaldays", "absents","medical",
                                                              "providentfund", "convence"),yscrollcommand=scrolly.set,
                                                                 xscrollcommand=scrollx.set)


        self.Employee_tree.heading("employee_ID", text="employee_ID")
        self.Employee_tree.heading("designation", text="designation.")
        self.Employee_tree.heading("name", text="name")
        self.Employee_tree.heading("age", text="age")
        self.Employee_tree.heading("gender", text="gender")
        self.Employee_tree.heading("email", text="email")
        self.Employee_tree.heading("hiredlocation", text="hiredlocation")
        self.Employee_tree.heading("address", text="address")
        self.Employee_tree.heading("doj", text="doj")
        self.Employee_tree.heading("dob", text="dob")
        self.Employee_tree.heading("experience", text="experience")
        self.Employee_tree.heading("proofid", text="proofid")
        self.Employee_tree.heading("contactno", text="contactno")
        self.Employee_tree.heading("status", text="status")
        self.Employee_tree.heading("month", text="month")
        self.Employee_tree.heading("year", text="year")
        self.Employee_tree.heading("Basicsalary", text="Basicsalary")
        self.Employee_tree.heading("totaldays", text="totaldays")
        self.Employee_tree.heading("absents", text="absents")
        self.Employee_tree.heading("medical", text="medical")
        self.Employee_tree.heading("providentfund", text="providentfund")
        self.Employee_tree.heading("convence", text="convence")
        

        self.Employee_tree["show"] = "headings"

        self.Employee_tree.column("employee_ID", width=100)
        self.Employee_tree.column("designation", width=100)
        self.Employee_tree.column("name", width=100)
        self.Employee_tree.column("age", width=100)
        self.Employee_tree.column("gender", width=100)
        self.Employee_tree.column("email",width=100)
        self.Employee_tree.column("hiredlocation",width=100)
        self.Employee_tree.column("address", width=100)
        self.Employee_tree.column("doj", width=100)
        self.Employee_tree.column("dob", width=100)
        self.Employee_tree.column("experience", width=100)
        self.Employee_tree.column("proofid",width=100)
        self.Employee_tree.column("contactno",width=100)
        self.Employee_tree.column("status", width=100)
        self.Employee_tree.column("month",width=100)
        self.Employee_tree.column("year", width=100)
        self.Employee_tree.column("Basicsalary",width=100)
        self.Employee_tree.column("totaldays",width=100)
        self.Employee_tree.column("absents", width=100)
        self.Employee_tree.column("medical",width=100)
        self.Employee_tree.column("providentfund", width=100)
        self.Employee_tree.column("convence",width=100)
        
        scrollx.config(command=self.Employee_tree.xview)
        scrolly.config(command=self.Employee_tree.yview)
        self.Employee_tree.pack(fill=BOTH, expand=1)
        self.show()'''


    def employee_frame(self):
        print("Clicked Employees")

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
                
                text_area.insert(tk.END, f"\nEmployee ID: {employee.employee_id}\n")
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
                text_area.insert(tk.END, "\n*****************************************************************************\n")

            root.mainloop()

        def merge_sort_and_display(cursor):
            sorted_employee_details = merge_sort_employee_details(cursor)
            display_sorted_employee_details(sorted_employee_details)

        if __name__ == "__main__":
            connection = cx_Oracle.connect('system', '1234', 'localhost:1521/ORCL')
            cursor = connection.cursor()


            cursor.close()
            connection.close()
            import bfs


        
        

######################################################################################################

root = Tk()
app = PayrollApp(root)
root.mainloop()
