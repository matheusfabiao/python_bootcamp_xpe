# atualizar o pip: python.exe -m pip install --upgrade pip
# pip install <nome_pacote>
from colorama import Fore, Back, Style  # (cores no terminal)
# pip install colorama
print('Texto normal')
print(Fore.BLUE + 'Texto azul')
print(Back.BLUE + Fore.WHITE + 'Texto branco com fundo azul')
print(Style.RESET_ALL + 'Texto normal novamente')
# pip install --upgrade <nome_pacote>
