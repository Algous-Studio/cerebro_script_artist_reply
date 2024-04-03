# -*- coding: utf-8 -*-
import cerebro
import os

pic_path = os.path.abspath(os.path.dirname(__file__)) + '/icon.png'




def init_actions():
    messageForumToolBar = cerebro.actions.MessageForumToolBar() # получили тулбар форума сообщений
    messageForumToolBar.add_action('cerebro_script_artist_reply.action.artist_reply', 'Artist reply', pic_path)

    messageMenu = cerebro.actions.MessageForumMenu()
    messageMenu.add_action('cerebro_script_artist_reply.action.artist_reply', 'Artist reply', pic_path)



def artist_reply():
    task = cerebro.core.current_task()
    print('Текущая задача',  task.name())

    text = """
    СТАТУС:
    
    
    ЧТО СДЕЛАНО:
    1 -
    2 -
    3 -
    
    ЧТО БУДЕТ СДЕЛАНО:
    1 -
    2 -
    3 -
    
    ПРОБЛЕМЫ/ВОПРОСЫ:
    """

    cerebro.gui.message_editor(1, task.id(), html_text=text)