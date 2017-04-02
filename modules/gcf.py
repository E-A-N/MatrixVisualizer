def gcf(n1,n2):
    div1 = n1 % 2
    div2 = n2 % 2
    while ((div1 == 0) and (div2 == 0)):
        n1 /= 2
        n2 /= 2
        div1 = n1 % 2
        div2 = n2 % 2

    return n1,n2


print(gcf(98,64))
print(gcf(100,44))
print(gcf(8,99))
print(gcf(64,8))
