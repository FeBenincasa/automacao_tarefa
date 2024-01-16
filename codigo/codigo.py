# Passo a passo do projeto

# Passo 1 - Entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

# pip install pyautogui
import pyautogui
import time

# clicar -> pyautogui.click
# escrever um texto -> pyautogui.write
# apertar uma tecla -> pyautogui.press
# apertar atalho -> pyautogui.hotkey
# scroll -> pyautogui.scroll
pyautogui.PAUSE = 0.2
# aperta a tecla do windows
pyautogui.press("win")
# digita o nome do programa (navegador)
pyautogui.write("edge")
# aperta enter
pyautogui.press("enter")

# digitar o link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
# apertar enter
pyautogui.press("enter")

# espera 5 segundos
time.sleep(2)


# Passo 2 - Fazer login

# clicar no espaco de email
pyautogui.click(x=790, y=352)
# escrever o email
pyautogui.write("teste@gmail.com")
# clicar no espaco de senha
pyautogui.press("tab")
# escrever a senha
pyautogui.write("python123")
# entrar
pyautogui.press("enter")
time.sleep(2)

# Passo 3 - Importar a base de dados
# pip install pandas numpy openpyxl
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
    # Passo 4 - Cadastrar um produto
    pyautogui.click(x=680, y=240)
    # codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
    # marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    # tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    # categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    # preco
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    # custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    # obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    # enviar o produto
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000) # or pgup


# Passo 5 - Repetir isso ate acabar a base de dados