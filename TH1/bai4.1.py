arr = [0]*4
arr[0]=input()
arr[1]=input()
arr[2]=input()
arr[3]=input()
max = arr[0]
min = arr[0]
for i in arr:
    if i > max:
        max=i
    elif i<min:
        min=i

print('So lon nhat la:' + max)
print('So nho nhat la:' +min)
