from bs4 import BeautifulSoup
import requests

def get_meaning(word, verbose=False):
    phrase = f"define+{word}"
    url = "https://www.google.com/search"
    params ={"q":phrase,
            "oq":phrase,
            "aqs":"chrome.0.69i59.5749j0j9",
            "sourceid":"chrome-mobile",
            "ie":"UTF-8"}
    if verbose: print("\rsearching...",end="")
    res = requests.get(url, params)
    soup = BeautifulSoup(res.text, 'html.parser')
    #print(soup.prettify())
    class_ = "BNeawe s3v9rd AP7Wnd"
    outer_class = soup.find_all("div", {"class":class_})[0]
    inner_classes = outer_class.find_all("div",{"class":class_.split()})
    for tag in inner_classes:
        if tag['class'] == class_.split():
            if not tag.span and not tag.br:
                return tag.text

if __name__ == "__main__":
    import sys
    WORD = sys.argv[1]
    meaning = get_meaning(WORD, verbose=True) or "\rSorry, Check Spelling or try again!"
    print("\r", meaning)
