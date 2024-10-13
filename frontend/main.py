import flet as ft
import requests

class Message(ft.Container):
    def __init__(self, author, body):
        super().__init__()
        self.content = ft.Column(
            controls=[
                ft.Text(author, weight=ft.FontWeight.BOLD),
                ft.Text(body),
            ],
        )
        self.border_radius = ft.border_radius.all(10)
        self.bgcolor = ft.colors.INDIGO_ACCENT
        self.padding = 10
        self
        self.expand = True
        self.expand_loose = True


# Основная функция для запуска приложения
def main(page: ft.Page):
    page.title = "VERS"
    page.theme_mode = ft.ThemeMode.DARK  # Тёмная тема
    page.window.maximized = True
    page.horizontal_alignment = (
        ft.CrossAxisAlignment.START
    )  # Выравнивание по горизонтали

    chats = ft.Column([
            ft.Container(
                    content=ft.Text('Новый чат'),
                    alignment=ft.alignment.center,
                    height=50,
                    bgcolor=ft.colors.AMBER,
                    border_radius=ft.border_radius.all(5),
            ),        
    ] * 20, scroll=ft.ScrollMode.AUTO)
    profile = ft.Row(
        [
            ft.CircleAvatar(),
            ft.Text('Имя профиля', expand=True),
            ft.IconButton(icon=ft.icons.SETTINGS)
        ],
        alignment=ft.MainAxisAlignment.START
    )

    # Левый блок: список чатов
    chats_and_profile = ft.Column(
        [
            ft.Container(
                content=chats,
                margin=ft.margin.only(left=5, right=5, top=5),
                padding=10,
                bgcolor=ft.colors.INDIGO,
                width=250,
                height=650,
                border_radius=10,
                
            ),
            ft.Divider(height=5),
            ft.Container(
                content=profile,
                margin=ft.margin.only(left=5, right=5, bottom=5),
                padding=5,
                bgcolor=ft.colors.INDIGO,
                width=250,
                height=70,
                border_radius=10,
            ),
        ],
        scroll=ft.ScrollMode.ALWAYS,  # Добавляем прокрутку
    )

    chatname = ft.Column(
        [
            ft.Text('Название чата', text_align=ft.MainAxisAlignment.START),
            ft.Text('Статус', text_align=ft.MainAxisAlignment.START, size=10),
        ],
        alignment=ft.MainAxisAlignment.START,
    )
    
    messages = ft.ListView(
        padding=10,
        spacing=10,
        controls=[
            ft.Row(
                alignment=ft.MainAxisAlignment.START,
                controls=[
                    Message(
                        author="John",
                        body="Hi, how are you?",
                    ),
                ],
            ),
            ft.Row(
                alignment=ft.MainAxisAlignment.END,
                controls=[
                    Message(
                        author="Jake",
                        body="Hi I am good thanks, how about you?",
                    ),
                ],
                
            ),
            ft.Row(
                alignment=ft.MainAxisAlignment.START,
                controls=[
                    Message(
                        author="John",
                        body="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.",
                    ),
                ],
            ),
            ft.Row(
                alignment=ft.MainAxisAlignment.END,
                controls=[
                    Message(
                        author="Jake",
                        body="Thank you!",
                    ),
                ],
            ),
        ],
    )


    

    send_message_row = ft.Row(
        [
            ft.Text('Отправить'),
            ft.Text('Написать блавлавдл')
        ]
    )

    # Центральная часть: список сообщений
    message_list = ft.Column(
        [
            chatname,
            ft.Divider(thickness=2),
            messages,
            ft.Divider(thickness=2),
            send_message_row,
        ],
        expand=True,
    )

    chat = ft.Container(
        content=message_list,
        bgcolor=ft.colors.INDIGO,
        expand=True,
        padding=10,
        margin=10,
        border_radius=10,
        height=750
    )

    # Правая часть: список участников
    participants = ft.Column([ft.Text("Участники", size=16)], width=200)

    # Добавляем 3 основные колонки в макет страницы
    page.add(ft.Row([chats_and_profile, chat, participants], alignment=ft.MainAxisAlignment.SPACE_BETWEEN))

    page.update()  # Обновляем интерфейс


# Запуск приложения
ft.app(target=main)
