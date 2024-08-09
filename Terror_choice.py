import random
# i = 0 Para hacer seguimiento del nivel alcanzado por el usuario
next_level = 'Y' #Indicador que permite al usuario avanzar de nivel
while next_level == 'Y':
    A = random.randint(1,99) #Numero random entre 1 y 99
    B = random.randint(1,99)
    C = A + B
    D = random.randint(1,2) 
    '''D es una variable que decide mostrar el resultado correcto 
    o incorrecto al usuario. Si D=1, el resultado es correcto 
    y A + B = C. Si D=2, el resultado es incorrecto y A + B = C + random_number. ''' 
    if D == 1:
        Test = 'Si' #El resultado es correcto y el usuario debe decir que Si
        print(f"Escribe 'Si' o 'No' si la suma de {A} + {B} es {C}\n")
        Answer = input()
        if Answer == Test: #El usuario acertó
            print(f"Correcto, pasas al siguiente nivel\n")
        else: #El usuario se equivocó
            print(f"Incorrecto, la criatura está frente a ti...\n")
            next_level = 'N'
    else:
        Test = 'No' #El resultado es incorrecto y el usuario debe decir que No
        C += random.randint(1,9) #C cambia su valor por un numero random entre 1 y 9
        print(f"Escribe 'Si' o 'No' si la suma de {A} + {B} es {C}\n")
        Answer = input()
        if Answer == Test: #El usuario acertó
            print(f"Correcto, pasas al siguiente nivel\n")
        else: #El usuario se equivocó
            print(f"Incorrecto, la criatura está frente a ti....\n")
            next_level = 'N'
                       