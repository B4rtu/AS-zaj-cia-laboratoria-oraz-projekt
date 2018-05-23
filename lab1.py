import numpy as np
import time
import copy
x = np.arange(5001)
np.random.shuffle(x)
x1 = copy.copy(x)
x2 = copy.copy(x)
x3 = copy.copy(x)
y = np.arange(5001)
first = time.time()
while True:
    warunek = True
    for i in range(5000,0,-1):
        if x1[i-1] > x1[i]:
            buf = x1[i-1]
            x1[i-1] = x1[i]
            x1[i] = buf
    if (x1==y).all():
        break
second = time.time()
print("czas pierwszego sortowania",second-first)
print(x1)
third = time.time()
i=0
while i<len(x2):
    min = x2[i]
    for j in range(i,5001,1):
        if x2[j]<min:
            min= x2[j]
            index = j
    x2[i],x2[index] = x2[index],x2[i]
    if (x2==y).all():
        break
    i=i+1
fourth = time.time()
print("czas drugiego sortowania",fourth-third)
print(x2)
left = 0
right = 4999


def quicksort(left,right,x3):
    while True:
        warunek = True
        pivot = x3[right+1]
        buf = left
        buf2 = right
        pivot_index=right+1
        while (right-left)>1:
            if x3[left]>=pivot:
                if x3[right]<=pivot:
                    temp = x3[right]
                    x3[right] = x3[left]
                    x3[left] = temp
                    right -= 1
                    left += 1
                    warunek = False
                else:
                    right -= 1
                    warunek = False
            else:
                left += 1
        if warunek:
            break
        x3[right],x3[pivot_index]=x3[pivot_index],x3[right]
        pivot_index = right
        quicksort(buf,(pivot_index-2),x3)
        quicksort(pivot_index, buf2, x3)

fifth = time.time()
quicksort(left,right,x3)
sixth = time.time()
print(x3)
print("czas trzeciego sortowania",sixth-fifth)

