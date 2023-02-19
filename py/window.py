import customtkinter
import time
import multiprocessing
import random
import tkinter
import selenium_bot

bot = selenium_bot.bot

def bot_status_changed():

    if bot_is_running.get():

        bot_is_running.set(False)
        button.configure(state="normal")
        label_bot_status.configure(text="Apagado")
        box_bot_status.configure(fg_color="#D32424")
        button_run_bot.configure(fg_color="green", text="ON", hover_color="#77C156")
        price.configure(text="$0.00")
        bot.quit()

    else:
        
        bot_is_running.set(True)
        button.configure(state="disabled")
        label_bot_status.configure(text="Prendido")
        box_bot_status.configure(fg_color="green")
        button_run_bot.configure(fg_color="#D32424", text="OFF", hover_color="brown4")

        bot.run(price)
        
        
        


        

        

    """ button.configure(state="disabled" if bot_is_running.get() else "normal")
    bot_is_running.set(False if bot_is_running.get() else True)
    label.configure(text= "Prendido" if bot_is_running.get() else "Apagado") """


ctk = customtkinter

ctk.set_appearance_mode("dark")



root = ctk.CTk()
root.geometry("1280x720")
root.title("Trading Bot")

bot_is_running = ctk.BooleanVar()



frame = ctk.CTkFrame(master=root, fg_color="#494B4B")
frame.pack(pady=20, padx=60, fill="both", expand=True, side="top")


box_bot_status = ctk.CTkFrame(master=frame, fg_color="#D32424", height=100)
box_bot_status.pack(pady=0, padx=0, fill="x", side="top",)

label_bot_status = ctk.CTkLabel(master=box_bot_status, text="Apagado" , text_color="white", font=("Roboto", 40), corner_radius=20)
label_bot_status.pack(pady=20)


""" body = ctk.CTkFrame(master=frame, fg_color="#494B4B")
body.pack(fill="both", pady=10, expand=True, side="bottom") """


button_run_bot = ctk.CTkButton(master=frame, text="ON", command=bot_status_changed, fg_color="green", border_spacing=0, corner_radius=20, hover_color="#77C156" )
button_run_bot.place(x=980, y=610)

button = ctk.CTkButton(master=frame, state="normal", text="Opciones")
button.place(x=100, y=600)

price = ctk.CTkLabel(master=frame, text="$0.00", font=("Roboto", 40))
price.pack(pady=200)





root.mainloop()

#

