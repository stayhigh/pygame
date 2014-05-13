#-*- encoding:utf8 -*-
#!/usr/bin/env python

background_image_filename = 'sushiplate.jpg'
mouse_image_filename = 'fugu.png'
#指定图像文件名称

import pygame
#导入pygame库
from pygame.locals import *
#from pygame.key import *
#导入一些常用的函数和常量
from sys import exit
#向sys模块借一个exit函数用来退出程序

def handleMouse():
    """@todo: Docstring for handleMouse.

    :arg1: @todo
    :returns: @todo

    """
    return pygame.mouse.get_pos()


def handleKeys(eventName):
    """@todo: Docstring for handleKeys.

    :arg1: @todo
    :returns: @todo

    """
    key_msg = "<KEY_UnAssigned>"
    if eventName.key == K_LEFT:
        key_msg = "K_LEFT"
    elif eventName.key == K_RIGHT:
        key_msg = "K_RIGHT"
    elif eventName.key == K_UP:
        key_msg = "K_UP"
    elif eventName.key == K_DOWN:
        key_msg = "K_DOWN"
    else:
        key_msg = "else KEY"

    return key_msg

def handleEvent():
    """@todo: Docstring for doEvent.

    :arg1: @todo
    :returns: @todo

    """
    for event in pygame.event.get():
        if event.type == QUIT:
            #接收到退出事件后退出程序
            exit()
        elif event.type == ACTIVEEVENT:
            print "print ACTIVEEVENT"
        elif event.type == KEYDOWN:
            print "KEYDOWN:", handleKeys(event)
        elif event.type == KEYUP:
            print "KEYUP"
        elif event.type == MOUSEMOTION:
            print "MOUSE MOTION:", handleMouse()
        elif event.type == MOUSEBUTTONDOWN:
            print "MOUSEBUTTONDOWN"
        elif event.type == JOYAXISMOTION:
            print "JOYAXISMOTION"
        elif event.type == JOYBALLMOTION:
            print "JOYBALLMOTION"
        elif event.type == JOYHATMOTION:
            print "JOYHATMOTION"
        elif event.type == JOYBUTTONDOWN:
            print "JOYBUTTONDOWN"
        elif event.type == JOYBUTTONUP:
            print "JOYBUTTONUP"
        elif event.type == VIDEORESIZE:
            print "VIDEORESIZE"
        elif event.type == VIDEOEXPOSE:
            print "VIDEOEXPOSE"
        elif event.type == USEREVENT:
            print "USEREVENT"
        else:
            print "else EVENT"

pygame.init()
#初始化pygame,为使用硬件做准备

screen = pygame.display.set_mode((640, 480), 0, 32)
#创建了一个窗口
pygame.display.set_caption("Hello, World!")
#设置窗口标题

background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()
#加载并转换图像

while True:
#游戏主循环
    handleEvent()
    screen.blit(background, (0,0))
    #将背景图画上去

    x, y = pygame.mouse.get_pos()
    #获得鼠标位置
    x-= mouse_cursor.get_width() / 2
    y-= mouse_cursor.get_height() / 2
    #计算光标的左上角位置
    screen.blit(mouse_cursor, (x, y))
    #把光标画上去

    pygame.display.update()
    #刷新一下画面
