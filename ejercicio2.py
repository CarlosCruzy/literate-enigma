letters=[]
def reader(s):
    chain=""
    counter=0
    for value in s:
        if (counter == 0) :
            chain = chain +  value.upper()
            counter = counter + 1
            letters.append(chain)
            continue
        if (value == " "):
            chain = chain + " "
            counter = 0
            letters.append(chain)
            continue
        else:
            chain= chain + value
            counter = counter + 1
    return chain

chain=reader(input("Ingrese una cadena"))
print(letters)