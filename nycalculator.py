import customtkinter

import fontloader
from label import *

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

fontloader.load_font("Monocraft.otf")

"""
Main parameters of application
"""
app_width = 1200
app_height = 600
font = "Monocraft"

app = ctk.CTk()
app.title("New Year Calculator")
app.resizable(False, False)
app.geometry(f"{app_width}x{app_height}")

"""
This frame is used to center the main elements
of the application and create amazing round border
"""
frame = ctk.CTkFrame(
    app,
    corner_radius=20
)
frame.pack(
    expand=True,
    ipadx=50,
    pady=30,
)

"""
Creating a label informing us about the purpose
of this application
"""
label = ctk.CTkLabel(
    frame,
    text='До Нового года осталось',
    text_font=(font, 32)
)
label.pack(
    side=ctk.TOP,
    ipadx=10, ipady=10,
    padx=10, pady=10
)

"""
A New Year label with automatically updating
time before the celebration
"""
new_year_label = NewYearLabel(
    frame,
    fg_color='#349eeb',
    wraplength=app_width // 1.5,
    corner_radius=20,
    width=250,
    height=100,
    text_font=(font, 36)
)
new_year_label.pack(
    ipadx=10, ipady=10,
    padx=10, pady=10
)

"""
A current time label from pc
"""
time_label = TimeLabel(
    frame,
    text_font=(font, 32)
)
time_label.pack(
    ipadx=10, ipady=10,
    padx=10, pady=10
)

"""
Starting the application
"""
app.mainloop()
