'''
#Lectura de fichero
f = open('mifile.txt')
for linea in f:
    print(linea)
print(f)
'''

'''
#Otra forma de leer un archivo
f = open ('mifile.txt','r')
mensaje = f.read()
print(mensaje)
f.close()
'''

'''
#Agregar texto en un archivo ya creado
f = open('mifile.txt','a')
f.write('\n' + 'Hola Mundo Agregado otra vez')
f.close()
'''

#'''
#Escribir un archivo en python, si ya existe se sobre escribe
f = open('./miOtrofile.txt','w')
for i in range(0, 15):
    f.write('\n'+'Hola Mundo Agregado '+str(i))
f.close()
#'''
