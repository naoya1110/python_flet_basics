import flet as ft


def main(page: ft.Page):
    
    # page(アプリ画面)の設定
    page.title = "COUNT UP AND DOWN"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.colors.INDIGO_50
    page.padding = 50
    page.window_height = 500
    page.window_width = 500
    
    
    # plus_buttonがクリックされたときのコールバック
    def on_plus(e):
        text.value = int(text.value) + 1
        page.update()                   # pageを更新
    
    # minus_buttonがクリックされたときのコールバック
    def on_minus(e):
        text.value = int(text.value) - 1
        page.update()                   # pageを更新
    
    # テキスト表示部分を作成
    text = ft.Text(0, size=50, color=ft.colors.BLUE_500)
    
    
    # ボタンを作成
    # クリックされたときのコールバックとしてchenge_textを実行
    plus_button = ft.ElevatedButton("+1", on_click=on_plus)
    minus_button = ft.ElevatedButton("-1", on_click=on_minus)
    buttons = ft.Row([minus_button, plus_button]) # ボタンを横一列に並べる
    
    # コントロールを部品に追加
    page.add(text)
    page.add(buttons)

    # アプリ画面を更新    
    page.update()


# デスクトップアプリとして開く
#ft.app(target=main)

# webアプリとして開く場合は任意のポート番号を指定し
# ブラウザでlocalhost:7777を開く
# ft.app(target=main, port=7777)
    
