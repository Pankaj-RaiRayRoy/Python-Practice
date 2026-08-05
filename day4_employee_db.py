employee_data = {}

while True:
    name = input("Enter the name of the employee ('done' to exit): ")
    if name == "done":
        break
    else:
        department = input("Enter the department name: ")
        employee_data[name]= department

    
print(employee_data)
