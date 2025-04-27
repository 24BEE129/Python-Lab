print("Name:Maitrak Barot")
print("Roll No.:24BEE129")
def poly(a):
   t = (a,a*a,a*a*a)
   return t
b = int(input("Enter a number:"))
for i in range ( 0, b+1):
    print(poly(i))
