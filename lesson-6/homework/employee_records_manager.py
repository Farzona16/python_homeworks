import os
my_file='employees.txt'
if not os.path.exists(my_file):
    open(my_file,'w').close()

def add_employee():
    employee_id=input("enter the id of employee: ")
    with open(my_file,'r') as f:
        for line in f:
            if line.startswith(employee_id+','):
                print('this employee id already exists')
                return
    name=input('enter name: ')    
    position=input('enter position: ')
    salary=input('enter salary: ')
    with open(my_file,'a') as f:
        f.write(f"\n{employee_id}, {name}, {position}, {salary}\n")
        print("New employee added successfully!")     
def view_employees():
    with open(my_file, 'r') as f:
        records=f.readlines()
        if not records:
            print("There isn`t any information")
        else:
            for record in records:
                print(record)
def search_employees():
    employee_id=input("enter employee`s id for search: ").strip()
    with open(my_file,'r') as f:
        for line in f:
            if line.strip().startswith(employee_id+','):
               print(line.strip())
               return 
    print("Employee not found whith this id")
def update_employee():
    employee_id=input("enter employee id for update: ")
    with open(my_file, 'r') as f:
        records=f.readlines()
        updated=False
        with open(my_file, 'w') as f:
            for line in records:
                if line.startswith(employee_id+','):
                    print(line.strip())
                    name=input("Enter new name for uptade: ")
                    position=input("enter new position to update: ")
                    salary=input("enter new salary to uptade: ")
                    f.write(f"{employee_id}, {name}, {position}, {salary}\n")
                    updated=True
                else:
                    f.write(line)
        if updated:
            print("updated successfully")
        else:
            print("id not found")   
def delete_employee():
    employee_id=input("enter employee_id to delete: ")
    with open(my_file,'r') as f:
        records=f.readlines()
    deleted=False
    with open(my_file,'w') as f:    
        for line in records:
            if line.startswith(employee_id+','):
                print("employee was succesfully deleted ")
                print(line.strip())
                deleted=True
            else:
                f.write(line)
    if not deleted:
            print("This id not found")  

def main():   
    while True:
        print("""
        1.Add employee
        2.View employees
        3.Search employees
        4.Update employee
        5.Delete employee
        6.Exit program
        """)
        my_choice=input("enter your choise from 1 to 6 : ")
        if my_choice=='1':
            add_employee()
        elif my_choice=='2':
            view_employees()
        elif my_choice=='3':
            search_employees()
        elif my_choice=='4':
            update_employee()
        elif my_choice=='5':
            delete_employee()
        elif my_choice=='6':
            print("Exiting the programm")
            break
        else:
            print("Your choice is not correct. Please try again!")
if __name__=="__main__":
    main()