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
.../word-meaning $ python main.py ablaze            

ABLAZE

Meaning-1:
   adjective                                            lighted up by or as by fire or flame
   Example: “forests set ablaze (or afire) by lightning”

Meaning-2:
   adjective
    resembling flame in brilliance or color
   Example: “maple trees ablaze in autumn”

Meaning-3:
   adjective
    lighted with red light as if with flames
   Example: “streets ablaze with lighted Christmas trees”

Meaning-4:
   adjective
    keenly excited (especially sexually) or indicating excitement
   Example: “"his face all ablaze with excitement"- Bram Stoker”

USAGE:
    Use the adjective ablaze to describe something that's on fire. Once your campfire is ablaze, you cantoast marshmallows over it.

.../word-meaning $
```

### Limitations

One limitation is that I haven't added the functionality to deal with a typo. I will add this some time soon. Not to mention: **you are warmly welcome to add/comtribute to this little project!**


### Motivation

I built up this simple program for two reasons:
1. To revisit the OOP and webscraping concepts using python.

2. This happens to me quite frequently: I search for a word in the internet, then somehow 30 minutes later I find my self watching videos on youtube about how to pour water into a glass. You get the idea. Hopefully this little CLI program will keep me away from the clutter of the internet. 

### LameFact
I wrote and tested this program entirely in my android phone with Termux installed. I installed git, python and vim in it. Worked fine.
