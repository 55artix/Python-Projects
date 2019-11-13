#a

class Complex:
#==========================================
# Purpose: Initializes the class complex. 
# Input Parameter(s): self-provides a reference to the class instance.
#real-The real number
#imag-The imaginary number
# Return Value(s): none
#==========================================
    def __init__(self,real=0.0,imag=0.0):
        self.real=real
        self.imag=imag
#==========================================
# Purpose: Overloads a string method to return the number in the format <real>+<imag>i
# Input Parameter(s): self-provides a reference to the class instance.
# Return Value(s): returns a string in the format of <real>+<imag>i
#==========================================
    def __str__(self):
        return str(self.real)+' + '+str(self.imag)+'i'
#==========================================
# Purpose: Overloads the + operator to take in a Complex object other,
#and returns a new Complex object representing the sum of the complex numbers.  
# Input Parameter(s): self-provides a reference to the class instance.
#other-Complex object
# Return Value(s): returns the sum of the complex numbers.  
#==========================================
    def __add__(self,other):
        total_real=self.real+other.real
        total_imag=self.imag+other.imag
        return Complex(total_real,total_imag)
#==========================================
# Purpose: Overloads the * operator to take in a Complex object other,
#and returns a new Complex object representing the product of the complex numbers.  
# Input Parameter(s): self-provides a reference to the class instance.
#other-Complex object
# Return Value(s): returns the product of the complex numbers.  
#==========================================
    def __mul__(self,other):
        total_real1=self.real*other.real
        total_real2=self.imag*other.imag
        total_imag1=self.real*other.imag
        total_imag2=self.imag*other.real
        return Complex(total_real1-total_real2,total_imag1+total_imag2)
#==========================================
# Purpose: Writes a get_real method to return the real number.
#input parameters(s)-self-provides a reference to the class instance.  
# Return Value(s): returns the real number.
#==========================================
    def get_real(self):
        return self.real
#==========================================
# Purpose: Writes a get_imag method to return the imaginary number.
#input parameters(s)-self-provides a reference to the class instance.  
# Return Value(s): returns the imaginary number.
#==========================================
    def get_imag(self):
        return self.imag
#==========================================
# Purpose: Writes a set_real method to set the real number.
#input parameters(s)-self-provides a reference to the class instance.
#new_real-the real number you are setting.  
# Return Value(s): returns the new set real number.
#==========================================
    def set_real(self,new_real):
        self.real=new_real
#==========================================
# Purpose: Writes a set_imag method to set the imaginary number.
#input parameters(s)-self-provides a reference to the class instance.
#new_imag-the imaginary number you are setting.  
# Return Value(s): returns the new set imaginary number.
#==========================================
    def set_imag(self,new_imag):
        self.imag=new_imag
#==========================================
# Purpose: Overloads the = operator to take in a Complex object other,
#and the corresponding boolean value based on whether the numbers equal one another.  
# Input Parameter(s): self-provides a reference to the class instance.
#other-Complex object
# Return Value(s): returns the boolean True or False based on whether or not the numbers equal one another.  
#==========================================
    def __eq__(self,other):
        if self.real==other.real and self.imag==other.imag:
            return True
        else:
            return False
#x = Complex(2.7,3)
#y = Complex(-4,0)
#z = Complex(0,-1.5)
#print(x.real) # 2.7
#print(x.get_real()) # 2.7
#print(y.get_imag()) # 0
#x.set_real(6)
#z.set_imag(-2.5)
#print(x.real) # 6
#print(x) # 6 + 3i
#print(y) # -4 + 0i
#print(z) # 0 + -2.5i
#print(x+y) # 2 + 3i
#print(z+y+x) # 2 + 0.5i
#print(y*z) # 0.0 + 10.0i
#print(x*z) # 7.5 + -15.0i
#print(x*y+x*z) # -16.5 + -27.0i
#print(x*(y+z)) # -16.5 + -27.0i
#print(x == y) # False
#print(x*y+x*z == x*(y+z)) # True


#b
class Employee:
#==========================================
# Purpose: Initilizes the five instances(name,position, salary, seniority, and value) in the class Employee
# Input Parameter(s): self-provides a reference to the class instance.
#other-The string argument for the class Employee.
# Return Value(s): None 
#==========================================
    def __init__(self,other=''):
        word_list=other.split(',')
        self.name=word_list[0]
        self.position=word_list[1]
        self.salary=float(word_list[2])
        self.seniority=float(word_list[3])
        self.value=float(word_list[4].split('\n')[0])
#==========================================
# Purpose: Overloads the string method to return a string in the format "<Name>, <Position>"
#input parameters(s)-self-provides a reference to the class instance.  
# Return Value(s): returns a string in the format "<Name>, <Position>"
#==========================================
    def __str__(self):
        return str(self.name)+', '+str(self.position)
#==========================================
# Purpose: Write method net_value to return the employee's value minus their salary.  
#input parameters(s)-self-provides a reference to the class instance.  
# Return Value(s): returns the employee's value minus their salary.  
#==========================================
    def net_value(self):
        return self.value-self.salary
#==========================================
# Purpose: Overload the < operator so it takes in another Employee object and returns True or False based on whether or not
#the left operand has a lower value than the right operand.  
# Input Parameter(s): self-provides a reference to the class instance.
#other-An Employee object
# Return Value(s):True or False based on whether or not
#the left operand has a lower value than the right operand.   
#==========================================
    def __lt__(self,other):
        if self.net_value()<other.net_value():
            return True
        else:
            return False
#emp1 = Employee('Milton,Underling,310423.01,5.0,22.99\n')
#emp2 = Employee('Bill,Boss,403567.34,5.0,519.35\n')
#print(emp1.name)
#print(emp1.position)
#print(emp1.salary)
#print(emp1.seniority)
#print(emp1.value)
#print(emp1)
#print(emp1.net_value())
#print(emp2.net_value())
#print(emp1 < emp2)
#print(emp2 < emp1)
#Milton
# Underling
# 310423.01
# 5.0
# 22.99
# Milton, Underling # -310400.02
# -403047.99
# False
# True        
class Branch:
#==========================================
# Purpose: Initilizes the three instances(location,upkeep, and team) in the class Branch.  
# Input Parameter(s): self-provides a reference to the class instance.
#fname-the name of the CSV file as a string
# Return Value(s): returns -1 if the file is invalid, or a -2 if the file is empty.  
#==========================================
    def __init__(self,fname=''):
        try:
            f=open(fname)
        except:
            print(fname,' invalid file')
            return -1
        try:
            list_lines=f.readlines()
        except:
            print('empty file')
            return -2
        word_list=list_lines[0].split(',')
        self.location=word_list[1]
        word_list2=list_lines[1].split(',')
        self.upkeep=float(word_list2[1])
        self.team=list_lines[3:]
#==========================================
# Purpose: Overloads the string method to return a string containing the location of the branch, followed by the string
# representation of each employee separated by newlines.  
#input parameters(s)-self-provides a reference to the class instance.  
# Return Value(s): returns a string containing the location of the branch, followed by the string
# representation of each employee separated by newlines.  
#==========================================
    def __str__(self):
        string=str(self.location)+'\n'
        for item in self.team:
            list_word=item.split(',')
            string+=str(list_word[0])+', '+str(list_word[1])+'\n'
        return string
#==========================================
# Purpose: Write method profit to return the sum of the net values of all the emplyees in the branch, minus
# the upkeep of the barnch.  
#input parameters(s)-self-provides a reference to the class instance.  
# Return Value(s): returns the sum of the net values of all the emplyees in the branch, minus
# the upkeep of the barnch.  
#==========================================
    def profit(self):
        total_profit= -self.upkeep
        for item in self.team:
            E=Employee(item)
            total_profit+=E.net_value()
        return total_profit
#==========================================
# Purpose: Overload the < operator so it takes in another Branch object and returns True or False based on whether or not
#the left operand has a lower value than the right operand.  
# Input Parameter(s): self-provides a reference to the class instance.
#other-An Branch object
# Return Value(s):True or False based on whether or not
#the left operand has a lower value than the right operand.   
#==========================================
    def __lt__(self,other):
        if self.profit()<other.profit():
            return True
        else:
            return False
#==========================================
# Purpose: Takes in one argument: num is an integer representing the number of employees that must be cut from the branch, and cut sorts the
#employees by their net value, and removes the lowest num Employees from the team list.  
# Input Parameter(s): self-provides a reference to the class instance.
#num-num is an integer representing the number of employees that must be cut from the branch
# Return Value(s):cut sorts employees by their net value, and removes the lowest num Employees from the team list.  
#==========================================
    def cut(self,num):
        employee_list=[]
        for item in self.team:
            E=Employee(item)
            employee_list.append(E)
            
        sorted_employees=sorted(employee_list)
        for i in range(num):
            sorted_employees.pop(0)
        kept_employees=[]
        for item in sorted_employees:
            index=employee_list.index(item)
            kept_employees.append(self.team[index])
        self.team=kept_employees
        
#branch2 = Branch('branch2.csv')
#print(branch2.location)
#print(branch2.upkeep)
#print()
#Pawnee #98229.98
#print(branch2)
#### Pawnee
#### Ron, Efficiency Logistics Strategist
#### Leslie, Creative Evolution Strategist
#### Ann, Data Evolution Engineer
#### Mark, Operational Services Specialist
#### Tom, Creative Logistics Coordinator
#### April, Enterprise Services Consultant
#### Andy, Creative Logistics Specialist
#### Jerry,
#### Donna, ##
#print()
#Enterprise Services Technician Operational Innovation Engineer
#branch2.cut(7)
#print(branch2)
#### Pawnee
#### Leslie, Creative Evolution Strategist
#### Ann, Data Evolution Engineer ##
#print()
#print(branch2.profit())
#branch1 = Branch('branch1.csv')
#print(branch1.upkeep)
##
#print()
#print(branch1)
#### Scranton
#### Dwight, Efficiency Evolution Specialist
#### Jim, Data Innovation Specialist
#### Pam, Operational Analytics Technician
#### Ryan, Data Evolution Consultant
#### Stanley, Efficiency Logistics Technician
#### Michael, Enterprise Communications Technician
#### Kevin, Operational Services Technician
#### Meredith, Data Evolution Technician
#### Angela, Enterprise Communications Consultant
#### Oscar, Creative Innovation Coordinator
#### Phyllis, Enterprise Analytics Technician
#branch1.cut(8)
##
#print()
#print(branch1)
#### Scranton
#### Pam, Operational Analytics Technician
#### Michael, Enterprise Communications Technician
#### Stanley, Efficiency Logistics Technician   
class Company:
#==========================================
# Purpose: Initilizes the two instances(name and branches) in the class Company.  
# Input Parameter(s): self-provides a reference to the class instance.
#company_name-the string representing the name of the company
#branch_list-list of the branches
# Return Value(s): None
#==========================================
    def __init__(self,company_name='',branch_list=[]):
        self.name=company_name
        self.branches=branch_list
#==========================================
# Purpose: Overloads the string method so that it returns the company name,
#followed by the string representation of each branch(in no particular order) separated
#by two newlines.  
# Input Parameter(s): self-provides a reference to the class instance.
# Return Value(s): returns the company name,
#followed by the string representation of each branch(in no particular order) separated
#==========================================
    def __str__(self):
        string=str(self.name)+'\n'
        for item in self.branches:
           string+=str(item)+'\n'
        return string
#==========================================
# Purpose: Implements the HR policy to find the branhc with the lowest profit margin and cut hald of the employees from that branch.   
# Input Parameter(s): self-provides a reference to the class instance.
# Return Value(s): none
#==========================================
    def synergize(self):
        sorted_branches=sorted(self.branches)
        low_branch=sorted_branches[0]
        index=self.branches.index(low_branch)
        cut_branch=self.branches[index]
        Num_ppl_cut=len(cut_branch.team)//2
        cut_branch.cut(Num_ppl_cut)
       
#b1 = Branch('branch1.csv')
#b2 = Branch('branch2.csv')
#b3 = Branch('branch3.csv')
#b4 = Branch('branch4.csv')
#hs = Company('Synergistic Management Solutions',[b1,b2,b3,b4])
#print(hs.name)
#print()
#print(hs) ####
####
####
#Synergistic Management Solutions

#print()
#hs.synergize()
#print()
#print(hs)       
#        
