#https://www.youtube.com/watch?v=iSNsgj1OCLA&ab_channel=Veritasium
#The Riddle That Seems Impossible Even If You Know The Answer 
#I implemented the riddle and the solution in python and find its accuracy
#The riddle contains a set of numbers from 1-100 arranged randomly for which i used the random module
#The riddle will be explained in the youtube link above 
#I got accuracy of one out of ten trails as the solution promises the best accuracy ever for that problem
#Try it by your self

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
    
    
