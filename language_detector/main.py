

from .languages import LANGUAGES

def detect_language(text, languages=LANGUAGES):
    lan_count = {l['name']:0 for l in languages}  #create dictionary to count words with
    for language in languages: #check each language
        for word in language['common_words']: #iterate through list of common words
            if word in text.split():  #see if common word exists in text
                lan_count[language['name']]+=1 #count the words 
    return max(lan_count, key=lan_count.get) #return language with most common words
        



 





