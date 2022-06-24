arr = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]
k = input('So hang=')
if int(k)-1> len(arr):
   print('Khong hop le')
elif int(k)-1<0:
   print('Khong hop le')
else:
   for r in range(len(arr)):
      if int(r)==int(k)-1:
         for c in range(len(arr[r])):

            print(arr[r][c], end=" ")
         print('\n')