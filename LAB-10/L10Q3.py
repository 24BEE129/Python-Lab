print("Name:Maitrak Barot")
print("Roll no.:24BEE129")
def create_vcard():
    
    name = input("Enter Full Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    
    vcard = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL;TYPE=CELL:{phone}
EMAIL;TYPE=INTERNET:{email}
ADR;TYPE=HOME:;;{address}
END:VCARD
"""

    
    filename = name.replace(" ", "_") + ".vcf"
    with open(filename, "w") as f:
        f.write(vcard)

    print(f"\n vCard saved as '{filename}' - You can now share it or open it on your phone.")


create_vcard()
print("Name:Maitrak Barot")
print("Roll no.:24BEE129")
