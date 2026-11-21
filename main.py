import funciones
import dataset
baseProd = dataset.connect("sqlite:///datos.db")
tabla_prod=baseProd["Productos"]
baseUsuarios=dataset.connect("sqlite:///datos.db")
tabla_usu=baseUsuarios["Usuarios"]
from colorama import init,Fore,Style
init()
usuarios=[]
productos=["coca", "pan", "leche", "queso"]

#Usuarios
while True:
  ingreso=input("Ingese 'R' para registrarse o 'L' si ya esta registrado \n").upper()
  match ingreso:
    
    #registro de usuario nuevo
    case"R":
     print("====================================\n\n              REGISTRATE\n\n====================================")
     funciones.registro()
    

  #inicio de sesion
    case"L":
     print("====================================\n\n              LOGIN    \n\n====================================")
     funciones.login()
     
    