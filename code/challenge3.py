# Challenge 3

from itertools import permutations

data = list('1867')
perms = list( permutations(data) )
perms_int = [ int("".join(p)) for p in perms]
print("Number of permutations:", len(perms))

# find permutations that are divisible by 7
div_7 = []
for i in range(len(perms)):
    print (perms[i], perms_int[i])
    if perms_int[i]%7==0:
        div_7.append(perms_int[i])

if len(div_7)==0:
    print("No permutations are divisible by 7.")
elif len(div_7)==1:
    print(div_7)
    print("Result: {}".format(div_7[0]))
else:
    result = 0.5*( min(div_7) + max(div_7) )
    print("Permutations divisible by 7: {}".format(div_7))
    print("Result: {}".format(result))

# Program output:
# number of permutations:  24
# ['1', '8', '6', '7'] 1867
# ['1', '8', '7', '6'] 1876
# ['1', '6', '8', '7'] 1687
# ['1', '6', '7', '8'] 1678
# ['1', '7', '8', '6'] 1786
# ['1', '7', '6', '8'] 1768
# ['8', '1', '6', '7'] 8167
# ['8', '1', '7', '6'] 8176
# ['8', '6', '1', '7'] 8617
# ['8', '6', '7', '1'] 8671
# ['8', '7', '1', '6'] 8716
# ['8', '7', '6', '1'] 8761
# ['6', '1', '8', '7'] 6187
# ['6', '1', '7', '8'] 6178
# ['6', '8', '1', '7'] 6817
# ['6', '8', '7', '1'] 6871
# ['6', '7', '1', '8'] 6718
# ['6', '7', '8', '1'] 6781
# ['7', '1', '8', '6'] 7186
# ['7', '1', '6', '8'] 7168
# ['7', '8', '1', '6'] 7816
# ['7', '8', '6', '1'] 7861
# ['7', '6', '1', '8'] 7618
# ['7', '6', '8', '1'] 7681
# Permutations divisible by 7: [1876, 1687, 8176, 8617, 7168, 7861]
# Result: 5152.0
