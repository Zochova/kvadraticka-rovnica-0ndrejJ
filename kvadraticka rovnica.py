a=int(input("Zadajte číslo a: "))
b=int(input("Zadajte číslo b: "))
c=int(input("Zadajte číslo c: "))

D=(b*b)-((4*a)*c)

x1=(-b+(D**(1/2)))/(2*a)
x2=(-b-(D**(1/2)))/(2*a)

print("x1=",x1, "x2=",x2)
