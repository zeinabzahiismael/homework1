import json
result=0
zi1=[]
user_name=input('Please,enter your name:')
k=open('e:\\zeinab.json','r')
t=json.load(k)
k.close()
for i in t:
    print(i)
    answer=input('Please,enter the  correct answer:')
    zi1.append(answer)
    if answer==t[i]:
        print('Well done,your answer is correct','\n')
        result=result+1
    else:
        print('sorry,your answer is incorrect','\n')
print('user name is:',user_name,'\n')
print('The answers that entered:','\n',zi1,'\n')
print('The result is ','\n',result,'\n')
nam_ans={user_name:zi1}
name_result={'result':result}
user=json.dumps(nam_ans)
user22=json.dumps(name_result)
with open('e:\\user.json','w') as g:
    g.write(user)
    g.write(user22)

