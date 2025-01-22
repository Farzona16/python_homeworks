import os

class Employee:
    def __init__(self,employee_id,name,position,salary):
        self.employee_id=employee_id
        self.name=name
        self.position=position
        self.salary=salary
    
    def str(self):
        return f"{self.employee_id},{self.name}, {self.position},{self.salary}"
    
    @staticmethod
    def from_string(data):
        employee_id, name, position,salary= data.split(', ')
        return Employee(employee_id,name,position,float(salary))

class EmployeeManager:
    my_file='employees.txt'
    
    def __init__(self):
        if not os.path.exists(self.my_file):
            with open(self.my_file, 'w') as f:
                pass
    
    def add_employee(self):
        employee_id=input("Enter the employee id: ").strip()
        if self.search_employee(employee_id):
            print("This employee id already exists:")
            return
        name=input("Enter name: ")
        position=input("Enter position: ")
        salary=float(input("Enter salary: "))
        employee=Employee(employee_id,name,position,salary)
        with open(self.my_file,'a') as f:
            f.write(str(employee)+'\n')
        print("Employee added successfully")

    def view_employee(self):
        with open(self.my_file,'r') as f:
            records=f.readlines()
        if not records:
            print("No records found")
            return
        print("Employee records: ")
        for record in records:
            print(record.strip())

    def search_employee(self,employee_id):
        with open(self.my_file, 'r') as f:
            for line in f:
                employee=Employee.from_string(line.strip())
                if employee.employee_id==employee_id:
                    return employee
        return None
    
    def update_employee(self):
        employee_id = input("Enter Employee ID to update: ").strip()
        employee = self.search_employee(employee_id)
        if not employee:
            print("Error: Employee not found.")
            return

        print(f"Current Record: {employee}")
        name = input(f"Enter New Name (leave blank to keep '{employee.name}'): ").strip() or employee.name
        position = input(f"Enter New Position (leave blank to keep '{employee.position}'): ").strip() or employee.position
        salary_input = input(f"Enter New Salary (leave blank to keep '{employee.salary}'): ").strip()
        salary = float(salary_input) if salary_input else employee.salary

        updated_employee = Employee(employee_id, name, position, salary)
        self._update_file(employee_id, str(updated_employee))
        print("Employee updated successfully!")
  
    def delete_employee(self):
        employee_id = input("Enter Employee ID to delete: ").strip()
        if not self.search_employee(employee_id):
            print("Error: Employee not found.")
            return

        self._update_file(employee_id, None)
        print("Employee deleted successfully!")

    def update_file(self, employee_id, new_data):
        with open(self.FILE_NAME, 'r') as f:
            lines = f.readlines()
        with open(self.FILE_NAME, 'w') as f:
            for line in lines:
                employee = Employee.from_string(line.strip())
                if employee.employee_id == employee_id:
                    if new_data:
                        f.write(new_data + "\n")
                else:
                    f.write(line)

    def run(self):
        while True:
            print("\nWelcome to the Employee Records Manager!")
            print("1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Exit")
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.view_all_employees()
            elif choice == "3":
                employee_id = input("Enter Employee ID to search: ").strip()
                employee = self.search_employee(employee_id)
                if employee:
                    print(f"Employee Found:\n{employee}")
                else:
                    print("Error: Employee not found.")
            elif choice == "4":
                self.update_employee()
            elif choice == "5":
                self.delete_employee()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__=='__main__':
    manager = EmployeeManager()
    manager.run()