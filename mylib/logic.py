import wikipedia

def wiki(name="War Goddess", length=1):
    my_wiki = wikipedia.summary(name, length)
    return my_wiki

def wiki_search(name="War"):
    result = wikipedia.search(name)
    return result