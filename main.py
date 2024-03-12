import requests
from bs4 import BeautifulSoup
from datetime import datetime

x = datetime.now()
x = x.strftime("%d/%m/%y %A")

def take_in_log():
    val = input("Link: ")
    r = requests.get(val)
    soup = BeautifulSoup(r.content, 'html5lib')
    name = ""
    div_element = soup.find('a', attrs ={'class':'no-underline hover:text-blue-s dark:hover:text-dark-blue-s truncate cursor-text whitespace-normal hover:!text-[inherit]'})
    if div_element:
        name = div_element.text.strip()
    difficulty = ""
    if soup.find('div', attrs ={'class':'relative inline-flex items-center justify-center text-caption px-2 py-1 gap-1 rounded-full bg-fill-secondary text-difficulty-easy dark:text-difficulty-easy'}):
        difficulty = "Easy"
    elif soup.find('div', attrs ={'class':'relative inline-flex items-center justify-center text-caption px-2 py-1 gap-1 rounded-full bg-fill-secondary text-difficulty-medium dark:text-difficulty-medium'}):
        difficulty = "Medium"
    elif soup.find('div', attrs = {'class':'relative inline-flex items-center justify-center text-caption px-2 py-1 gap-1 rounded-full bg-fill-secondary text-difficulty-hard dark:text-difficulty-hard'}):
        difficulty = "Hard"
    print(f"{x}\n{name} - {difficulty}")
take_in_log()


