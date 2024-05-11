# Pacote do python que transforma pdf em pandas(tabula)
# (pyperclip) Permite que vc escreva caracteres especiais em python

# Passo a Passo

# 1. Abrir o sistema da empresa;
   # https://dlp.hashtagtreinamentos.com/python/intensivao/login

# Para instalar o pyautogui: pip install pyautogui
import pyautogui # Importação das funções
import time # Importação das funções
import pandas as pd # Importação das funções

pyautogui.PAUSE = 2.0

# pyautogui.click -> clicar com o mouse; 
# pyautogui.write -> escrever um texto;
# pyautogui.press -> pressionar uma tecla do teclado;
# pyautogui.hotkey -> apertar um conjunto de teclas(Ctrl C, Ctrl V, Atl Tab)

# Abrir o navegador(Edge)
pyautogui.press('win')
pyautogui.write('Edge')
pyautogui.press('enter')

#Entrar no site do sistema;
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter');

# Pode ser que ele demore alguns segundos para carregar o site 
time.sleep(3); # Função para fazer o codigo esperar/dormir para inicializar o navegador

# 2. Fazer login;
pyautogui.click(x=520, y=361) # Comando para fazer o mouse clicar em uma certa posição da tela
pyautogui.write('matheusdegrossi22@gmail.com')

pyautogui.press('tab') # Passou para o campo de senha
time.sleep(0.5) # Função para esperar a digitação do campo do email para fazer a troca para o campo de senha
pyautogui.write('2912')

pyautogui.press('tab') # Passou para o botao de login
pyautogui.press('enter')

time.sleep(3);

# 3. Abrir/importar a basa de dados de produtos para cadastrar
# pip install panda numpy openpyxl

  
tabela = pd.read_csv('produtos.csv') # Variavel que armazena todos os valores inclusos na tabela

print(tabela)

# 4. Cadastrar um produto;
# str = string = texto
for linha in tabela.index: # função(for) para pegar todas as linha da tabela/indices
   codigo = str(tabela.loc[linha, 'codigo'])
   marca = str(tabela.loc[linha, 'marca'])
   tipo = str(tabela.loc[linha, 'tipo'])
   categoria = str(tabela.loc[linha, 'categoria'])
   preco = str(tabela.loc[linha, 'preco_unitario'])
   custo = str(tabela.loc[linha, 'custo'])
   observacao = str(tabela.loc[linha, 'obs'])

   # Clicar no campo do codigo do produto
   pyautogui.click(x=490, y=237) # Comando para fazer o mouse clicar em uma certa posição da tela
   # Preencher o codigos
   pyautogui.write(codigo)
   # Passar para o proximo campo
   pyautogui.press('tab')
   # Marca
   pyautogui.write(marca)
   # Passar para o proximo campo
   pyautogui.press('tab')
   # Tipo
   pyautogui.write(tipo)
   # Passar para o proximo campo
   pyautogui.press('tab')
   # Categoria
   pyautogui.write(categoria)
   # Passar para o proximo campo
   pyautogui.press('tab')
   # Preço
   pyautogui.write(preco)
   # Passar para o proximo campo
   pyautogui.press('tab')
   # custo
   pyautogui.write(custo)
   # Passar para o proximo campo
   pyautogui.press('tab')
   # Obs
   if observacao != 'nan': # IF usado para ver se a palavra escrita na obs da tabela for diferente de ('nan')
      pyautogui.write(observacao)
   # Passar para o proximo campo
   pyautogui.press('tab')
   # Apertar o botão
   pyautogui.press('enter')
   pyautogui.scroll(1000) # Função que da scroll para cima se for(positivo) e se for scroll para baixo é(negatido (-))

# 5. Repetir isso tudo até acabar a lista de produtos;

