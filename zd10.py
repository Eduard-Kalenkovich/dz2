kolichestvo=int(input("ВВедите число монет="))
vverh=0
vniz=0
for i in range(kolichestvo):
    moneta=int(input("введите монетка вверх=1 или вниз=0"))
    if moneta:
        vverh+=1
    else:
        vniz+=1
if vverh<vniz:
    print("Нужно перевернуть",vverh," монет" ) 
else:
    print("Нужно перевернуть",vniz," монет" )               

