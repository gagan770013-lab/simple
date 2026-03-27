def main():
    print("=== Python Exception Handling Program ===")

    # Taking input from user
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
    except ValueError:
        print("Error: Please enter valid numbers only!")
        returnytrezwxdfcgvhnm
        hbrexdcgvhbjm
        buytrxcfgvhbjm,

    # Arithmetic operations
    try:
        print("Addition:", num1 + num2)
        print("Subtraction:", num1 - num2)
        print("Multiplication:", num1 * num2)
        print("Division:", num1 / num2)   # may cause ZeroDivisionError
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")

    # List handling
    try:
        my_list = [10, 20, 30]
        index = int(input("Enter index to access list: "))
        print("Element:", my_list[index])
    except IndexError:
        print("Error: Index out of range!")
    except ValueError:
        print("Error: Invalid index input!")

    # Dictionary handling
    try:
        my_dict = {"name": "Gagan", "age": 20}
        key = input("Enter key to access dictionary: ")
        print("Value:", my_dict[key])
    except KeyError:
        print("Error: Key not found!")

    # File handling
    try:
        file_name = input("Enter file name to open: ")
        file = open(file_name, "r")
        print(file.read())
        file.close()
    except FileNotFoundError:
hxerctyu uyytcrtyvghj 
k jhgtxrf gvbnmhgyvgh bn





        print("Error: File not found!")

    # Type error example
    try:
        result = "Hello" + 5
        print(result)
    except TypeError:
        print("Error: Cannot add string and integer!")

    print("=== Program Finished Successfully ===")


# Run the program
main()
