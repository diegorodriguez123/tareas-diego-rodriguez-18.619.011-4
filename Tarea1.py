#Esta tarea consiste en crear un programa que pida al usuario a escribir algo. Si escribe "salir" el programa se detiene. Si no, entonces el programa vuelve a pedir que escriba.

while True:
             palabra = str(input("escriba algo:"))
             if palabra == "salir":
                     break
