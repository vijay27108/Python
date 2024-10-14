# Functions are used to do same calulation multiple times without duplicating the code
#  Notes:
#  Function names should be in lowercase and should not contain spaces between words when creating functions.
 #get the input and so some operation
def add_var(input_var):
   inp=input_var+3
   return inp

# To run the function
print("Enter the number:")
inp1 = input()
inp2=add_var(int(inp1))
print(inp2)
#They're in a 12% tax bracket (in other words, 12% of their salary is taken for taxes, and they only take home 88%), and
#They're paid hourly, at a rate of $15/hour.

def salary(num_of_hours):
   salary=num_of_hours *15
   salary = salary*(1-0.12)
   return salary

print("Salary of the person")
print("Enter the number of hours")
inp=int(input())
print(salary(inp))
#Variables defined inside a function have a local scope of that function only. However, variables defined outside all functions have a global scope and can be accessed anywhere.

print("Enter the number of hours")
num_hours=int(input())
print("Enter the hourly wage")
hourly_wage = int(input())
print("Enter the tax rate")
tax = float(input())
# To pass various variables 
def get_pay(num_hours, hourly_wage, tax):
    output_sal= num_hours*hourly_wage
    output_sal = output_sal * (1-tax)
    return output_sal

# get the num_hours,hourly_wages and tax
print("salary",get_pay(num_hours,hourly_wage,tax))