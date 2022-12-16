"""
Description:
Main file to launch New Year application
developed using CustomTKinter by Tom Schimansky

Purpose:
Initialize the New Year application window
and start all main working processes in program

Creation date: 01/11/2022

Author: Aleksandr Gordienko
Version: 0.11A
"""

import customtkinter

from module import fontloader
from module.label import *


class NewYearApplication(customtkinter.CTk):
    """
    Fields of the application, there is main parameters
    such as width and height of the application
    and its default font (can be loaded with a prepare_application(self)
    """
    app_width = 1200
    app_height = 600
    font = "Monocraft"

    def __init__(self, width, height, *args, **kwargs):
        """
        Main application class

        @param width - width of the application
        @param height - height of the application
        """
        super().__init__(*args, **kwargs)
        self.app_width = width
        self.app_height = height
        self.geometry(f"{width}x{height}")

    def prepare_application(self):
        """
        Preparation function for application
        which loads fonts and sets main parameters
        """
        self.set_appearance_mode("System")
        # Set title and block resize
        self.title("New Year Calculator")
        self.resizable(False, False)
        # Load font from external file
        self.font = fontloader.load_font("assets/Monocraft.otf", self.font)

    def create_widgets(self):
        """
        Function to create necessary widgets
        and put them to main application window
        """
        # Main frame with New Year info
        frame = ctk.CTkFrame(
            self,
            corner_radius=20
        )
        frame.pack(
            expand=True,
            ipadx=50,
            pady=30,
        )

        # Label informing about the purpose
        # of the application
        label = ctk.CTkLabel(
            frame,
            text='До Нового года осталось',
            text_font=(self.font, 32)
        )
        label.pack(
            side=ctk.TOP,
            ipadx=10, ipady=10,
            padx=10, pady=10
        )

        # Label with automatically updating
        # time before the celebration
        time_frame = ctk.CTkFrame(
            frame,
            fg_color="#349eeb",
            width=600,
            height=150
        )
        time_frame.pack(
            ipadx=10, ipady=10,
            padx=10, pady=10
        )
        new_year_label = NewYearLabel(
            time_frame,
            wraplength=600,
            text_font=(self.font, 28)
        )
        new_year_label.place(
            relx=.5, rely=.5,
            anchor=ctk.CENTER
        )

        # Realtime from the device
        system_time_label = ctk.CTkLabel(
            frame,
            text="Текущее время:",
            text_font=(self.font, 24)
        )
        system_time_label.pack(
            padx=10
        )
        time_label = TimeLabel(
            frame,
            text_font=(self.font, 32)
        )
        time_label.pack(
            ipadx=10, ipady=10,
            padx=10, pady=10
        )

    def run(self, **kwargs):
        """
        Function to run the application
        """
        self.mainloop(**kwargs)


def main():
    """
    This is the main function which
    creates the instance of the New Year application
    and starts it after all preparations
    """
    application = NewYearApplication(1200, 600)
    application.prepare_application()
    application.create_widgets()
    application.run()


if __name__ == '__main__':
    main()
