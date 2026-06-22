arr = [1,2,45, 66,67,77, 99, 100, 123]
maxnum = arr[0]
for aa in arr:
    if maxnum < aa:
        maxnum = aa
print(maxnum)