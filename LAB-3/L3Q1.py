user_string=input("enter a string:")
vowel_count=0
vowels='aeiouAEIOU'
for char in user_string:
    if char in vowels:
        vowel_count+=1
print("the number of vowels in the string is:",vowel_count)
