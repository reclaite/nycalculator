"""
Description:
Custom labels file for the New Year application
with updatable timers etc.

Creation date: 01/11/2022

Author: Aleksandr Gordienko
Version: 0.11A
"""
import abc
import datetime
import customtkinter as ctk

from nycalc import formatter


class UpdatedLabel(ctk.CTkLabel):
    """
    This class allows us to create tkinter label
    with updated information per any time
    """
    app = None
    counter = 0

    def __init__(self, app, **kw):
        super().__init__(app, **kw)
        self.app = app
        self.tk_var = ctk.StringVar()
        self.tk_var.set("0")
        self.config(textvariable=self.tk_var)
        self.updater()

    @abc.abstractmethod
    def updater(self):
        self.counter += 1
        pass


class TimeLabel(UpdatedLabel):
    """
    Label inherited class to show dynamically
    updating time clock
    """
    def __init__(self, app, **kw):
        super().__init__(app, **kw)

    def updater(self):
        local_time = datetime.datetime.now()
        self.tk_var.set(local_time.strftime("%H:%M:%S"))
        self.app.after(1000, self.updater)


class NewYearLabel(UpdatedLabel):
    """
    Label inherited class to count time
    before next New Year celebration
    """
    def __init__(self, app, **kw):
        super().__init__(app, **kw)

    def updater(self):
        now = datetime.datetime.now()
        now_stamp = now.timestamp()
        new_year_stamp = datetime.datetime(now.year + 1, 1, 1).timestamp()

        time_stamp = new_year_stamp - now_stamp + 1
        days = time_stamp // 86400
        time_stamp = time_stamp % (24 * 3600)
        hour = time_stamp // 3600
        time_stamp %= 3600
        min = time_stamp // 60
        time_stamp %= 60

        self.tk_var.set(
            formatter.plurals(int(days), "день", "дня", "дней") + " " +
            formatter.plurals(int(hour), "час", "часа", "часов") + " " +
            formatter.plurals(int(min), "минута", "минуты", "минут") + " " +
            formatter.plurals(int(time_stamp), "секунда", "секунды", "секунд")
        )
        self.app.after(1000, self.updater)
