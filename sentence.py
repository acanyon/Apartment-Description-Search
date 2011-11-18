import sys
import nltk
from nltk.stem.wordnet import WordNetLemmatizer 

class Sentence :
   """ does all sentence processing """

   endToken = ['.', '!', ';', '?']

   def __init__(self, text):
      text = text.lower()
      self.sentence = nltk.word_tokenize(text)
   
   def getSentence (self) :
      return self.sentence

   def categorizeText(self) :
      """ splits text into a list of tuples containing a word and its syntactic category.
      Standardizes words by making everything lowercase and singular"""
      
      wordList = []
      lmtr = WordNetLemmatizer()
      for word in self.sentence :
         wordList.append(lmtr.lemmatize(word))
         
      self.sentence =  nltk.pos_tag(wordList)
      return self.sentence

   def sentenceSplit(self) :
      """ splits categorizedText into a list of sentences.
      split by endToken global variable """
      wordParts = []
      phrase = []
         
      for tword in self.sentence :
         w, c = tword
         if w in endToken :
            wordParts.append(phrase)
            phrase = []
         else :
            phrase.append(tword)

      self.sentence = wordParts
      return self.sentence