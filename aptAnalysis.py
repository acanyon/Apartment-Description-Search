#!/usr/bin/env python

import sys
import nltk
from nltk.stem.wordnet import WordNetLemmatizer 


exampleText = """Our luxury loft-style apartments were constructed as condominiums, so
your new residence will have: Solid floors and walls (this will be the
quietest apartment you've EVER lived in); Premium stainless steel
designer appliances; Distinctive accent walls and hardwood flooring; A
kitchen that most chefs would drool over with easy to clean gas stove
and countertops; Walk in closets with built in storage; Full size
washer and dryer in each apartment home. In addition, all residents
will enjoy use of our top-notch amenities, including reserved parking,
cutting-edge fitness center, wireless internet cafe/business center,
and rooftop lounge to soak up the sun!"""

endToken = ['.', '!', ';', '?']


def categorizeText(text) :
   """ splits text into a list of tuples containing a word and its syntactic category.
   Standardizes words by making everything lowercase and singular"""
   text = text.lower()
   tokenized = nltk.word_tokenize(text)

   wordList = []
   lmtr = WordNetLemmatizer()
   for word in tokenized :
      wordList.append(lmtr.lemmatize(word))

   tokenized =  nltk.pos_tag(wordList)
   return tokenized

def sentenceSplit(catText) :
   """ splits categorizedText into a list of sentences.
   split by endToken global variable """
   wordParts = []
   phrase = []

   for tword in catText :
      w, c = tword
      if w in endToken :
         wordParts.append(phrase)
         phrase = []
      else :
         phrase.append(tword)
   
   return wordParts



if len(sys.argv) <= 1 :
   print "Please supply file apt description input"
   exit()

searchTerms = raw_input("search :  ")
searchTerms = categorizeText(searchTerms)

print searchTerms

# for each input file, do analysis
for i in range(1, len(sys.argv)) :
   descFile = open(sys.argv[i])

   print sys.argv[i], " : "
   for line in descFile.readlines() :
      catText = categorizeText(line)
      sentences = sentenceSplit(catText)

      for set in sentences :
         print set

