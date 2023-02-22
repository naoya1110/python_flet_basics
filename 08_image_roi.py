# https://flet.dev/docs/controls/image
# https://flet.dev/docs/controls/gesturedetector

import flet as ft
import cv2
import base64
import numpy as np




def main(page: ft.Page):
    
    # page(アプリ画面)の設定
    page.title = "IMAGE ROI"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.colors.INDIGO_50
    page.padding = 50
    page.window_height = 500
    page.window_width = 800
    
    
    xy_roi_start = [0, 0]
    xy_roi_end = [0, 0]
    filepath = ""
    
    CYAN = (255, 0, 255)
    LINETYPE = cv2.LINE_AA

    # numpy画像データをbase64にエンコードする関数
    def get_base64_img(img):
        _, encoded = cv2.imencode(".jpg", img)
        img_base64 = base64.b64encode(encoded).decode("ascii")
        return img_base64
    
    def open_img(e):
        global img_original
        scale = img_scale.value
        img = img_original.copy()
        img = cv2.resize(img, dsize=None, fx=scale, fy=scale)
        img_h, img_w, _ = img.shape
        
        # image_displayのプロパティを更新
        image_display.src_base64 = get_base64_img(img)
        image_display.height = img_h
        image_display.width = img_w
        
        # stackのプロパティを更新
        stack.height = img_h
        stack.width = img_w
        
        # pageをアップデート
        page.update()
        
    
    # ファイルが選択された時のコールバック
    def on_img_open(e: ft.FilePickerResultEvent):
        global img_original
        filepath = e.files[0].path
        scale = img_scale.value
        img_original = cv2.imread(filepath)
        img = img_original.copy()
        img = cv2.resize(img, dsize=None, fx=scale, fy=scale)
        img_h, img_w, _ = img.shape
        
        # image_displayのプロパティを更新
        image_display.src_base64 = get_base64_img(img)
        image_display.height = img_h
        image_display.width = img_w
        
        # stackのプロパティを更新
        stack.height = img_h
        stack.width = img_w
        
        # pageをアップデート
        page.update()
    
    def mouse_on_hover(e: ft.HoverEvent):
        mouse_x = int(e.local_x)
        mouse_y = int(e.local_y)
        x_loc.value = mouse_x
        y_loc.value = mouse_y
        page.update()
    
    def on_drag_start(e: ft.HoverEvent):
        global xy_roi_start
        mouse_x = int(e.local_x)
        mouse_y = int(e.local_y)
        x_loc.value = mouse_x
        y_loc.value = mouse_y
        xy_roi_start = [mouse_x, mouse_y]
        print(xy_roi_start)
        page.update()

    def on_drag_update(e: ft.HoverEvent):
        global xy_roi_start, xy_roi_end, img_original
        mouse_x = int(e.local_x)
        mouse_y = int(e.local_y)
        x_loc.value = mouse_x
        y_loc.value = mouse_y
        xy_roi_end = [mouse_x, mouse_y]
        print(xy_roi_start, xy_roi_end)
        xs = [xy_roi_start[0], xy_roi_end[0]]
        ys = [xy_roi_start[1], xy_roi_end[1]]
        scale = img_scale.value
        x0 = int(min(xs)/scale)
        x1 = int(max(xs)/scale)
        y0 = int(min(ys)/scale)
        y1 = int(max(ys)/scale)
        img = img_original.copy()
        img = cv2.rectangle(img, (x0, y0), (x1, y1), CYAN, 5, LINETYPE)
        img = cv2.resize(img, dsize=None, fx=scale, fy=scale)
        img_h, img_w, _ = img.shape
        
        # image_displayのプロパティを更新
        image_display.src_base64 = get_base64_img(img)
        image_display.height = img_h
        image_display.width = img_w
        
        # stackのプロパティを更新
        stack.height = img_h
        stack.width = img_w
        
        
        page.update()
    
    
    filepick_button = ft.ElevatedButton("Open Image", on_click=lambda _: file_picker.pick_files(allow_multiple=True))
    
    # 初期画像（ダミー）
    img_blank = 255*np.ones((300, 300, 3), dtype="uint8")
    img_original = img_blank
    img_h, img_w, _ = img_blank.shape
    image_display = ft.Image(src_base64=get_base64_img(img_blank),
                             width=img_w, height=img_h,
                             fit=ft.ImageFit.CONTAIN)
    
    gd = ft.GestureDetector(
        mouse_cursor=ft.MouseCursor.MOVE,
        on_hover=mouse_on_hover,
        on_horizontal_drag_start=on_drag_start,
        on_horizontal_drag_update=on_drag_update)
    
    x_loc_label = ft.Text("X", size=20)
    x_loc = ft.Text("0", size=20)
    y_loc_label = ft.Text("Y", size=20)
    y_loc = ft.Text("0", size=20)
    
    mouse_loc = ft.Column([ft.Row([x_loc_label, x_loc]),
                           ft.Row([y_loc_label, y_loc])])
    
    img_scale = ft.Slider(value=0.3, max=1.5, min=0.1, on_change=open_img)
    stack = ft.Stack([image_display, gd], width=img_w, height=img_h)
        
    page.add(filepick_button)
    page.add(img_scale)
    page.add(ft.Row([stack, mouse_loc]))
    
    file_picker = ft.FilePicker(on_result=on_img_open)
    page.overlay.append(file_picker)
    page.update()
    



# デスクトップアプリとして開く
ft.app(target=main)

# webアプリとして開く場合は任意のポート番号を指定し
# ブラウザでlocalhost:7777を開く
# ft.app(target=main, port=7777)
    
