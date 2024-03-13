from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def take_in_log(url):
    x = datetime.now()
    x = x.strftime("%d/%m/%y %A")
        
    driver = webdriver.Chrome()
    driver.get(url)
    name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'no-underline.hover\\:text-blue-s.dark\\:hover\\:text-dark-blue-s.truncate.cursor-text.whitespace-normal.hover\\:\\!text-\\[inherit\\]'))
    )
    try:
        driver.find_element(By.CLASS_NAME, 'relative.inline-flex.items-center.justify-center.text-caption.px-2.py-1.gap-1.rounded-full.bg-fill-secondary.text-difficulty-easy.dark\:text-difficulty-easy')
        difficulty = "Easy"
    except NoSuchElementException:
        try:
            driver.find_element(By.CLASS_NAME, 'relative.inline-flex.items-center.justify-center.text-caption.px-2.py-1.gap-1.rounded-full.bg-fill-secondary.text-difficulty-medium.dark\:text-difficulty-medium')
            difficulty = "Medium"
        except NoSuchElementException:
            driver.find_element(By.CLASS_NAME, 'relative.inline-flex.items-center.justify-center.text-caption.px-2.py-1.gap-1.rounded-full.bg-fill-secondary.text-difficulty-hard.dark\:text-difficulty-hard')
            difficulty = "Hard"
    print(f"{x}\n{name.text} - {difficulty}")
    driver.quit()
    return {"name": name.text, "difficulty": difficulty, "date": x}