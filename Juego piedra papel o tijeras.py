import tkinter
#esta liberia te permite crear ventanas para hacerlo mas grafico

def procesar():
    escoger = entrada.get().lower()
    if escoger in ("piedra","papel","tijeras"):
        resultado.config(text=f"elegiste: {escoger}")
juego = tkinter.Tk()
#asi creo la ventana

Seleccion = tkinter.StringVar(juego)
entrada = tkinter.StringVar(juego)


#esta funcion permite entrar las variables de string y guardarlas y permite actualizar el string si se lo cambia

juego.configure(background='black')
juego.title("Piedra,papel o tijeras")
#le asigne nombre a la app 
juego.geometry("400x400")

tkinter.Label(
    juego,
    text="Escribe abajo entre las tres opciones piedra,papel o tijeras",
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
    ).pack( 
      fill=tkinter.BOTH,
      expand=True
      )
 
#este es un widget o almenos asi lo llamo el chico del video q vi jaja son diferentes funciones que se le pueden agregar a la app en este caso button logicamente para agregar un boton
#el .pack permite ingresar o incrustar el boton al codigo osea permite que salga en pantalla
#el fill sirve para expandir el boton con el both se expande en el eje x e y de misma manera  
juego.mainloop()
#este loop permite hacer los cambios que pasan en la ventana a tiempo real o algo asi pero actualiza lo que hace el juego jaja


