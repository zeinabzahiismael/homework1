#طريقة1
odd1=[z for z in range (1001) if z%2!=0]
print(odd1)

#طريقة2
odd2=[]
for x in range (1,1001,1):
    if x%2!=0:
        odd2.append(x)
print(odd2)










