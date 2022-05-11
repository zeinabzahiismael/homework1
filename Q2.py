# طرسقة1
binary=[]
num=int(input('Enter the decimal number:'))

while(num!=0):
    z=num%2
    num=num//2
    binary.append(z)
binary.reverse()
for x in range (0,len(binary)):
    print(binary[x],end='')
print('')

# طريقة2
bin=[]
def binaryy(p):
    while (p != 0):
        r = p % 2
        p = p // 2
        bin.append(r)
    bin.reverse()
    for y in range(0, len(bin)):
        print(bin[y], end='')
binaryy(int(input('Enter the decimal number')))
print('')



#طريقة3
num=int(input('Enter the decimal number'))
i=res=0
while num!=0:
    res=res+(num%2)*(10**i)
    num=num//2
    i=i+1
print('the binary number is:',res)




