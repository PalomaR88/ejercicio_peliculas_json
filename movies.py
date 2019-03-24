import json
import webbrowser

with open("movies.json") as fichero:
    doc=json.load(fichero)

#función que devuelve todos los datos de directores
def datos(doc,datos):
    lista=[]
    for i in doc:
        lista.append(i[datos])
    return lista

#función para el ejercicio 3
def ejercicio3(doc, palabra1, palabra2):
    lista=[]
    for i in range(len(datos(doc, "storyline"))):
        if palabra1 in datos(doc, "storyline")[i]:
            if palabra2 in datos(doc, "storyline")[i]:
                lista.append(datos(doc, "title")[i])
    return lista

#función que crea la lista de los actores sin repetir
def lista_actores(dos):
    lista=[]
    for i in datos(doc, "actors"):
        for x in i:
            lista.append(x)
    actores_sin_repetir=lista_sin_repetir(lista)
    return actores_sin_repetir

#función para el ejercicio 4
def ejercicio4(doc, numero):
    lista=[]
    actor=lista_actores(doc)[numero]
    for i in range(len(doc)):
        if actor in doc[i]["actors"]:
            lista.append(doc[i]["title"])
    return lista

#funcion que convalida, introduce el máx y devuelve una nueva opcion
def convalidar(dato, num_max):
    while True:
        numero=int(input("Introduce el número que corresponde %s" %(dato)))
        if numero>num_max:
            print("ERROR. El número debe ser entre 0  y", num_max)
        else:
            break
    return numero

#función que recibe una lista y te la devuelve sin repetir
def lista_sin_repetir(lista_primaria):  
    lista=[]
    for i in range(len(lista_primaria)):
        existe=False
        for x in range(len(lista)):
            if lista_primaria[i]==lista[x]:
                existe=True
        if existe==False:
            lista.append(lista_primaria[i])
    return lista

##función que crea extra los directores
#def directores(doc):
#    lista=[]
#    for i in doc:
#        director=i["director"]["name"]
#        lista.append(director)
#    return lista  
#
##función que devuelve la lista de los direcores sin repetir
#def directores_sin_repetir(doc):
#    todos_dir=directores(doc)
#    filtro_dir=lista_sin_repetir(todos_dir)
#    return filtro_dir
#
##función para elegir peliculas segun director
#def dir_peli(doc,registro, registro2, numero):
#    lista=[]
#    direlegido=directores_sin_repetir(doc)[numero]
#    datosdir=datos(doc,registro)
#    datodirele=eleccion(datosdir,registro2,direlegido)
#    pelicula=eleccion(doc,registro,datodirele[0])
#    return pelicula
#
##función para elegir peliculas segun director
#def act_peli(doc,registro, numero):
#    lista=[]
#    actor=actores_sin_repetir(doc)[numero]
#    listapeliculas=lista_peliculas_actor(doc,actor)
#    return listapeliculas
#
#def lista_peliculas_actor(doc,actor):
#    lista=[]
#    for i in doc:
#        name=i["name"]
#        for x in i["actors"]:
#            if x==actor:
#                lista.append(name)
#    return lista
#
#
##función que recibe un registro y devuleve las películas 
##donde aparecen
#def eleccion(doc,registro,dato):
#    lista=[]
#    for i in doc:
#        #print(i[registro])
#        if i[registro]==dato:
#            lista.append(i)
#    return lista
#
##función que devuelve los actores
#def actores_sin_repetir(doc):
#    listactores=datos(doc,"actors")
#    lista=[]
#    for i in listactores:
#        for x in i:
#            lista.append(x)
#    actores=lista_sin_repetir(lista)
#    return actores
#
#menu principal
while True:
    print('''
1.- Listar título, año y duración de todas las películas
2.- Mostrar los títulos de las películas y el número de actores/actrices
3.- Mostrar las películas que contengan en la sinopsis dos palabras dadas
4.- Mostrar las películas en las que ha trabajado un actor dado
5.- Mostrar título y la url del póster de las tres películas con una media de puntuaciones dadas entre dos fechas dadas
0.- Salir''')
    opcion=input("Opción: ")
    print("")
    if opcion=="1":
        for i in range(len(datos(doc,"title"))):
            print(i, "-", datos(doc,"title")[i])
        print("")
        tecla= input("PRESIONA UNA INTRO PARA CONTINUAR")

    elif opcion=="2":
        for i in range(len(datos(doc, "title"))):
            print("-", datos(doc,"title")[i])
            print("         Actores/actrices: ",len(datos(doc, "actors")[i]))
        print(" ")
        tecla= input("PRESIONA UNA INTRO PARA CONTINUAR")

    elif opcion=="3":
        palabra1=input("Introduce la primera palabra: ")
        palabra2=input("Introduce la segunda palabra: ")
        if len(ejercicio3(doc, palabra1, palabra2))==0:
            print("No hay coincidencias")
        else:
            print("Películas con las palabras", palabra1,"y", palabra2)
            for i in range(len(ejercicio3(doc, palabra1, palabra2))):
                print("     - ", ejercicio3(doc, palabra1, palabra2)[i])
        print(" ")
        tecla= input("PRESIONA UNA INTRO PARA CONTINUAR")

    elif opcion=="4":
        for i in range(len(lista_actores(doc))):
            print(i, "-", lista_actores(doc)[i]) 
        numero=convalidar("al actor o actriz: ", len(lista_actores(doc)))
        print("Las películas donde aparece", lista_actores(doc)[numero], "son:")
        for i in ejercicio4(doc,numero):
            print("    -", i)
        print("")
        tecla= input("PRESIONA UNA INTRO PARA CONTINUAR")

    elif opcion=="5":
        
#        for i in range(len(datos(doc,"name"))):
#            print(i, "-", datos(doc,"name")[i])
#        print("")
#        pel=convalidar("a la película: ", len(datos(doc,"name")))
#        nombrepeli=datos(doc,"name")[pel]
#        nombrelink=nombrepeli.replace(" ","+")
#        link="https://www.imdb.com/find?ref_=nv_sr_fn&q="+nombrelink
#        webbrowser.open(link,1,True)
#        print("")
#        tecla= input("PRESIONA UNA INTRO PARA CONTINUAR")  
#
    elif opcion=="0":
        print("Adios")
        break
    else:
        print("Lo siento, no hay ninguna opción disponible")
        print(" ")


