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
#
##funcion que convalida, introduce el máx y devuelve una nueva opcion
#def convalidar(dato, num_max):
#    while True:
#        numero=int(input("Introduce el número que corresponde %s" %(dato)))
#        if numero>num_max:
#            print("ERROR. El número debe ser entre 0  y", num_max)
#        else:
#            break
#    return numero
#
##función que recibe una lista y te la devuelve sin repetir
#def lista_sin_repetir(lista_primaria):  
#    lista=[]
#    for i in range(len(lista_primaria)):
#        existe=False
#        for x in range(len(lista)):
#            if lista_primaria[i]==lista[x]:
#                existe=True
#        if existe==False:
#            lista.append(lista_primaria[i])
#    return lista
#
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

#    elif opcion=="2":
#        print("Elige una opción:")
#        print(" 0 - Director")
#        print(" 1 - Actor")
#        opcion=convalidar("a la opción: ", 1)
#        if opcion==0:
#            for i in range(len(directores_sin_repetir(doc))):
#                print(i, "-", directores_sin_repetir(doc)[i])
#            dir=convalidar("al director: ", len(directores_sin_repetir(doc)))
#            pelicula=datos(dir_peli(doc,"director","name",dir),"name")
#            print("Películas de",directores_sin_repetir(doc)[dir])
#            for i in pelicula:
#                print("")
#                print(" -",i)
#        else:
#            for i in range(len(actores_sin_repetir(doc))):
#                print(i, "-", actores_sin_repetir(doc)[i])
#            act=convalidar("al actor: ", len(actores_sin_repetir(doc)))
#            print("Peliculas de", actores_sin_repetir(doc)[act])
#            peliculas=act_peli(doc,"actors",act)
#            for i in peliculas:
#                print("")
#                print(" -",i)
#        print(" ")
#        tecla= input("PRESIONA UNA INTRO PARA CONTINUAR")
#
#    elif opcion=="3":
#        for i in range(len(datos(doc,"name"))):
#            print(i, "-", datos(doc,"name")[i])
#        print("")
#        pel=convalidar("a la película: ", len(datos(doc,"name")))
#        anio=eleccion(doc,"name",datos(doc,"name")[pel])[0]["year"]
#        print(datos(doc,"name")[pel],"es de",anio)
#        print(" ")
#        tecla= input("PRESIONA UNA INTRO PARA CONTINUAR")
#
#
#    elif opcion=="4":
#        anio=int(input("Introduce el año: "))
#        #print(eleccion(doc,"year",anio))
#        listapeliculas=eleccion(doc,"year",anio)
#    
#        if len(listapeliculas)==0:
#            print("No se tienen datos de películas en el año",anio)
#        else:
#            for i in listapeliculas:
#                print("")
#                print(" -",i["name"])
#        print("")
#        tecla= input("PRESIONA UNA INTRO PARA CONTINUAR")
#
#
#    elif opcion=="5":
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
#    elif opcion=="0":
#        print("Adios")
#        break
#    else:
#        print("Lo siento, no hay ninguna opción disponible")
#        print(" ")
#
#
#