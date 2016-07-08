

from .languages import LANGUAGES

def detect_language(text, languages=LANGUAGES):
    lan_count = {l['name']:0 for l in languages}  #create dictionary to count words with
    for language in languages: #check each language
        for word in language['common_words']: #iterate through list of common words
            if word in text.split():  #see if common word exists in text
                lan_count[language['name']]+=1 #count the words 
    return max(lan_count, key=lan_count.get) #return language with most common words
        

''' William, we were confused between the languages.py file in the third directory vs the languages dictionary in the 
    test_main.py. It turns out that the tests used BOTH files. I had to look up some common words in german and finish
    the languages.py dictionary. It wasn't much work on google. you can see what the words are that I added. This code does
    what we decided on. I split the text then counted the words from both dictionaries and added added if the word was in the text.
    I returned the max word count from each test. I DID NOT turn this in yet. please add notes or make changes as you see fit. 
    The README file asked us to check for English detection also, so I added another list of english words just to
    make them happy, even though none of the tests had english text. 
    
    side note: I looked at some regex and there's a findall() method that would have worked pretty good here. If you're
    interested in changing some code, that may be a way to do it. Just an idea.
'''

 





