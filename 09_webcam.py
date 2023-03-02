# https://flet.dev/docs/controls/image

import flet as ft
import cv2
import base64
import numpy as np


def main(page: ft.Page):
    
    # page(アプリ画面)の設定
    page.title = "WEBCAM"
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
    

    
    page.add(image_display)

    page.update()
    
    while True:
        ret, img = cap.read()
        # print(ret)
        # img = cv2.resize(img, (img_w, img_h))
        image_display.src_base64 = get_base64_img(img)
        page.update()




# デスクトップアプリとして開く
ft.app(target=main)

# webアプリとして開く場合は任意のポート番号を指定し
# ブラウザでlocalhost:7777を開く
# ft.app(target=main, port=7777)
    
