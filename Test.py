n= int(input("Enter Number: "))
for i in range(n):
    print(" " * (n-i) +  "A" * ((2*i) + 1))

for i in range(n):
    print(" " * (i+1) + "A" * (n-i) + "A" * (n-i-1) + " " * (i+1))
    