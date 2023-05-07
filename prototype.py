import tkinter as tk
from PIL import Image, ImageTk
from moviepy.editor import VideoFileClip

root = tk.Tk()
root.configure(bg="black")
frame2 = tk.Frame()
frame2.configure(bg="black")
text = "Le Kekis"

def quit():
    frame2.quit()
    root.quit()


# Определяем шрифт.
font_family = "Courier"
font_size = 14  # размер шрифта можно изменить
font = (font_family, font_size)

tk.Label(master=frame2, bg="black", fg="lime", justify=tk.CENTER, font=font).pack()
tk.Button(master=frame2, text="Выход", command=quit, bg="black", fg="lime", activebackground="lime",
          activeforeground="black", relief=tk.SOLID, font=font).pack(side=tk.BOTTOM)


# Загружаем видео с помощью библиотеки moviepy.
video_path = 'C:/Users/shalo/PycharmProjects/laba1/loading.mp4'
clip = VideoFileClip(video_path)

# Получаем первый кадр из видео, конвертируем его в объект PIL.Image
# и создаем объект PhotoImage на основе изображения.
first_frame = clip.get_frame(0)
frame_image = Image.fromarray(first_frame)
frame = ImageTk.PhotoImage(frame_image)

# Создаем метку, которая будет отображать видео.
label = tk.Label(root, image=frame)
label.pack()


# Определяем функцию для обновления кадров.
def update(ind):
    """Обновляет кадр видео."""
    frame = clip.get_frame(ind * 1.0 / clip.fps)
    frame_image = Image.fromarray(frame)
    photo = ImageTk.PhotoImage(frame_image)
    label.configure(image=photo)
    label.image = photo
    ind += 1
    if ind >= clip.fps * clip.duration:  # останавливаем воспроизведение видео после окончания файла
        label.destroy()
        frame2.pack()
        update_text(text, 0, label.image)
        return
    root.after(int(1000 / clip.fps), update, ind)

def update_text(text, index, photo):
        """Обновляет отображаемый текст."""
        if index < len(text):
            # Добавляем следующий символ к отображаемому тексту.
            label.configure(text=text[:index+1])
            index += 1
            # Планируем вызов этой же функции через 100 миллисекунд.
            root.after(100, update_text)
        elif index == len(text):
            # Удаляем ссылку на изображение.
            photo = None

# Запускаем воспроизведение видео.
update(0)

root.attributes('-fullscreen', True)
root.mainloop()
