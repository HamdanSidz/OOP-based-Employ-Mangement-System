

class Workers:

    tot_no_of_employees = 0     # class variable

    def __init__(self, name, age, addr):
        self.name = name
        self.age = age        # instance variables
        self.addr = addr
        self.designation = ""
        self.salary = 0.00
        Workers.tot_no_of_employees += 1   # class variable updation

    def get_salary(self):
        return self.salary

    def get_designation(self):
        return self.designation

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def get_addr(self):
        return self.addr

    def set_age(self, age):
        self.age = age

    def set_name(self, name):
        self.name = name

    def set_addr(self, addr):
        self.addr = addr

    def set_salary(self):
        self.salary = float(input("enter salary: "))

    def set_designation(self):
        self.designation = input("enter employee designation: ")


class IT(Workers):

    def __init__(self, no_of_it_emp):
        self.no_of_it_emp = no_of_it_emp
        self.it_total_salary = []
        self.it_total_emp = []

    def add_it_employee(self, workers):
        if len(self.it_total_salary) <= self.no_of_it_emp:
            workers.set_designation()
            workers.set_salary()
            self.it_total_salary.append(workers.salary)
            self.it_total_emp.append(workers)
            return True
        else:
            return False

    def get_it_emp_info(self):
        for i in self.it_total_emp:
            print(i.name, end="    ")
            print(i.age, end="     ")
            print(i.addr, end="          ")
            print(i.salary, end="        ")
            print(i.designation, end=" ")
            print()

    def total_of_salary_of_it(self):
        a = 0.00
        for i in range(len(self.it_total_salary)):
            a += float(self.it_total_salary[i])
        print(f"Total Salary goes to IT department is: {a}")

    def delete_emp(self, worker):
        for i in self.it_total_emp:
            if worker == i:
                self.it_total_emp.remove(i)
                print("Successufully deleted")
            else:
                return "not present"

        for i in self.it_total_salary:
            if i == worker.salary:
                self.it_total_salary.remove(i)
            else:
                print("not present")

    def update_emp_sal(self, worker):
        for i in self.it_total_salary:
            if i == worker.salary:
                self.it_total_salary.remove(i)
                worker.set_salary()
                self.it_total_salary.append(worker.salary)
                print("Successfully Updated")
                break


# enrolled worker in workers class
w1 = Workers("Hamdan", 20, "326/A-WILSON ROAD")
w2 = Workers("Noman", 24, "r-45/khayaban-e-street")

i1 = IT(2)                     # giving max no.of workers to it departmenet
print(i1.add_it_employee(w1))  # additing enrolled workers in it department
print(i1.add_it_employee(w2))
""" 
i1.total_of_salary_of_it()     # total salary goes to it department
i1.get_it_emp_info()         # info about it depart employees 
i1.delete_emp(w1)            # delete it employee
i1.get_it_emp_info()       # chech after deletion of it depart employees
i1.total_of_salary_of_it() # check total salary of it after deletin of 1 employee
 """
print()

print(w2.salary)          # checking individual salary
i1.update_emp_sal(w2)        # updating salary
print(w2.salary)           # checking individual salary after updation
i1.total_of_salary_of_it()   # checking updation at total of salary
print()
i1.get_it_emp_info()        # info printing after updation
