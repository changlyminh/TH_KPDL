arr = [0]*4
arr[0]=input()
arr[1]=input()
arr[2]=input()
arr[3]=input()
count = 0
for i in arr:
    if int (i) > 0:
        count += 1

print('Tong so duong la:' + str(count))