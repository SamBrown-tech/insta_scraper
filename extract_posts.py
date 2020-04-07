import bs4
import selenium.webdriver as webdriver

from bs4 import BeautifulSoup as soup

# making new file
file = 'posts.csv'
f = open(file, 'w')


# site url
base_url = 'https://www.instagram.com'
url = 'https://www.instagram.com/viewfervor'


# using driver to access website
driver = webdriver.Chrome('C:/Users/Eigenaar/chromedriver.exe')
driver.get(url)


# get page source
page = soup(driver.page_source, 'html.parser')


# getting suffix for single posts and writing to file
suffix_list = page.findAll('div', {'class':'v1Nh3'})

for el in suffix_list:
	suffix = el.a['href']
	print(suffix)
	f.write(base_url + suffix + '\n')

f.close()