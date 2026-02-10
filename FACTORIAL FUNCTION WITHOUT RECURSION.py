# USN 1RUA25BCA0059 NAME MANOJ C
def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

num = int(input("Enter a number: "))
print("Factorial:", factorial(num))

