import cerebro
import os

script_directory = os.path.abspath(os.path.dirname(__file__))
pic_path = os.path.join(script_directory, 'icon.png')

def init_actions():
    messageForumToolBar = cerebro.actions.MessageForumToolBar()
    messageForumToolBar.add_action('cerebro_script_artist_reply.action.artist_reply', 'Artist reply', pic_path)

    messageMenu = cerebro.actions.MessageForumMenu()
    messageMenu.insert_action(0, 'cerebro_script_artist_reply.action.artist_reply', 'Artist reply', pic_path)

def artist_reply():
    task = cerebro.core.current_task()
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

    cerebro.gui.message_editor(1, task.id(), html_text=html_string)