import random

letra_mayuscula = False
letra_minuscula = False
tiene_numero = False
caracter_especial = False
listo = False

while not listo:
    cantidad_agregada = 0
    password = ""

    while( cantidad_agregada < 8 ):
        numero = random.randint(33,125)
        password  += chr(numero)
        cantidad_agregada += 1

        if 65 <= numero <= 90 and not letra_mayuscula:

            letra_mayuscula=True

        elif 97 <= numero <= 122 and not letra_minuscula:

            letra_minuscula = True

        elif 48 <= numero <= 57 and not tiene_numero:

            tiene_numero = True

        elif (33 <= numero <= 47 or 58 <= numero <= 64 or 91 <= numero <= 96 or 123 <= numero <= 125) and not caracter_especial:

            caracter_especial = True
    
    if letra_mayuscula and letra_minuscula and tiene_numero and caracter_especial:
        
        listo=True
    else:
        letra_mayuscula = False
        letra_minuscula = False
        tiene_numero = False
        caracter_especial = False
            



print(password)