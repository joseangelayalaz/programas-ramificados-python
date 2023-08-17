#Abstraccion: significa que no necesito entedener la forma en que algo opera internamente para poderlo utilizar.
#Ejemplo: Calculadora.
#Descomposiocion: Permite dividir el codigo en componentes que colaboran con un fin comun.
#Ejemplo: Se puede pensar como en mini programas dentro de un programa mayor.

#Defincion de funciones:
'''
def <nombre>(<parametros>):
    <cuerpo>
    return <expresion>
    
'''
#Ejemplo:
def suma(a,b):
    total = a + b
    return total

suma(2,3)

#Las funciones en Python pueden tener valores de tipo keyword y valores por defecto

#Ejemplo
def nombre_completo(nombre, apellido, inverso=False):
    if inverso:
        return f'{apellido} {nombre}'
    else:
        return f'{nombre} {apellido}'
    
nombre_completo('Angel', 'Ayala')
nombre_completo('Angel', 'Ayala', inverso=True)
nombre_completo(apellido='Ayala', nombre='Angel')