while True:
    linea = input('> ')
    if linea == 'fin':
        break
    print(linea)
print('Terminado')

y = 8
x = 10

if y > 9:
    print("Mayor a nueve")
else:
    print("No era mayor a nueve :( ")

def imprimelo(parametro):
    print(parametro)
    if x == 0:
        print("tab")