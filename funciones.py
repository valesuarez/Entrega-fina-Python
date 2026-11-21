import dataset
import getpass
baseProd = dataset.connect("sqlite:///datos.db")
tabla_prod=baseProd["Productos"]
baseUsuarios=dataset.connect("sqlite:///datos.db")
tabla_usu=baseUsuarios["Usuarios"]
from colorama import init, Fore, Style,Back
init()
usuarios=[]
productos=["coca", "pan", "leche", "queso"]

def registro():
     nombre=input(Fore.CYAN + "Nombre\n" + Style.RESET_ALL).title()
     print("------------------------------------")
     apellido=input(Fore.CYAN + "Apellido\n" + Style.RESET_ALL).title()
     print("------------------------------------")
     usuario= input (Fore.CYAN + "Usuario\n" + Style.RESET_ALL).title()
     print("------------------------------------")
     if tabla_usu.find_one(usuario=usuario) is not None:
         print(Fore.RED + f"El {usuario} ya existe. Elije otro" + Style.RESET_ALL)
         return
     clave= getpass.getpass(Fore.CYAN + "Ingrese una contraseña de 4 numeros\n" + Style.RESET_ALL)
     if clave.isdigit() and len(clave)==4:
           print(Back.GREEN + "Clave aceptada" + Style.RESET_ALL)
     else:
           print(Fore.RED + "Intentelo nuevamente" + Style.RESET_ALL)
           return
     
     registro= input(Fore.CYAN + "ingrese 'SI'para confirmar, 'NO' para cancelar\n" + Style.RESET_ALL).upper()
     if registro=="NO":
      print(Fore.BLACK + Back.RED + "Intentelo mas tarde" + Style.RESET_ALL )
      return
     elif registro == "SI":
     
     
      nuevo_usuario={"nombre":nombre,"apellido":apellido,"usuario":usuario,
                   "clave":clave}
      tabla_usu.insert(nuevo_usuario
                            )
     
         
          
     
     print( Back.GREEN + f"Usuario registrado {usuario}" + Style.RESET_ALL)
     print("Ya puedes logearte")
     
def login():
      usuario_buscado=input(Fore.LIGHTBLUE_EX + "Ingrese su nombre de usuario \n" + Style.RESET_ALL).title()
      print("------------------------------------")
      clave_buscada=getpass.getpass(Fore.LIGHTBLUE_EX + "Ingrese su clave\n " + Style.RESET_ALL)
      print("------------------------------------")
      
      usuario_encontrado=tabla_usu.find_one(
        usuario=usuario_buscado,
        clave=clave_buscada
            )
      if usuario_encontrado:
               print(Fore.BLACK + Back.GREEN + f"Bienvenido {usuario_buscado}, gracias por visitarnos" + Style.RESET_ALL)
               menu()
      elif ["nombre_usuario"]!=usuario_buscado or  ["clave"]!=clave_buscada:
              print(Fore.BLACK + Back.RED + "Usuario o contraseña incorrecta" + Style.RESET_ALL)
      else:
              print(Fore.RED + "No hay usuario registrado" + Style.RESET_ALL)
          
def menu():
     print("====================================\n\n                MENU\n\n====================================")
     while True:
              menu=input(Fore.BLUE + "1. Agregar Productos.\n2. Mostrar Productos.\n3. Buscar Productos\n4. Eliminar Productos.\n5. Salir \n" + Style.RESET_ALL)
              match menu:
              
              #producto nuevo
               
               case "1":
                print("====== AGREGAR PRODUCTOS ======")
                agregar()
               
            
              #mostrar lista de productos
               case"2":
                print("====== LISTA DE PRODUCTOS ======")
                mostrar() 
                
                         
              #busqueda de productos
               case"3":
                print("====== BUSQUEDA ======")
                busqueda()
               
              #Eliminar productos
               case"4":
                 print("====== ELIMINAR ======")
                 eliminar()
                          
              # salida de la sesion
               case"5":
                 salir()
                 break
               case _:
                 print(Fore.RED + Back.BLACK + "Opcion invalida, intente de nuevo" + Style.RESET_ALL )

def agregar():
    producto=input(Fore.LIGHTBLUE_EX + "Ingrese el nombre del producto que desea agregar\n" + Style.RESET_ALL).strip().lower()
    print("------------------------------------")
    if tabla_prod.find_one(nombre=producto):
              print (Fore.RED + f"{producto} ya existe\n")
              return
    
    precio=float(input(Fore.LIGHTBLUE_EX + "Precio:\n" + Style.RESET_ALL))
    print("------------------------------------")
    categoria=input(Fore.LIGHTBLUE_EX + "categoria:\n" + Style.RESET_ALL)
    print("------------------------------------")  
       
    nuevo_producto={"nombre":producto,
                    "precio":precio,
                    "categoria":categoria}
            
    tabla_prod.insert(nuevo_producto)
    print(Fore.BLACK + Back.GREEN + f"El producto {nuevo_producto['nombre']} ha sido agregado de forma exitosa" + Style.RESET_ALL)
    print(Style.RESET_ALL)

def mostrar():
    if len(tabla_prod)==0:
        print (Fore.BLACK + Back.RED + "No hay productos en la base de datos" + Style.RESET_ALL)
    else:
     for nuevo_producto in tabla_prod.all():
      print(Fore.LIGHTBLACK_EX + f"Nombre:{nuevo_producto['nombre']}           Precio:{nuevo_producto['precio']}           Categoria:{nuevo_producto['categoria']}" + Style.RESET_ALL)
      print()


def busqueda():
     busqueda=input(Fore.LIGHTBLACK_EX + "ingrese el nombre del producto que desea buscar\n" + Style.RESET_ALL)
     producto_encontrado=tabla_prod.find_one(nombre=busqueda)            
     if producto_encontrado:
        print(Fore.BLACK + Back.GREEN + "¡Producto encontrado!" + Style.RESET_ALL)
        print(Fore.CYAN + f"Nombre:{producto_encontrado['nombre']}\nPrecio:{producto_encontrado['precio']}\nCategoria:{producto_encontrado['categoria']}" + Style.RESET_ALL)
     else:
        print(Fore.RED + f"lo sentimos, actualmente no tenemos stock de {busqueda}" + Style.RESET_ALL)
        print()
            
def eliminar():
    eliminar_producto=input(Fore.CYAN + "Ingrese el nombre del elemento que quiera eliminar de la lista.\n" + Style.RESET_ALL).lower()
    if tabla_prod.find_one(nombre=eliminar_producto):
      print(Fore.BLACK + Back.GREEN + f"{eliminar_producto}, ha sido eliminado correctamente" + Style.RESET_ALL)
      tabla_prod.delete(nombre=eliminar_producto.lower())
    else:
      print(Fore.BLACK + Back.RED + f"No ha sido posible eliminar {eliminar_producto}, no se encuentra en la base de datos" + Style.RESET_ALL)
      print("\n")

def salir():
     print(Fore.LIGHTMAGENTA_EX + "Gracias por visitarnos. Vuelve pronto" + Style.RESET_ALL)
  