from calc import Calculator

def perform_calculations():
    calc = Calculator()

    # Perform various operations
    sum_result = calc.add(10, 5)
    diff_result = calc.subtract(10, 5)
    prod_result = calc.multiply(10, 5)
    div_result = calc.divide(10, 0)     # test divide by zero
    pow_result = calc.power(2, 3)
    sqrt_result = calc.square_root(16)

    # Print individual results
    print("Addition Result:", sum_result)
    print("Subtraction Result:", diff_result)
    print("Multiplication Result:", prod_result)
    print("Division Result:", div_result)
    print("Power Result:", pow_result)
    print("Square Root Result:", sqrt_result)

    # Print history
    print("\nCalculation History:")
    for entry in calc.get_history():
        print(entry)

if __name__ == "__main__":
    perform_calculations()
