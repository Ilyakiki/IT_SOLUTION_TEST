import cv2
import numpy as np


# Функция для создания видео с бегущей строкой
def create_video(text: str):
    # Текст пользователя
    message = text.encode(encoding="utf-8").decode(encoding="utf-8")
    width, height = 100, 100  # Задаем размеры окна

    out = cv2.VideoWriter("ready_video.mp4", cv2.VideoWriter_fourcc(*'mp4v'), 60, (width, height))  # Видеопоток счастотой 60 кдаров в секунду
    frame = np.zeros((height, width, 3), dtype=np.uint8)  # Создаем кадр с черным фоном

    x, y = width, height // 2  # Начальные координаты для бегущей строки

    # Установим параметры шрифта
    font = cv2.FONT_HERSHEY_COMPLEX  # Выбираем данный,так как большинство не работают с русским языком
    font_scale = 0.7
    font_thickness = 1
    font_color = (125, 55, 255)  # Розовый цвет текста

    for t in range(180):  # 3 секунды с частотой 60 кадра/сек

        frame.fill(0)  # Очистка кадра
        speed=len(text)//10
        if len(text)<10:
            speed=1
        x -= speed # Скорость бегущей строки

        cv2.putText(frame, message, (x, y), font, font_scale, font_color, font_thickness)  # Добавление текста в кадр

        out.write(frame)  # Фиксация кадра

    # Закроем тут видеопоток
    out.release()
