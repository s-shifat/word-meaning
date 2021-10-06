# word-meaning

### Intro

This is a simple python program which can find out meaning of an english word.
### Mechanism

This program is basically a webscraper.
You pass a word to this program, then it scrapes [this website](https://www.vocabulary.com/dictionary/)
and finds out the meaning of the word.

### How to use

Using this is pretty straight forward. This is a command line interface program. So all you need is a terminal like bash, powershell or termux with python 3x  installed.
Command:
```bash`
python main.py [your-word-here]
```
Or,

```bash
sh word.sh [your-word-here]
```

Sample Execution:
```console
ZEAL

Meaning-1:
   noun
    a feeling of strong eagerness (usually in favor of a person or cause)
   Example: “he felt a kind of religious zeal”

Meaning-2:
   noun
    prompt willingness
   Example: “they disliked his zeal in demonstrating his superiority”

Meaning-3:
   noun
    excessive fervor to do something or accomplish some end
   Example: “he had an absolute zeal for litigation”

USAGE:
    Zeal is dedication or enthusiasm for something. If you have zeal, you're willing, energized, and motivated.

.../Python_Projects/word-meaning $
```

### Limitations

One limitation is that I haven't added the functionality to deal with a typo. I will add this some time soon. Not to mention: **you are warmly welcome to add/comtribute to this little project!**


### Motivation

I built up this simple program for two reasons:
1. To revisit the OOP and webscraping concepts using python.

2. This happens to me quite frequently: I search for a word in the internet, then somehow 30 minutes later I find my self watching videos on youtube about how to pour water into a glass. You get the idea. Hopefully this little CLI program will keep me away from the clutter of the internet. 

### LameFact
I wrote and tested this program entirely in my android phone with Termux installed. I installed git, python and vim in it. Worked fine.
