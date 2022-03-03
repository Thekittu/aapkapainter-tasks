from collections import Counter

li=[1,2,3,2,1]
d = Counter(li)

repeated_list = list([num for num in d if d[num]> +1])
print("Duplicate integers: ",repeated_list)