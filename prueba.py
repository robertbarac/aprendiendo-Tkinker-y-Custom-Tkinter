import customtkinter
app = customtkinter.CTk()
# # Ejemplo sin usar clases
boton = customtkinter.CTkButton(app, text="Haz clic", command=funcion_clic)

# Ejemplo con clases
class MiApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.boton = customtkinter.CTkButton(self, text="Haz clic", command=self.funcion_clic)
        self.boton.grid(row=0, column=0, padx=20, pady=10)

    def funcion_clic(self):
        print("¡Botón clickeado!")

mi_app = MiApp()
mi_app.mainloop()


# def button_event():
#     print("button pressed")


# button = customtkinter.CTkButton(app, text="CTkButton", command=button_event)
# button.pack()
app.mainloop()