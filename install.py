import os
import time


os.system('cls||clear')
time.sleep(1)

def banner():
    print('''\033[33m
    
===================================    
 ### ###  #####    ##  ##   ##  ##
 #######  ##       ### ##   ##  ##
 ## # ##  ####     ######   ##  ##
 ## # ##  ##       ## ###   ##  ##
 ##   ##  #####    ##  ##    ####
 ===================================

           
           Gilmar Filho
        =============================
             '//||\\`
               ''`` 
Espero ter te ajudado com esse script\033[m''')
banner()
print('\n')
menu = 0
while menu != 7:
    menu = int(input(('''
    [ 1 ] Youtube
    [ 2 ] Intalar Todas As Dependencias
   
    
    Coloque a opção desejada: ''')))
    if menu == 2:
     os.system('cls||clear')
    
    
    print('\n')
    
     if menu == 2:
    print("Autualizando os repostitorio")
    os.system("apt-get update")
    os.system("apt-get upgrade")
    
    print("Instalando as dependicias")
    
    os.system('apt install git')
    os.system("apt-get install")
    
    print("Instalando o python")
    
    os.system("apt-get install python")
    os.system("apt-get install python2")
    os.system("apt-get install python3")
    
    
    print('\n')
    
   
