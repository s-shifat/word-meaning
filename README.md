# word-meaning

### Intro

This is a simple python program which can find out meaning of an english word.
### Mechanism

This program is basically a webscraper. It uses the *define* search keyword, searches in google, then scrapes out the word meaning. Some tweaking is needed. But works quite fine.

### How to use

Using this is pretty straight forward. This is a command line interface program. So all you need is a terminal like bash, powershell or termux.
command: ```shell
python script.py <your-word>```

example: ```bash
../word-meaning $ python script.py oasis
 a fertile spot in a desert, where water is found.
/word-meaning $```

### Limitations

	-  There are some words that by default does not show up with a *define* keyword google search like "define internet*. Probably I need to add a scraper for these patterns.
	
	-  Some words does not just show up like *define potato* shows properly in the google search but does not show up in this program. I have not found the reason yet.

	-  It might also spit out ambigous result if the first google result is a google add.


You are most welcome to add/comtribute to this little project!

### LameFact
I wrote and tested this program entirely in my android phone with Termux installed. I installed git, python and vim in it. Worked fine.
