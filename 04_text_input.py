# https://flet.dev/docs/controls/textfield

import flet as ft


def main(page: ft.Page):
    
    # page(アプリ画面)の設定
    page.title = "TEXT INPUT"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.colors.INDIGO_50
    page.padding = 50
    page.window_height = 500
    page.window_width = 500
    
    
    # plus_buttonがクリックされたときのコールバック
    def on_add_button(e):
        new_text = ft.Text(textfield.value, size=20, color=ft.colors.GREEN_500)
        page.add(new_text)
        page.update()                   # pageを更新

    
    # テキスト表示部分を作成
    textfield = ft.TextField(label="WRITE HERE")
    
    
    # ボタンを作成
    # クリックされたときのコールバックとしてchenge_textを実行
    add_button = ft.ElevatedButton("add", on_click=on_add_button)

    # コントロールを部品に追加
    page.add(ft.Row([textfield, add_button]) )


    # アプリ画面を更新    
    page.update()


# デスクトップアプリとして開く
ft.app(target=main)

# webアプリとして開く場合は任意のポート番号を指定し
# ブラウザでlocalhost:7777を開く
# ft.app(target=main, port=7777)
    
