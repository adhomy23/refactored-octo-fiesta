def add_numbers(x, y):
       return x + y


def main():
       num1 = float(input("Enter 1st number: "))
       num2 = float(input("Enter 2nd number: "))
       print(f"Result: {num1} + {num2} = {add_numbers(num1, num2)}")


if __name__ == "__main__":
       main()