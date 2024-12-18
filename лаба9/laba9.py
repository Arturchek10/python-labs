import tkinter as tk
from tkinter import colorchooser


class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Приложение для рисования")
        self.root.geometry("800x600")

        # атрибуты кисти
        self.brush_color = "black"
        self.brush_size = 5

        # создание холста для рисования
        self.canvas = tk.Canvas(self.root, bg="white", width=700, height=500)
        self.canvas.pack(pady=10)

        #привязка событий мыши к холсту
        self.canvas.bind("<B1-Motion>", self.paint)

        # панель управления
        self.control_frame = tk.Frame(self.root)
        self.control_frame.pack()

        # кнопка выбора цвета
        self.color_button = tk.Button(self.control_frame, text="Выбрать цвет", command=self.choose_color)
        self.color_button.grid(row=0, column=0, padx=5)

        # поле ввода толщины кисти
        self.size_label = tk.Label(self.control_frame, text="Толщина кисти:")
        self.size_label.grid(row=0, column=1, padx=5)
        self.size_entry = tk.Entry(self.control_frame, width=5)
        self.size_entry.insert(0, "5")
        self.size_entry.grid(row=0, column=2, padx=5)

        # Кнопка очистки холста
        self.clear_button = tk.Button(self.control_frame, text="Очистить", command=self.clear_canvas)
        self.clear_button.grid(row=0, column=3, padx=5)

    "рисование линии на холсте при движении мыши"
    def paint(self, event):
      x1, y1 = event.x - self.brush_size, event.y - self.brush_size
      x2, y2 = event.x + self.brush_size, event.y + self.brush_size
      self.canvas.create_oval(x1, y1, x2, y2, fill=self.brush_color, outline=self.brush_color)

    "открытие диалога выбора цвета и обновление текущего цвета"
    def choose_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.brush_color = color

    def clear_canvas(self):
        self.canvas.delete("all")

    "обновление толщины кисти из поля ввода"
    def update_brush_size(self):        
      size = int(self.size_entry.get())
      if size > 0:
          self.brush_size = size


if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)

    # привязка обновления размера кисти
    app.size_entry.bind("<Return>", lambda e: app.update_brush_size())

    root.mainloop()
