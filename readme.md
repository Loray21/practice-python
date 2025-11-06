
``` txt
Para poder trabajar sobre estos puntos vamos a escoger un problema cotidiano y empezar a resolverlo cada semana aplicando con cada uno de los puntos anteriores.
Por ejemplo deseo hacer una aplicacion que gestione un conjunto de estudiantes con sus nombres, edades y notas, y que permita calcular automáticamente el promedio individual de cada uno, identificar al estudiante con el mejor y peor rendimiento, listar a los aprobados y desaprobados según su promedio, obtener el promedio global de la clase y determinar quién es el más joven y el más viejo, resolviendo estas operaciones cada semana con distintas herramientas del lenguaje como funciones built-in, list comprehensions, decoradores, generadores, context managers y más, para aprender progresivamente de lo básico a lo avanzado.

```

## Questions
1. What can be the keys of a dictionary in Python?

All the keys of diccionary should hashable.
for example a list o a set not can be keys of dictionary because arme mutable.
python when yo define a dict convert de values of dict in hash so if the key is mutable and the value change, python dont find de key and crash the dictionary.

# La clave es un string → inmutable
d = {"a": [1, 2, 3]}

# Puedo cambiar el valor (la lista)
d["a"].append(4)

print(d)
# Resultado: {'a': [1, 2, 3, 4]}


# Intentar usar una lista como clave
d = {[1, 2, 3]: "valor"}

TypeError: unhashable type: 'list'
