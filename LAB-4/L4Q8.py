print("Name: Maitrak Barot")
print("Roll No.: 24BEE129")
def f(n):
    r = 1
    for i in range(1, n + 1):
        r *= i
    return r
n = int(input("Enter a number:"))
print("The factorial is:",f(n))
