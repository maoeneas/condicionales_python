#!/usr/bin/env python
'''
Condicionales [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"


def ej1():
    # Ejercicios de práctica numérica

    # Comparadores
    # Ingrese dos números cualesquiera y realice las sigueintes
    # comparaciones entre ellos
    numero_1 = int(input('Ingrese el primer número:\n'))

    numero_2 = int(input('Ingrese el segundo número:\n'))

    # Compare cual de los dos números es mayor
    # Imprima en pantalla según corresponda
    if numero_1 > numero_2:
        print("el munero", numero_1 ,"es mayor que el ", numero_2)
    else:
        print("el munero", numero_2, "es mayor que el ", numero_1)
    # Verifique si el numero_1 positivo, negativo o cero
    # Imprima el resultado en cada caso
    numero_1 = int(input('Ingrese el primer número:\n'))

    if numero_1 > 0:
        print(numero_1, "es positivo")
    elif numero_1 < 0:
        print(numero_1, 'es negativo')
    else:
        print(numero_1, 'y es 0')

    #Verifique si el numero_1 es mayor a 0 y menor a 100
    #Imprima en pantalla si se cumple o no la condición
    numero_1 = int(input('Ingrese un número:\n'))

    if numero_1 > 0 and numero_1 < 100:
        print("el numero que ingreso si cumple la condicion mayor a cero y menor que 100")
    else:
        print("no se cumple la condicion mayor a cero y menor que 100")

    # Verifique si el numero_1 es menor a 10 o el numero_2
    # es mayor a -2
    # Imprima en pantalla si se cumple o no la condición

    numero_1 = int(input('Ingrese un número:\n'))
    numero_2 = int(input('Ingrese un número:\n'))
    if numero_1 < 10 or numero_2 > -2:
        print('ASI ES!!! SE CUMPLE')
    else:
        print('NO NO.... NO SE CUMPLE LA CONDICION')



def ej2():
    # Ejemplos variables de texto

    # Comparadores
    # Ingrese dos palabras cualesquiera y realice las sigueintes
    # comparaciones entre ellas
    texto_1 = str(input('Ingrese la primera palabra:\n'))

    texto_2 = str(input('Ingrese la segunda palabra:\n'))

    # Compare cual de las dos palabras es mayor (alfabéticamente)
    # Imprima en pantalla según corresponda
    
    if texto_1 > texto_2:
        print('{} esta despues alfabeticamente que {}'.format(texto_1, texto_2))
    else:
        print('{} esta antes alfabeticamente que {}'.format(texto_1, texto_2))
    
       
    # Compare cual de las dos palabras tiene mayor
    # cantidad de letras
    # Imprima en pantalla según corresponda
    # Verifique si la primera letra de la primera palabra
    # es mayor a la primera letra de la segunda palabra
    # Imprima en pantalla según corresponda
    texto_1 = str(input('Ingrese la primera palabra:\n'))
    texto_2 = str(input('Ingrese la segunda palabra:\n'))

    pasa_len = len(texto_1)
    pasa_len2 = len(texto_2)

    if texto_1 > texto_2:
        # Este condicional tiene que ser entre pasa_len y pasa_len2, porque nos interesa encuestar la cantidad de letras, no el orden alfabetico.
        # Además tenes el indentado corrido XD
    print(texto_1,"tiene mayor cantidad de letras que",texto_2)
    print("porque tiene:",pasa_len,"caracteres")
    else:
    print(texto_2,"tiene mayor cantidad de letras que",texto_1)
    print("porque tiene:",pasa_len2,"caracteres")
    
    if texto_1[0] > texto_2[0]:
        print('primer letra de texto 1',texto_1,'es mayor a primer letra de', texto_2)
    else:
        print('primer letra de texto2',texto_2, 'es mayor a primer letra de', texto_1)

    copia_texto_1 = texto_1  # Copia de la variable texto_1

    # Verifique que copia_texto_1 es igual a texto_1
    if copia_texto_1 == texto_1:
        print("son iguales las dos variables")        
    
    # Imprima en pantalla según corresponda
    print(copia_texto_1,texto_1)

    # Verifique que copia_texto_1 es distinta a texto_2
    # Imprima en pantalla según corresponda
    if copia_texto_1 == texto_1:
        print("son iguales las dos variables")        
    if copia_texto_1 != texto_2: 
        # Acá tenes de nuevo el tema del indentado, recorda siempre que luego de un " : " tenes que agregar 4 espacios debajo antes de escribir ;D 
    print("nada que ver!!")    

def ej3():
    # Ejercicios de práctica numérica

    # Condicionales anidados
    numero_1 = 7
    numero_2 = -2

    # Verifique si el numero_1 es mayor a 5
    #   --> En caso afirmativo, verifique si el numero_2
    #       es positivo
    #       --> En caso afirmativo imprima en pantalla "Resp=1"
    #       --> En caso negativo imprima en pantalla   "Resp=2"
    numero_1 = 7
    numero_2 = -2

    if numero_1 > 5 and numero_2 > 0:
        print ('resp=1')
    else:
        print('resp2')

    if not numero_1 > 5 and numero_2 > 5:
        # Indentado :D
    print('resp 3')
    else:
        print('resp 4')

    # Verifique la calificación de un estudiante según su
    # puntaje en un examen
    puntaje = 70

    # Si el puntaje es mayor igual a 90 --> imprimir A
    # Si el puntaje es mayor igual a 80 --> imprimir B
    # Si el puntaje es mayor igual a 70 --> imprimir C
    # Si el puntaje es mayor igual a 60 --> imprimir D
    # Si el puntaje es manor a  60      --> imprimir F
    # Debe imprimir en pantalla la calificacion
    # Utilizar "if" anidados

    # no me esta funcionando pero tampoco me da error!!!! me anote para charlarlo ...
    puntaje = 70

    if puntaje >= 90:
        print("A")
        if puntaje >= 80:
            print("B")
            if puntaje >= 70:
                print("C")
                if puntaje >= 60 and puntaje < 69:
                    print("D")
                    if puntaje < 60:
                        print("F")
    # Que pasaría si el puntaje del alumno es 69?
    # Y si fuera 91? no imprimiría 'A', 'B' y 'C'? porque 91 es mayor a 90, a 80 y a 70... entonces? como hacemo XD?
    # para eso tenemos que usar 'elif' que descarta el resto una vez que entra a una condición, así:

    # puntaje = 91

    # if puntaje >= 90:
    #     print('A')
    # elif puntaje >= 80:
    #     print('B')
    # elif puntaje >= 70:
    #     print('C')
    # elif puntaje >= 60 and puntaje <= 69:
    #     print ('D')
    # elif puntaje < 60:
    #     print('F')
    

    

def ej4():
    # Ejemplos variables de texto

    texto_1 = '5'
    texto_2 = '7'

    # Verifique cual cual de los dos textos es mayor alfabéticamente
    # Imprima en pantalla según corresponda
    if texto_1 > texto_2:
        print( texto_1,"es mayor alfabeticamente hablando")
    else:
        print( texto_2,"es mayor alfabeticamente hablando")
    # Transforma esas variables tipo texto y almacénalas
    texto_1= int(texto_1)
    texto_2= int(texto_2)

    # en nuevas variables númericas (int)
    # Repita el proceso, ¿Cuál de las nuevas variables es mayor?
    # Imprima en pantalla según corresponda
    if texto_1 > texto_2:
        print( texto_1,"es mayor alfabeticamente hablando")
    else:
        print( texto_2,"es mayor alfabeticamente hablando")

    # Para pensar!
    # ¿Por qué cree que texto_2 es mayor a texto_1?
    # Siendo números tiene sentido, pero son caracteres, texto,
    # aún así el operador arroja el mismo resultado que con las
    # variables numéricas, cierto? ¿Por qué creen que es así?
    # Esta pregunta estará repetida en el Campus para que puedan
    # responder.
    # NOTA: La respuesta no se encuentra en el apunte, sino en Google ;)

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
