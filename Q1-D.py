#طريقة1
d1={x:x**2 for x in range (1,11) if x>0}
print(d1)


#طريقة2
d=dict()
for i in range (1,11):
    d[i]=i**2
print(d)








