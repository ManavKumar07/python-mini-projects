# EMPLOYEE PAYROLL SYSTEM

import json
import os


class EmployeePayroll:

    FILE = "employees.json"

    def __init__(self):
        if not os.path.exists(self.FILE):
            with open(self.FILE, "w") as file:
                json.dump([], file)

    # ---------------- File Handling ----------------

    def load_data(self):
        with open(self.FILE, "r") as file:
            return json.load(file)

    def save_data(self, data):
        with open(self.FILE, "w") as file:
            json.dump(data, file, indent=4)

    # ---------------- Salary Calculation ----------------

    def calculate_salary(self, basic):

        hra = basic * 0.20
        da = basic * 0.10
        pf = basic * 0.08

        net_salary = basic + hra + da - pf

        return hra, da, pf, net_salary

    # ---------------- Add Employee ----------------

    def add_employee(self):

        try:

            emp_id = int(input("Enter Employee ID : "))

            data = self.load_data()

            for emp in data:
                if emp["Employee ID"] == emp_id:
                    print("Employee ID Already Exists.")
                    return

            name = input("Enter Employee Name : ")
            department = input("Enter Department : ")

            basic_salary = float(input("Enter Basic Salary : "))

            hra, da, pf, net = self.calculate_salary(basic_salary)

            employee = {

                "Employee ID": emp_id,
                "Name": name,
                "Department": department,
                "Basic Salary": basic_salary,
                "HRA": hra,
                "DA": da,
                "PF": pf,
                "Net Salary": net

            }

            data.append(employee)
            self.save_data(data)

            print("Employee Added Successfully.")

        except ValueError:
            print("Invalid Input.")

    # ---------------- Display ----------------

    def display_employees(self):

        data = self.load_data()

        if len(data) == 0:
            print("No Employee Found.")
            return

        print("\n========== EMPLOYEE RECORDS ==========\n")

        for emp in data:

            print("Employee ID :", emp["Employee ID"])
            print("Name :", emp["Name"])
            print("Department :", emp["Department"])
            print("Basic Salary :", emp["Basic Salary"])
            print("HRA :", emp["HRA"])
            print("DA :", emp["DA"])
            print("PF :", emp["PF"])
            print("Net Salary :", emp["Net Salary"])
            print("-" * 40)

    # ---------------- Search ----------------

    def search_employee(self):

        emp_id = int(input("Enter Employee ID : "))

        data = self.load_data()

        for emp in data:

            if emp["Employee ID"] == emp_id:

                print("\nEmployee Found\n")

                for key, value in emp.items():
                    print(key, ":", value)

                return

        print("Employee Not Found.")

    # ---------------- Update Salary ----------------

    def update_salary(self):

        emp_id = int(input("Enter Employee ID : "))

        data = self.load_data()

        for emp in data:

            if emp["Employee ID"] == emp_id:

                new_salary = float(input("Enter New Basic Salary : "))

                hra, da, pf, net = self.calculate_salary(new_salary)

                emp["Basic Salary"] = new_salary
                emp["HRA"] = hra
                emp["DA"] = da
                emp["PF"] = pf
                emp["Net Salary"] = net

                self.save_data(data)

                print("Salary Updated Successfully.")
                return

        print("Employee Not Found.")

    # ---------------- Delete ----------------

    def delete_employee(self):

        emp_id = int(input("Enter Employee ID : "))

        data = self.load_data()

        new_data = []

        found = False

        for emp in data:

            if emp["Employee ID"] != emp_id:
                new_data.append(emp)
            else:
                found = True

        if found:

            self.save_data(new_data)

            print("Employee Deleted Successfully.")

        else:
            print("Employee Not Found.")


# ---------------- Main Program ----------------

payroll = EmployeePayroll()

while True:

    print("\n========= EMPLOYEE PAYROLL SYSTEM =========")

    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Search Employee")
    print("4. Update Salary")
    print("5. Delete Employee")
    print("6. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":
        payroll.add_employee()

    elif choice == "2":
        payroll.display_employees()

    elif choice == "3":
        payroll.search_employee()

    elif choice == "4":
        payroll.update_salary()

    elif choice == "5":
        payroll.delete_employee()

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")