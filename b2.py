# this imports the ProductionWorker class from the first file
from a1 import ProductionWorker

# this lets the user input their data
product = ProductionWorker(input("Enter your first and last name: "), input("Enter your employee number: "),
                           int(input("What shift do you work?(1 = day 2 = night): ")), input("Enter your hourly rate: "))

def main():
    print("-----------------")
    print("--Employee info--")
    print("Name:", product.get_name())
    print("Employee number:", product.get_number())
    if product.get_shift_number() > 1:
        print("Shift: Night")
    else:
        print("Shift: Day")
    print("Hourly rate:", "$" + product.get_hourly_rate())


main()
