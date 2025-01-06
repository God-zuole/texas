import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk, ImageDraw, ImageFont

class ImageUtil():
    def __init__(self, root):
        self.root = root
    def image_show(self, image_path, resize, label_name, coordinate):
        image = Image.open(image_path)
        if resize is not None:
            image = image.resize(resize, Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(self.root, image=photo, name = label_name)
        image_label.image = photo
        image_label.place(x=coordinate[0], y=coordinate[1])

    def image_show_flip(self, image_path, resize, label_name, coordinate):
        image = Image.open(image_path)
        if resize is not None:
            image = image.resize(resize, Image.LANCZOS)
        image = image.rotate(180)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(self.root, image=photo, name = label_name)
        image_label.image = photo
        image_label.place(x=coordinate[0], y=coordinate[1])

    def image_show_lower(self, image_path, resize, label_name, coordinate):
        image = Image.open(image_path)
        if resize is not None:
            image = image.resize(resize, Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(self.root, image=photo, name = label_name)
        image_label.image = photo
        image_label.place(x=coordinate[0], y=coordinate[1])
        image_label.lower()