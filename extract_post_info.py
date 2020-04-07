import bs4
import csv
import selenium.webdriver as webdriver
# to auto-save images
import urllib.request

from bs4 import BeautifulSoup as soup

likes = []
imgs = []

# retreiving the urls
with open('posts.csv') as f:
	csv_reader = csv.reader(f, delimiter=',')
	for row in csv_reader:
		# print(row[0])

		url = row[0]

		# using driver to access website
		driver = webdriver.Chrome('C:/Users/Eigenaar/chromedriver.exe')
		driver.get(url)


		# getting page source
		page = soup(driver.page_source, 'html.parser')

		# getting likes and image url
		like = page.find('div', {'class':'Nm9Fw'}).span.text
		likes.append(like)

		img_url = page.find('div', {'class':'KL4Bh'}).img['src']
		imgs.append(img_url)


		# TODO: saving images to local machine


		# saving image to local machine
		# urllib.request.urlretrieve(img_url, 'C://Users//Eigenaar//Documents//programming//python//webscrape//instagram//img') # url , local_path

print(likes)
print(imgs)


## site url
# url = 'https://www.instagram.com/viewfervor'


# # using driver to access website
# driver = webdriver.Chrome('C:/Users/Eigenaar/chromedriver.exe')
# driver.get(url)


# # get page source
# page = soup(driver.page_source, 'html.parser')


# # getting suffix for single posts and writing to file
# suffix_list = page.findAll('div', {'class':'v1Nh3'})

# for el in suffix_list:
# 	suffix = el.a['href']
# 	print(suffix)
# 	f.write(base_url + suffix + '\n')

# f.close()