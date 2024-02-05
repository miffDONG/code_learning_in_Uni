def bubble_sort(arr):
    sorted = True
    length = len(arr)
    cycle = 1
    for i in range(length-cycle):
      if arr[i] > arr[i+1]:
        arr[i] , arr[i+1] = arr[i+1] , arr[i]
        sorted = False  
    cycle += 1

    while sorted == False:
      sorted = True
      for i in range(length-cycle):
        if arr[i] > arr[i+1]:
          arr[i] , arr[i+1] = arr[i+1] , arr[i]
          sorted = False
      cycle+=1

    return arr


n = int(input())

m = list(map(int,input().split()))

bubble_sort(m)


for i in m:
  print(i,end=" ")