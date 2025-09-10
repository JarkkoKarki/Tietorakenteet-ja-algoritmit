def arithmetic(a, b):
    print(f"${a} + ${b} is {a+b}")
    print(f"${a} - ${b} is {a-b}")
    print(f"${a} * ${b} is {a*b}")
    print(f"${a} / ${b} is {a/b}")
    print(f"${a} % ${b} is {a%b}")
    print(f"${a} ^ ${b} is {a**b}")

a = input()
b = input()
arithmetic(a, b)