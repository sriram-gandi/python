#https://www.youtube.com/watch?v=094y1Z2wpJg&ab_channel=Veritasium
#The Collatz Conjecture is a look simple problem which ends up with a loop 4,2,1 for any number

a = int(input("enter a value"))
li = [a]
while True:
    
    
    if a%2 == 0:
        a = a//2
    else:
        a = a*3+1
    if a in li:
        break
    li.append(a)
print(li)
print("The repeated loop is",li[li.index(a):])
