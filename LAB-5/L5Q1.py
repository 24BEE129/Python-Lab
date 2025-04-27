print("Name:Maitrak Barot")
print("Roll No.: 24BEE129")
import random

odd_list = [random.randint(1,99)for _ in range(5) if random.randint(1,99) %2!= 0]
even_list = [random.randint(2,100)for _ in range(4) if random.randint(2,100) %2 == 0]

print("odd list:",odd_list)
print("Even List:", even_list)

odd_list[2] = even_list
print("After replacing 3rd element:",odd_list)

flattened_list = [num for sublist in odd_list for num in (sublist if isinstance(sublist,list) else[sublist])]
sorted_list = sorted(flattened_list)

print("Flattened and sorted list:",sorted_list)
