from bs4 import BeautifulSoup
import requests
import sys
word = sys.argv[1]
search = f"https://www.google.com/search?q=define+{word}&oq=define+{word}&aqs=chrome.0.69i59.5749j0j9&sourceid=chrome-mobile&ie=UTF-8"
res = requests.get(search)
raw = res.text
soup = BeautifulSoup(res.text, 'html.parser')
#print(soup.prettify())
class_ = "BNeawe s3v9rd AP7Wnd"
foo = soup.find_all("div", {"class":class_})[0]
je = foo.find_all("div",{"class":class_.split()})
for tag in je:
	if tag['class'] == class_.split():
		if not tag.span and not tag.br:
			print(tag.text)