import flet as ft


def main(page: ft.Page):
    
    # page(アプリ画面)の設定
    page.title = "Hello World"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.colors.INDIGO_50
    page.padding = 50
    page.window_height = 500
    page.window_width = 500
    
    # コントロール（部品）の作成
    text = ft.Text("Hello world!", size=20, color=ft.colors.BLUE_500)
    
    # コントロールを部品に追加
    page.add(text)

    # アプリ画面を更新    
    page.update()


# デスクトップアプリとして開く
ft.app(target=main)

# webアプリとして開く場合は任意のポート番号を指定し
# ブラウザでlocalhost:7777を開く
# ft.app(target=main, port=7777)
    
