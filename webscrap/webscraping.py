import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/Users/alika/Downloads/webdrive/chromedriver.exe')
driver.get('https://oxylabs.io/blog')
results = []
other_results = []
content = driver.page_source
soup = BeautifulSoup(content)

for a in soup.find_all(attrs='css-1dmex2s e1kk1ckf2'):
    name = a.find('h5')
    if name not in results:
        results.append(name.text)

for b in soup.find_all(attrs='css-16hh3lg e15x7lld0'):
    date = b.find('p')
    if date not in results:
        other_results.append(date.text)

df = pd.DataFrame({'Names': results,'Dates': other_results})
df.to_csv('names.csv', index=False, encoding='utf-8')
