
s=int(input("vvedite s= "))
p=int(input("vvedite p= "))
for a in range(1,p):
    b=s-a
    if a+b==s and a*b==p:
        print("Первое число= ", a, "Второе число= ",b)
        break

