print("Name:Maitrak Barot")
print("Roll No.:24BEE129")
def isPangram(string):
    a = set('abcdefghijklmnopqrstuvwxyz')
    lstring = set(string.lower())
    
    return a <= lstring
string = input("Enter a string:")
print(isPangram(string))
