import tkinter as tk
import time  

def actualizar_hora():
    hora_actual = time.strftime("%H:%M:%S")  
    etiqueta_hora.config(text=hora_actual)
    ventana.after(1000, actualizar_hora)

ventana = tk.Tk()
ventana.title("Digital Clock")

etiqueta_hora = tk.Label(ventana, text="00:00:00", font=("white", 80), bg="white", fg="black")
etiqueta_hora.pack(padx=50, pady=50)

actualizar_hora() 
ventana.mainloop()

