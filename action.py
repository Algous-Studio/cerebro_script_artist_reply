import cerebro
import os

# Получаем абсолютный путь к папке скрипта
script_directory = os.path.abspath(os.path.dirname(__file__))
# Объединяем путь к иконке с папкой скрипта
pic_path = os.path.join(script_directory, 'icon.png')

def init_actions():
    # Получаем тулбар форума сообщений
    messageForumToolBar = cerebro.actions.MessageForumToolBar()
    # Добавляем действие "Artist reply" в тулбар
    messageForumToolBar.add_action('cerebro_script_artist_reply.action.artist_reply', 'Artist reply', pic_path)

    # Получаем меню форума сообщений
    messageMenu = cerebro.actions.MessageForumMenu()
    # Вставляем действие "Artist reply" в меню
    messageMenu.insert_action(0, 'cerebro_script_artist_reply.action.artist_reply', 'Artist reply', pic_path)

def artist_reply():
    # Получаем текущую задачу
    task = cerebro.core.current_task()
    print('Текущая задача:', task.name())

    # Генерируем HTML-строку
    html_string = (
        "<p>СТАТУС:</p>\n"
        "<p></p>\n"
        "<p></p>\n"
        "<p>ЧТО СДЕЛАНО:</p>\n"
        "<p>1 -</p>\n"
        "<p>2 -</p>\n"
        "<p>3 -</p>\n"
        "<p></p>\n"
        "<p>ЧТО БУДЕТ СДЕЛАНО:</p>\n"
        "<p>1 -</p>\n"
        "<p>2 -</p>\n"
        "<p>3 -</p>\n"
        "<p></p>\n"
        "<p>ПРОБЛЕМЫ/ВОПРОСЫ:</p>\n"
        "<p></p>\n"
    )

    # Открываем редактор сообщений с сгенерированным HTML-текстом
    cerebro.gui.message_editor(1, task.id(), html_text=html_string)