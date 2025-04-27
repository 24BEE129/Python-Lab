print("Name:Maitrak Barot")
print("Roll no.:24BEE129")
import csv

# Define CSV filename
filename = 'excel_data.csv'

# Sample data to write
header = ['ID', 'Name', 'Department', 'Salary']
data = [
    [1, 'Ravi', 'HR', 50000],
    [2, 'Shyam', 'Engineering', 75000],
    [3, 'Rahul', 'Marketing', 62000],
    [4, 'Dhyana', 'Finance', 67000]
]

with open(filename, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    
    writer.writerow(header)
    
    
    writer.writerows(data)

print(f"CSV file '{filename}' created successfully.")
