<<<<<<< HEAD
arr = [12, 5, 30, 20, 25]

largest = second = -1

for i in arr:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i

print("Second largest:", second)
=======
arr = [12, 5, 30, 20, 25]

largest = second = -1

for i in arr:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i

print("Second largest:", second)
>>>>>>> ca7a16a056dda36fc548c068c6b43616efa2f0ab
