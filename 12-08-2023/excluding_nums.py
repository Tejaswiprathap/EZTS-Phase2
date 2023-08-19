'''print numbers from 1-100 excluding (10,22,99,97,25,44)'''
a=[10,22,25,44,97,99]
for i in range(1,101):
    if i not in a:
        print(i,end=' ')
