#pyramid pattern:-
n=int(input())
spaces=n-1
stars=1
for i in range(n):
    for j in range(spaces):
        print(" ",end="")
    for j in range (stars):
        print("*",end=" ")
    print()
    spaces=spaces-1
    stars=stars+1

#right-angle triangle pyramid:-
  n=int(input())
spaces=0
stars=1
for i in range(n):
    for j in range(spaces):
        print(" ",end="")
    for j in range (stars):
        print("*",end=" ")
    print()
    spaces=spaces-1
    stars=stars+2
#squre shape pyramid:-
n=int(input())
for i in range(n):
    for j in range (n):
        print("*",end=" ")
    print()
#printing stars in even numbers and # in odd places:-
n=int(input())
for i in range(n):
    for j in range(i+1):
        if i%2==0:
            print("*",end=" ")
        else:
             print("#",end=" ")
    print()     
#inverted right angle pyramid:-
n=int(input())
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()

#invereted pyramid:-
n = int(input())
spaces = 0
for i in range(n, 0, -1):
   for j in range(spaces):
       print(" ", end = " ")
   spaces += 1
   for j in range(2 * i - 1):
       print("*", end = " ")
   print()
  
#combaining two pyramids:-
n = int(input())
stars = 2 * n - 1
spaces = 0

for i in range(n):
   for j in range(spaces):
       print(" ", end = " ")
   spaces += 1
  
   for j in range(stars):
       print("*", end = " ")
   stars -= 2
   print()
  
stars += 4
spaces -= 2
for i in range(1, n):
   for j in range(spaces):
       print(" ", end = " ")
   spaces -= 1
  
   for j in range(stars):
       print("*", end = " ")
   stars += 2
   print()









