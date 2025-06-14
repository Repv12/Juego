import tkinter
#esta liberia te permite crear ventanas para hacerlo mas grafico
import random
#libreria que me permite randomizar entre opciones

def jugar():
    escoger=["piedra", "papel", "tijera"]
    opciones= entrada.get().lower().strip()
    # en esta variable guardo  lo q escriba el usuario el lower lo uso para q se ponga todo en minuscula y haya menos chance de error escrbiendo y el strip elimina espacios vacios
    if opciones not in escoger:
        resultado.config(text="por favor solo escribe piedra, papel o tijera")
        entrada.set("")
        return
    # el .set("") borra lo que habia escrito el usuario automaticamente
    #el return hace que se repita la funcion o se termine
    # el config permite actualizar un texto
    random_ = random.choice(escoger)
    
    if opciones == random_:
        resultado.config(text="Han quedado empates")
    elif opciones == "piedra" and random =="tijera" or \
        opciones == "tijera" and random == "piedra" or \
        opciones == "papel" and random == " piedra":
        resultado.config(text="ganaste")
    else:
        resultado.config(text="perdiste")
        
        entrada.set("")
                    
        
juego = tkinter.Tk()
#asi creo la ventana


juego.configure(background='black')
juego.title("Piedra,papel o tijeras")
#le asigne nombre a la app 
juego.geometry("400x400")

entrada = tkinter.StringVar(juego)
#esta funcion permite entrar las variables de string y guardarlas y permite actualizar el string si se lo cambia


tkinter.Label(
    juego,
    text="Escribe abajo entre las tres opciones piedra,papel o tijera",
    bg="gray",
    fg="white",
    ).pack(
        fill=tkinter.BOTH,
        expand=False
        )
#este label muestra un texto de lo que tienes q hacer
    
tkinter.Entry(
    bg="gray",
    fg="white",
    justify="center",
    textvariable=entrada
    ).pack( 
      fill=tkinter.BOTH,
      expand=True
      )
        
#el textvariable sirve para hacer la vinculacion del strinvar con la variable del tkinter
# esta entrada de texto te permite escribir lo que elijas

tkinter.Button(
    juego,
    text="Ingresar",
    bg="gray",
    fg="white",
    command=jugar
    ).pack(
      fill=tkinter.BOTH,
      expand=True
      )
 

#este es un widget o almenos asi lo llamo el chico del video q vi jaja son diferentes funciones que se le pueden agregar a la app en este caso button logicamente para agregar un boton
#el .pack permite ingresar o incrustar el boton al codigo osea permite que salga en pantalla
#el fill sirve para expandir el boton con el both se expande en el eje x e y de misma manera  

resultado = tkinter.Label(
    juego,
    text="",
    bg="gray",
    fg="white",
    )
resultado.pack(
        fill=tkinter.BOTH,
        expand=True
        )
        
juego.mainloop()
#este loop permite hacer los cambios que pasan en la ventana a tiempo real o algo asi pero actualiza lo que hace el juego jaja


