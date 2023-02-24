""" 
nameFile => es solo el nombre del archivo con terminacion .md
content => aca iria el texto tipo string
action keys => "a" (add) , "r" (read) , "w" (write), "..." 
*args & **kwargs => para crear una funcion nueva con nuevos parametros en un array(tupla) o con un objeto(diccionario)
"""
def saveMarkDown(nameFile, content, action):
    with open(f"./md/{nameFile}", action) as archivo:
        archivo.write(content)


#PROBANDO saveMarkDown()
""" texto = "Este es un párrafo de prueba en generado con [`saveMarkDown`](../generateMD.py).\n___\n"
saveMarkDown("saveTest.md",texto,"a") """


#Esto seria un decorador para reutilizar la funcion base (saveMarkDown) con nuevos parametros
def decoSaveMkDw(func):
    def wrapper(nameFile, content, action, *args, **kwargs):
        with open(nameFile, action) as archivo:
            archivo.write(content)
        return func(nameFile, content, action, *args, **kwargs)
    return wrapper

#PROBANDO decorador @decoSaveMkDw
""" @decoSaveMkDw
def haceralgo(nombre , texto , act , nuevoArgumento):
    print(nombre,texto,act,nuevoArgumento)
haceralgo("nombre.md",texto,"w" , "nuevo argumento") """