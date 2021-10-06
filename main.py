#!/usr/bin/env python3

import bs4
from bs4 import BeautifulSoup
import requests

class Formatter:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ITALIC = "\033[3m"
    
    @classmethod
    def format(self,string, *args):
    	formatted_string = ''
    	for arg in args:
    		formatted_string += self().__getattribute__(arg.upper())
    	return formatted_string + string + self().END

class Exracter:
	CLASSES_OF_INTEREST = ["definition","pos-icon", "example"]
	URL = "https://www.vocabulary.com/dictionary/"
	
	def __init__(self, word):
		self.word = word
		self.result = {'word':None,'meanings':[], 'usage':None}
		self.url = self.URL + self.word
		self._response = requests.get(self.url)
		self._soup = BeautifulSoup(self._response.content, 'html.parser')
		self.get_meaning()
		
	@property	
	def fancy_string(self):
		f = Formatter()
		word_rep = f.format(self.result['word'],'header','bold','underline') + '\n'
		usage_rep =f.format('\n\nUSAGE:\n\t','bold','blue') + f.format(self.result['usage'], 'yellow')
		meaning_rep = ''
		for meaning in self.result['meanings']:
			i = meaning['index']
			meaning_rep += f'''
{f.format(f'Meaning-{i+1}:','blue')}
   {f.format(meaning['parts-of-speech'],'italic','cyan')}
	{f.format(meaning['meaning'],'yellow','bold')}
   {f.format("Example:",'green')} {meaning['example']}
'''
		return '\n ' + word_rep + meaning_rep + usage_rep + '\n'
	
	def get_meaning(self):
		self.result['word'] = self._soup.find("div",class_="word-area").h1.text.strip().upper()
		usage = self._soup.find("p", class_="short")
		self.result['usage'] = self.get_text(usage).replace('\n','').strip()
		ol = self._soup.find_all("ol")
		if len(ol) == 1:
			ol = ol[0]
		else:
			print("Problem, exiting...")
			exit()
		i=0
		for li in ol.children:
			_each_meaning = {'index':None,'meaning':None,'parts-of-speech':None,'example':None}
			if type(li) == bs4.element.Tag:
				meaning, pos, example = [li.find(class_=class_) for class_ in self.CLASSES_OF_INTEREST]
				_each_meaning['index'] = i
				pos_str = self.get_text(pos)
				_each_meaning['parts-of-speech'] = pos_str.strip()
				_each_meaning['meaning'] = self.get_text(meaning).replace(pos_str,"").strip()
				_each_meaning['example'] = self.get_text(example).replace("\n",'').strip()
				self.result['meanings'].append(_each_meaning)
				i+=1
	
	@staticmethod
	def get_text(tag_obj):
		if not tag_obj:
			return ""
		else:
			return tag_obj.text
	@staticmethod		
	def verify_querry(soup, word):
		# I will complete ot later
		searched_for = soup.find("div",class_="word-area")
		if searched_for:
				return searched_for.h1.textstrip()
		else:
			pass #ToDo: code to add if user makes a spelling mistake, use autocomplete
		
	
if __name__ == '__main__':
	import sys
	word = sys.argv[1]
	e = Exracter(word)
	print(e.fancy_string)
	# Note: Typo isn't handled yet!