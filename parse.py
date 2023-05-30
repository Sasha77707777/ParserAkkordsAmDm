import os
import time

import requests
from bs4 import BeautifulSoup as bs

clear = lambda: os.system('cls')
exit = lambda: os.system('exit')
clear()


# Это программа для быстрого переноса аккордов с сайта AmDm в txt файл
# Вот ссылка на него: https://amdm.ru/

def parse(url):
    responce = requests.get(url)
    soup = bs(responce.text, "html.parser")
    return (soup.pre).text

def main(link):
    text = parse(link)
    return text
  

def zapis(link):
        with open("Akkords.txt", "w", encoding="utf-8") as file:
            textOnFile = str(main(link))
            file.writelines(textOnFile)


if __name__ == "__main__":
    Flag = True
    if Flag:
        while Flag:
            link = str(input("Введите ссылку на песню: "))
            clear()
            print(main(link))
            zapis(link)
            print("\n")
            print("ГОТОВО, файл записан!\n\n")
            
            next_step = 1
            
            print("1 - ДА\n2 - НЕТ")
            next_step = int(input("Желаете продолжить: "))
            
            clear()
            
            if next_step == 1:
                print()
                continue
            elif next_step == 2:
                print("\nВсего доброго!")
                time.sleep(2)
                clear()
                break
            else:
                while next_step not in [1, 2]:
                    next_step = int(input("Введите корректное значение: "))
else:
    print("Ошибка в работе программы")           

time.sleep(0.5)
exit()