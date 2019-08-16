results=[]

n=int(input("ingrese un numero hasta el cual desea llegar"))
a=int(input("Ingrese un numero por cual desea multiplicar"))

for i in range(0,n + 1):
    results.append(i * a)

for result in results:
    print(result)
