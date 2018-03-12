
# coding: utf-8

# In[2]:


year = int(input())
def judge_year (year) :
    if year > 9999:
        print('Error')
    else:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            print('This is a leap year')
        else:
            print('This isn\'t a leap year')
judge_year(year)


# In[5]:


a = int(input('输入：'))
b = []
c = 0
def factor (a):
    for i in range (2,a + 1):
        if a % i == 0:
            if i == a:
                b.append(int(a))
                return
            b.append(i)
            c = int(a / i)
            break
        else:
            continue
    factor(c)
factor(a)
print(str(a) + ' ' + '=',end = ' ')
for i in range(0,len(b)):
    if i == len(b) - 1:
        print(' ' + str(b[i]))
    else:
        print(' ' + str(b[i]) + ' ' + '*',end = '')


# In[1]:


x = int(input('x = '))
if x < 0:
    print('y = ' + str(0))
elif  0 <= x < 5:
    print('y = ' + str(x))
elif 5 <= x <10:
    print('y = ' + str(3 * x - 5))
elif 10 <= x < 20:
    print('y = ' + str(0.5 * x - 2))
else:
    print('y = ' + str(0))

