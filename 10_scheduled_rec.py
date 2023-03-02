import flet as ft
import cv2
import base64
import numpy as np
from datetime import datetime
import time


def main(page: ft.Page):
    
    # page(アプリ画面)の設定
    page.title = "KSB RECORDER"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.colors.INDIGO_50
    page.padding = 50
    page.window_height = 500
    page.window_width = 800
    
    cap = cv2.VideoCapture(0)

    # numpy画像データをbase64にエンコードする関数
    def get_base64_img(img):
        _, encoded = cv2.imencode(".jpg", img)
        img_base64 = base64.b64encode(encoded).decode("ascii")
        return img_base64
    

    
    # 初期画像（ダミー）
    img_blank = 255*np.ones((300, 533, 3), dtype="uint8")
    img_h, img_w, _ = img_blank.shape
    image_display = ft.Image(src_base64=get_base64_img(img_blank),
                             width=img_w, height=img_h, fit=ft.ImageFit.CONTAIN)
    
    checkbox_rec = ft.Checkbox(value=True, label="録画")
    rec_start_textfield = ft.TextField(value="17:48:00", label="録画開始時刻", width=150, height=60, text_size=20, hint_text="hh:mm:ss")
    rec_stop_textfield = ft.TextField(value="19:05:00", label="録画終了時刻", width=150, height=60, text_size=20, hint_text="hh:mm:ss")
    current_time_textfield = ft.TextField(value="00:00:00", label="現在の時刻", width=150, height=60, text_size=20)
    
    rec_start = datetime.strptime(rec_start_textfield.value, "%H:%M:%S")
    rec_stop = datetime.strptime(rec_stop_textfield.value, "%H:%M:%S")
    
    print(rec_start)
    print(rec_stop)
    
    control_panel = ft.Column([checkbox_rec,
                                rec_start_textfield,
                                rec_stop_textfield,
                                current_time_textfield], alignment="start")
    

    
    page.add(ft.Row([image_display, control_panel], vertical_alignment="start"))

    page.update()
    
    is_recording_now = False
    is_recording_now_old = is_recording_now
    
    while True:
        now = datetime.now()
        current_time_str = now.strftime("%H:%M:%S")
        current_time_textfield.value = current_time_str
        ret, img = cap.read()
        # print(ret)
        # img = cv2.resize(img, (img_w, img_h))
        image_display.src_base64 = get_base64_img(img)
        
        rec_start_hhmmss = int((rec_start_textfield.value).replace(":", ""))
        rec_stop_hhmmss = int((rec_stop_textfield.value).replace(":", ""))
        current_time_hhmmss = int((current_time_textfield.value).replace(":", ""))
        
        if rec_start_hhmmss <= current_time_hhmmss < rec_stop_hhmmss:
            is_recording_now = True
        else:
            is_recording_now = False
        
        print(is_recording_now)
        is_recording_now_old = is_recording_now
        
        page.update()




# デスクトップアプリとして開く
ft.app(target=main)

# webアプリとして開く場合は任意のポート番号を指定し
# ブラウザでlocalhost:7777を開く
# ft.app(target=main, port=7777)
    
