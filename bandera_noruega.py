from tkinter import *

ventana_principal = Tk()

ventana_principal.title("Bandera de Noruega")

ventana_principal.geometry("1000x727")

ventana_principal.resizable(0,0)

ventana_principal.config(bg = "firebrick4")


frame_blanco1 = Frame(ventana_principal)
frame_blanco1.config(bg = "white", width = 1000, height = 181)
frame_blanco1.place(x=0, y=272)


frame_blanco2 = Frame(ventana_principal)
frame_blanco2.config(bg = "white", width = 181, height = 727)
frame_blanco2.place(x=272, y=0)



frame_azul1 = Frame(ventana_principal)
frame_azul1.config(bg = "midnight blue", width = 90, height = 727)
frame_azul1.place(x=318, y=0)


frame_azul2 = Frame(ventana_principal)
frame_azul2.config(bg = "midnight blue", width = 1000, height = 90)
frame_azul2.place(x=0, y=318)

ventana_principal.mainloop()