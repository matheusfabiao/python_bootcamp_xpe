"""
Faça um programa que abra e reproduza o áudio de um arquivo MP3
"""
import pygame
pygame.init()
# Insirir o arquivo mp3 na mesma pasta que este
pygame.mixer.music.load('STARSET PERFECT MACHINE.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
