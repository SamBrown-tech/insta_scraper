import bs4
import csv
import selenium.webdriver as webdriver
# to auto-save images
import urllib.request

from bs4 import BeautifulSoup as soup

likes = []
imgs = []

i = 1

# retreiving the urls
with open('posts.csv') as f:
	csv_reader = csv.reader(f, delimiter=',')
	for row in csv_reader:
		# print(row[0])

		url = row[0]

		# using driver to access website
		driver = webdriver.Chrome('') # NOTE: add location of (chrome) driver
		driver.get(url)


		# getting page source
		page = soup(driver.page_source, 'html.parser')

		# getting likes and image url
		like = page.find('div', {'class':'Nm9Fw'}).span.text
		likes.append(like)

		img_url = page.find('div', {'class':'KL4Bh'}).img['src']
		imgs.append(img_url)

		# saving image to local machine
		urllib.request.urlretrieve(img_url, '' + str(i) + '.jpg') # file url, local_path
		i += 1

print(likes)
print(imgs)