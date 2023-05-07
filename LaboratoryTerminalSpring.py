import os
import sys
import tkinter as tk
from PIL import Image, ImageTk
from moviepy.editor import VideoFileClip
import time
import pygame


class TextAnimation(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        # Определяем шрифт.
        font_family = "Courier"
        font_size = 24  # размер шрифта можно изменить
        font = (font_family, font_size)
        # Создаем метку для отображения текста.
        self.text_label = tk.Label(self, font=font, bg="black", fg="lime")
        self.text_label2 = tk.Label(self, font=font, bg="black", fg="lime")
        self.text_label3 = tk.Label(self, font=font, bg="black", fg="lime")
        self.text_label4 = tk.Label(self, font=font, bg="black", fg="lime")
        self.text_label5 = tk.Label(self, font=font, bg="black", fg="lime")
        self.text_label6 = tk.Label(self, font=font, bg="black", fg="lime")
        self.text_label7 = tk.Label(self, text="Ошибка! Материал не найден", font=font, bg="black", fg="lime")
        self.text_label.pack(fill="both", expand=True)
        self.text_label5.pack(fill="both", expand=True)
        self.startButton = tk.Button(root, text="Запуск терминала", command=self.show_video, bg="black", fg="lime",
                                     activebackground="lime",
                                     activeforeground="black", relief=tk.SOLID, font=("Courier", 48))
        # self.button = tk.Button(text="Выход", command=quit, bg="black", fg="lime", activebackground="lime",
        #                         activeforeground="black", relief=tk.SOLID, font=font)
        self.button2 = tk.Button(text="Запустить", command=self.receipt_search, bg="black", fg="lime",
                                 activebackground="lime",
                                 activeforeground="black", relief=tk.SOLID, font=font)
        self.button3 = tk.Button(text="Начать анализ", command=self.receipt_download, bg="black", fg="lime",
                                 activebackground="lime",
                                 activeforeground="black", relief=tk.SOLID, font=font)
        self.buttonCheck = tk.Button(text="Пробирка помещена", command=self.set_material, bg="black", fg="lime",
                                     activebackground="lime",
                                     activeforeground="black", relief=tk.SOLID, font=font)
        self.button_counter = 0
        self.isMaterialPut = False
        pygame.mixer.init()
        self.sound = pygame.mixer.Sound(resource_path("dialupFullv2.mp3"))
        volume = self.sound.get_volume() * 1.5
        self.sound.set_volume(volume)
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()
        # Определяем текст, который нужно отобразить.
        self.text = ""

    def quit(self):
        root.quit()

    def animate_text(self, text, label, animIndex):
        """Анимация вывода текста на экран."""
        self.text = text
        self.index = 0
        self.photo = None  # сохраняем ссылку на изображение в атрибут класса
        self.update_text(label, animIndex)

    def update_text(self, label, animIndex):
        """Обновляет отображаемый текст."""
        if self.index < len(self.text):
            # Добавляем следующий символ к отображаемому тексту.
            label.configure(text=self.text[:self.index + 1])
            self.index += 1
            # Планируем вызов этой же функции через 100 миллисекунд.
            self.after(100, self.update_text, label, animIndex)
        elif self.index == len(self.text):
            # Удаляем ссылку на изображение.
            self.photo = None
            if animIndex == 1:
                self.button2.pack(side=tk.TOP)
                # while time.time() < fintime:
                #     self.animate_text("Поиск файла, пожалуйста, подождите...", self.text_label2)
            elif animIndex == 2:
                time.sleep(5)
                self.receipt_found()
                self.button_counter += 1
            elif animIndex == 3:
                self.button3.pack()
                self.button3.place()
                self.buttonCheck.pack()
            elif animIndex == 4:
                formula_image = Image.open(resource_path("Формула сыворотки.png")).resize((400, 300))
                photo = ImageTk.PhotoImage(formula_image)
                formula_label = tk.Label(self.master, image=photo)
                formula_label.place(x=10, y=10)
                formula_label.image = photo
                formula_label.pack()
            # elif animIndex == 5:
            #     self.text_label6.pack(fill="both", expand=True, side=tk.BOTTOM)
            #     self.animate_text("Бла-бла-бла, бла-бла-бла, бла-бла-бла", self.text_label6, 0)

    def receipt_search(self):
        self.text_label.destroy()
        self.text_label2.pack(fill="both", expand=True)
        # global fintime
        # fintime = time.time() + 15
        self.animate_text("Запускаю анализатор, пожалуйста, подождите...", self.text_label2, 2)
        self.button2.destroy()

    def receipt_found(self):
        self.text_label2.destroy()
        with open(resource_path("anal.txt"), "r", encoding="utf-8") as k:
            analtext = k.read()
        self.text_label3.pack()
        self.animate_text(analtext, self.text_label3, 3)

    def receipt_download(self):
        if not self.isMaterialPut:
            self.text_label7.pack(fill="both", expand=True, side=tk.BOTTOM)
        else:
            self.button3.destroy()
            self.text_label3.destroy()
            self.text_label4.pack(fill="both", expand=True)
            self.animate_text("Провожу анализ............", self.text_label4, 0)
            self.show_video()

    def start(self):
        self.startButton.pack(side=tk.BOTTOM)



    def set_material(self):
        self.buttonCheck.destroy()
        self.isMaterialPut = True
        if self.text_label7:
            self.text_label7.destroy()

    def show_video(self):
        if self.startButton:
            self.startButton.destroy()
        if self.button_counter > 0 and self.text_label7:
            self.text_label7.destroy()
            # Воспроизводим звуковой файл.
            self.sound.play()
            video_path = resource_path('CompressedAnalysing.mp4')
            # pygame.time.wait(int(self.sound.get_length() * 1000))
        # Загружаем видео с помощью библиотеки moviepy.
        else:
            video_path = resource_path('loading.mp4')
        clip = VideoFileClip(video_path)
        # Получаем первый кадр из видео, конвертируем его в объект PIL.Image
        # и создаем объект PhotoImage на основе изображения.
        first_frame = clip.get_frame(0)
        frame_image = Image.fromarray(first_frame)
        self.photo = ImageTk.PhotoImage(frame_image.resize((self.screen_width, self.screen_height)))
        # сохраняем ссылку на изображение в атрибут класса
        label = tk.Label(self.master, image=self.photo)
        label.pack(side=tk.TOP)
        # Определяем функцию для обновления кадров.
        def update(ind):
            """Обновляет кадр видео."""
            frame = clip.get_frame(ind * 1.0 / clip.fps)
            frame_image = Image.fromarray(frame)
            photo = ImageTk.PhotoImage(frame_image.resize((self.screen_width, self.screen_height)))
            label.configure(image=photo)
            label.image = photo
            if self.button_counter > 0:
                ind += 3.2
            else:
                ind += 1.5
            if ind >= clip.fps * clip.duration:  # останавливаем воспроизведение видео после окончания файла
                label.destroy()
                if self.button_counter > 0:
                    pygame.quit()
                    self.text_label4.destroy()
                    with open(resource_path("antidote.txt"), "r", encoding="utf-8") as f:
                        text2 = f.read()
                    self.animate_text(text2, self.text_label5, 4)
                else:
                    with open(resource_path("test.txt"), "r", encoding="utf-8") as f:
                        text = f.read()
                    self.button_counter += 1
                    self.animate_text(text, self.text_label, 1)  # запускаем анимацию вывода текста
                    # self.button.pack(side=tk.BOTTOM)
                return
            self.master.after(int(1000 / clip.fps), update, ind)

        # Запускаем воспроизведение видео.
        update(0)


if __name__ == '__main__':
    def resource_path(relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(bg="black")
    app = TextAnimation(master=root)
    app.start()
    app.mainloop()


