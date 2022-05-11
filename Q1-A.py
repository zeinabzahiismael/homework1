# طريقة1
gradstu=['sam','nour','ali','kareem','farah','reem','tala','nouh','jad']
name=input('Enter the student name:')


if name in gradstu:
        print(name,'is graduation')
else:
        print(name, 'isnt graduation')


#طريقة2
gradstu=['sam','nour','ali','kareem','farah','reem','tala','nouh','jad']
name=input('Enter the student name:')
if gradstu.count(name)==0:
    print(name, 'isnt graduation')
else:
    print(name, 'is graduation')













