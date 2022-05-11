
import json
user_name=input('Please,enter your name:')
result=0
zi1=[]

with open ('zeinab.json','r') as z:
    zeinab=json.loads(z.read())

for i in zeinab:
    print(i)
    answer=input('Please,enter the  correct answer:')
    zi1.append(answer)

    if answer==zeinab[i]:
        print('Well done,your answer is correct','\n')
        result=result+1
    else:
        print('sorry,your answer is incorrect','\n')


print('user name is:','\n',user_name,'\n')
print('The answers that entered:','\n',zi1,'\n')
if result >= 12:
    print("Bravo,the final result is:",result,'\n')
else:
    print("Good luck,the final result is:",result,'\n')