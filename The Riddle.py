#https://www.youtube.com/watch?v=iSNsgj1OCLA&ab_channel=Veritasium
from random import randint as ran
li = []
while len(li)<=99:
    a = ran(0,99)
    if a not in li:
        li.append(a)

sucess = 0
for i in range(99):
    if i not in li:
        print(i)

for i in range(100):
    count = 0
    li2 = [i]
    index = i
    while True:
        count = count+1
        
        
        if i == li[index]:
            
            sucess+=1
            break
        if li[index] in li2:
            for i in range(100):
                index = i
                if index not in li2:
                    break
            
            li2.append(li[index])
        else:
            index = li[index]
        
        
        if count==50:
            break
print(sucess)
    
    
