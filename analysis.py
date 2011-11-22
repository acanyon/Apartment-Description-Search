
import sys
import string
import nltk
from nltk.stem.wordnet import WordNetLemmatizer 
       
def generate_snippet(document, query) :
    "the main function used to generate a snippet"
    print ""
    desc = AptDesc(document)
    terms = SearchTerms(query)
    return desc.rankDesc(terms)

class AptDesc :
    "Apartment description"
    origDesc = ""
    sentences = []
    
    def __init__ (self, desc) :
        self.origDesc = desc
        self.generateSentences()
    
    def generateSentences(self) :
        """ splits desc into a list of sentences.
        split by endToken global variable """
        endToken = ['.', '!', ';', '?']
        wordParts = []
        phrase = ""
#      
#        words = nltk.word_tokenize(self.origDesc)
#         
        for char in self.origDesc :
            if char in endToken :
                phrase = phrase + char
                wordParts.append(Sentence(phrase))
                phrase = ""
            else :
                phrase = phrase + char

        self.sentences = wordParts
        return 
    
    def rankDesc(self, searchTerms):
        "returns highest ranking sentences/phrase"
        
        ave = 0.0
        rankings = []
        for sent in self.sentences :
            sr = sent.rank(searchTerms)
            rankings.append(sr)
            ave += sr[1]
            
        ave = ave / len(rankings)
        
        if ave == 0.0 :
            print "No match found."
            return 
        
        segment = []
        out = False
        lastIndex = -1
        cutIndex = -1
        for i, (sent, rank) in enumerate(rankings) :
            if rank > ave or out:
                out = True
                segment.append((sent, rank))
                if rank > ave : lastIndex = i
            else :
                cutIndex = i

        segment = segment[:lastIndex - cutIndex ]
        section = ""
        for text, rank in segment :
            section = section + " " + text
            
        return section
            
  
class Text :
    "basic text functions. Inherited by Sentence and SearchTerms"
    
    def __init__(self, text) : 
        endToken = ['.', '!', ';', '?', '-', '/']
        
        self.origText = text.strip()
        
        text = text.lower().strip()
        for char in endToken :
            text = text.replace(char, " ")
        token = nltk.word_tokenize(text)
        
        self.tokenized = []
        lmtr = WordNetLemmatizer()
        for word in token :
            self.tokenized.append(lmtr.lemmatize(word))

class Sentence (Text):
    """ does all sentence processing """

    def getSentence (self) :
        return self.origText

    def categorizeText(self) :
        """ splits text into a list of tuples containing a word and its syntactic category.
        Standardizes words by making everything lowercase and singular"""
        
        wordList = []
        lmtr = WordNetLemmatizer()
        for word in self.sentence :
            wordList.append(lmtr.lemmatize(word))
         
        self.sentence =  nltk.pos_tag(wordList)
        return self.sentence
    
    def rank (self, terms):
        n = 0
        for word in terms.tokenized :
            if word in self.tokenized :
                n += 1
            
        return self.origText, n
  
class SearchTerms (Text):
    "search terms class. more could be implemented in the future. for now just the constructor of text used"
    pass
        