"""
Description:
Module to load custom fonts
into the Windows system

Creation date: 01/11/2022

Author: Aleksandr Gordienko
Version: 0.11A
"""
import pathlib
from ctypes import windll, byref, create_unicode_buffer, create_string_buffer

FR_PRIVATE = 0x10
FR_NOT_ENUM = 0x20


def load_font(fontpath, default_font, private=True, enumerable=False):
    """
    Makes fonts located in file `fontpath` available to the font system.

    `private`     if True, other processes cannot see this font, and this
                  font will be unloaded when the process dies
    `enumerable`  if True, this font will appear when enumerating fonts

    See https://msdn.microsoft.com/en-us/library/dd183327(VS.85).aspx
    """
    if str(fontpath):
        path_buffer = create_unicode_buffer(fontpath)
        AddFontResourceEx = windll.gdi32.AddFontResourceExW
    elif bytes(fontpath):
        path_buffer = create_string_buffer(fontpath)
        AddFontResourceEx = windll.gdi32.AddFontResourceExA
    else:
        raise TypeError('fontpath must be of type str or unicode')

    flags = (FR_PRIVATE if private else 0) | (FR_NOT_ENUM if not enumerable else 0)
    fonts_added = AddFontResourceEx(byref(path_buffer), flags, 0)
    return pathlib.Path(fontpath).stem if fonts_added > 0 else default_font
