#A=int(input())
#B=int(input())
#C=int(input())
#print(min(A,B,C))

#a=int(input())
#b=int(input())
#c=int(input())
#if a+b==c or a+c==b or b+c==a:
#    print('Oh yes sir')
#else: print('Oh no cringe')

a=int(input())
for i in range(1):
    if a > 1000:
        print('Введите меньше чисел')
        break
b=[]
for i in range(a):
    if int(input())>30000:
        print('Введите число поменьше')
        break
    else: b+=[int(input())]
    #elif int(input())%3 == 0:
        #b+=[int(input())]


print(b)

