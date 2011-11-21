import sys
import string
import nltk
from nltk.stem.wordnet import WordNetLemmatizer 

class AptDesc :
    
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
      
        words = nltk.word_tokenize(self.origDesc)
         
        for w in words :
            if w in endToken :
                phrase = phrase + w
                wordParts.append(Sentence(phrase))
                phrase = ""
            else :
                phrase = phrase + " " + w

        self.sentences = wordParts
        return 
    
    def rankDesc(self, searchTerms):
        
        ave = 0.0
        rankings = []
        for sent in self.sentences :
            sr = sent.rank(searchTerms)
            rankings.append(sr)
            ave += sr[1]
            
        ave = ave / len(rankings)
        
        segment = []
        out = False
        lastIndex = -1
        for i, (sent, rank) in enumerate(rankings) :
            print rank, ave
            if rank >= ave or out:
                out = True
                segment.append((sent, rank))
                if rank >= ave : lastIndex = i
                print i
                
        print i
                
        print segment[:lastIndex]
                    
        
        
            
  
class Text :
    "basic text functions. Inherited by Sentence and SearchTerms"
    
    def __init__(self, text) : 
        self.origText = text.strip()
        text = text.lower().strip()
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
    pass

