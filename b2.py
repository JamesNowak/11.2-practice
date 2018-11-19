# this imports the ProductionWorker class from the first file
from a1 import ProductionWorker

# this lets the user input their data
product = ProductionWorker(input("Enter your first and last name: "), input("Enter your employee number: "),
                           input("What shift do you work?(1 = day 2 = night): "), input("Enter your hourly rate: "))


def main():
    print()
    print("Name:", product.get_name())
    print("Employee number:", product.get_number())
    print("Shift number:", product.get_shift_number())
    print("Hourly rate:", "$" + product.get_hourly_rate())


main()
