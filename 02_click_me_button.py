# https://flet.dev/docs/controls/elevatedbutton

import flet as ft


def main(page: ft.Page):
    
    # page(アプリ画面)の設定
    page.title = "CLICK ME BUTTON"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.colors.INDIGO_50
    page.padding = 50
    page.window_height = 500
    page.window_width = 500
    
    
    # buttonがクリックされたときのコールバック
    def change_text(e):
        text.value = "You Clicked!"     # textの文字を変更
        text.color = ft.colors.RED_700  # textの色を変更
        text.size = 40                  # textのサイズを変更
        button.visible = False          # ボタンを非表示
        page.update()                   # pageを更新
    
    # テキスト表示部分を作成
    text = ft.Text("Hello world!", size=20, color=ft.colors.BLUE_500)
    
    # ボタンを作成
    # クリックされたときのコールバックとしてchenge_textを実行
    button = ft.ElevatedButton("CLICK ME", on_click=change_text) 
    
    # コントロールを部品に追加
    page.add(text)
    page.add(button)

    # アプリ画面を更新    
    page.update()


# デスクトップアプリとして開く
ft.app(target=main)

# webアプリとして開く場合は任意のポート番号を指定し
# ブラウザでlocalhost:7777を開く
# ft.app(target=main, port=7777)
    
