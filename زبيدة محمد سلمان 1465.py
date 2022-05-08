#!/usr/bin/env python
# coding: utf-8

# # السؤال الأول

# # A الطلب

# In[2]:


grad_s=['zubaida','yara','haneen','amjad','karam','sam']
#loop for accept more one name
while True:
    #input name
    s_name=input('input a student name:')
    #testing if student name in list
    if s_name in grad_s:
        print("{} graduated...>> congration!!!".format(s_name))
    else:
        print("bad luck...>> {} is not graduated".format(s_name))
    q=input("do you want to continue, if yes enter y ")
    #countinue or not
    if q!='y':
        break


# # B الطلب

# In[ ]:


odds=[x for x in range(1,1000) if x%2!=0]
print(odds)


# # C الطلب

# In[5]:


l=['Network','Math','Programming','Physics','Music']
for i in l:
    if i.startswith('P'):
        print(i,end="\t")


# # D الطلب

# In[6]:


#the dictionary is about numbers and square of numbers
d={x:x**2 for x in range(1,11)}
print(d)


# # السؤال الثاني

# In[4]:



temp=list()
while True:
    num=int(input('enter decimal number: '))
    while True:    
        temp.append(str(num%2))
        num//=2
        if num==0:
            break
    #to setting the true stutue
    temp.reverse()
    #convert list to string
    result=''.join(temp)
    print('result is ', result)
    temp.clear()
    q=input("do you want to continue, if yes enter y ")
    #countinue or not
    if q!='y':
        break


# # السؤال الثالث

# In[14]:


def readfunc():
    #this function to read lines from file and delete the \n at end of line and retuen a list contains lines
    filename="أسئلة وأجوبة.txt"
    infile=open(filename,'r')
    q=[line.rstrip() for line in infile]
    infile.close()
    return q
a=readfunc()
numques=len(a)
trueanswer=0
#make each question and answer in list
for i in a:
    q=i.split('?')
    print(q[0])
    s=input("answer the questions")
    #test
    if s==q[-1]:
        print('true')
        trueanswer+=1
    else:
        print('flase')
#take username
name=input('enter your name: ')
print('you are asnwered on {} true from {}'.format(trueanswer,numques))
#make file
outfile=open('resutls.txt','w')
outfile.writelines(name)
outfile.writelines(' you are asnwered on {} true from {}'.format(trueanswer,numques))
outfile.close()


# In[ ]:




