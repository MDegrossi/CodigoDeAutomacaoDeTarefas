# Arquivo para auxiliar a descobrir a posição do mouse(X, Y)
# Tambem arquivo de testes para alguns comando em python

import pyautogui
import time
import pandas


time.sleep(5)
print(pyautogui.position()) # Comando que da a posição do mouse(pyautogui.position)

pyautogui.scroll(1000)

tabela = pandas.read_csv('produtos.csv')
print(tabela)