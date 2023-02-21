# https://flet.dev/docs/controls/image

import flet as ft
import cv2
import base64
import numpy as np


def main(page: ft.Page):
    
    # page(アプリ画面)の設定
    page.title = "IMAGE DISPLAY"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.colors.INDIGO_50
    page.padding = 50
    page.window_height = 500
    page.window_width = 800
    
    
    # OpenCVで画像を読み込み
    img = cv2.imread("sample_imgs/ramen.jpg")
    img = cv2.resize(img, dsize=None, fx=0.3, fy=0.3)
    img_h, img_w, _ = img.shape
    
    # base64にエンコード
    _, encoded = cv2.imencode(".jpg", img)
    img_base64 = base64.b64encode(encoded).decode("ascii")
    
    # Imageコントロールを作成
    image_display = ft.Image(src_base64=img_base64, width=img_w, height=img_h)
    
    # コントロールを部品に追加
    page.add(image_display)

    # アプリ画面を更新    
    page.update()


# デスクトップアプリとして開く
ft.app(target=main)

# webアプリとして開く場合は任意のポート番号を指定し
# ブラウザでlocalhost:7777を開く
# ft.app(target=main, port=7777)
    
