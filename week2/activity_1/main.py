# a basic import
from src.greeter import Calculator
# use an alias - consider why might we do this?

# sometimes we only want to import what we need

# create a calculator class in the module
calculator = Calculator()

# use the new class to return a score to a user

print(calculator.add(10, 20))
print(calculator.multiply(8, 4))
print(calculator.divide(30, 5))
print(calculator.subtract(400, 356))

