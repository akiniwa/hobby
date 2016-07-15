#! coding: utf-8

import ctypes

file_jpg = 'path/to/image.jpg'

# SPI_SETDESKWALLPAPER <= 20
ctypes.windll.user32.SystemParametersInfoA(20, 0, file_jpg, 0)
