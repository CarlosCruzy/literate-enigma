numbers=[]
def askNumber(number):
    numbers.append(number)
    while  (number != 0):
        number=int(input("Ingrese un numero"))
        numbers.append(number)

number=int(input("Ingrese un numero"))
askNumber(number)
numbers.sort()
numbers.reverse()
for n in  numbers:
    print(n)



