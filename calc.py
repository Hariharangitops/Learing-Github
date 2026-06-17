def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Error"

def calculator():
    while True:
        choice = input("Op (1:+/2:-/3:*/4:/:5:Exit): ")
        if choice == '5': break
        if choice in ('1', '2', '3', '4'):
            n1, n2 = float(input("N1: ")), float(input("N2: "))
            ops = {'1': add, '2': subtract, '3': multiply, '4': divide}
            print("Result:", ops[choice](n1, n2))

if __name__ == "__main__":
    calculator()
