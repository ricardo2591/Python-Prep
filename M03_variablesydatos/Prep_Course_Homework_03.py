#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

# In[7]:
a = 13
print(a)



# 2) Imprimir el tipo de dato de la constante 8.5

# In[3]:
a = 8.5
print(type(a))




# 3) Imprimir el tipo de dato de la variable creada en el punto 1

# In[8]:
a = 13
print(type(a))




# 4) Crear una variable que contenga tu nombre

# In[2]:
nombre = 'ricardo'
print(nombre)



# 5) Crear una variable que contenga un número complejo

# In[3]:
complejo = 2j
print (complejo)




# 6) Mostrar el tipo de dato de la variable crada en el punto 5

# In[4]:
print (type(complejo))




# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# In[1]:
valor_pi = 3.1416


# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

# In[3]:
a = 'True'
b = True




# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8

# In[5]:
print(type(a))
print(type(b))




# 10) Asignar a una variable, la suma de un número entero y otro decimal

# In[1]:
suma = 25 + 3.18




# 11) Realizar una operación de suma de números complejos

# In[2]:
suma_complejos = 3j + 7j
print(suma_complejos)




# 12) Realizar una operación de suma de un número real y otro complejo

# In[4]:
k = suma_complejos + 3
print(k)




# 13) Realizar una operación de multiplicación

# In[5]:
multipli = 3*9
print (multipli)




# 14) Mostrar el resultado de elevar 2 a la octava potencia

# In[6]:
potencia = 2**8
print(potencia)



# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# In[8]:
division = 27/4
print(division)




# 16) De la división anterior solamente mostrar la parte entera

# In[9]:
division_entera = 27//4
print(division_entera)




# 17) De la división de 27 entre 4 mostrar solamente el resto

# In[1]:
division_resto = 27%4
print(division_resto)




# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# In[2]:
operacion = division_entera * 4 + division_resto
print(operacion)




# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# In[3]:
dato1 = 'Hola '
dato2 = 'mundo'
dato_final = dato1 + dato2
print(dato_final)




# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# In[4]:
2 == '2'




# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# In[11]:
l = '2'
print(type(l))
l = int(l)
print(type(l))
2 == l




# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# In[12]:
n = float('3.8')
#porque se pone , en lugar de .




# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.

# In[15]:
g = -5
g -= 2
print(g)




# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# In[29]:
print(1<<2)




# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# In[23]:
int(2) + int('2')

#uno es entero y el otro es string





# 26) Realizar una operación válida entre valores de tipo entero y string

# In[30]:
variable1 = 'este texto se repite '
variable2 = 4
print(variable1 * variable2 + str(variable2) + ' veces')


