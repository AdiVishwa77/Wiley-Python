from pathlib import Path
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer() 
import json


nltk.download('stopwords')
 
nltk.download('wordnet')

def readTextPath(file_Path):
            f=open(file_path,'r')
            words=str(f.read())
            print(words)
def split_text(file_path):
            f=open(file_path,'r')
            words=str(f.read())
            words=words.split()
            print(words)
def rmStopWords(words):
            f=open(file_path,'r')
            words=str(f.read())
            words=words.split()
            SW = set(stopwords.words('english'))
            words_clean=[]
            for i in words:
                if i not in SW:
                    words_clean.append(i)
            print(words_clean)
            lemmatize_words(words_clean)
def lemmatize_words(a):
        count =0
        l=[]
        for word in a:
            lemmatizer = WordNetLemmatizer()
            words_lemmatized = lemmatizer.lemmatize(word)
            if words_lemmatized != word:
                    l.append(words_lemmatized)
            else:
                pass
        print("The Lemmatized words are: ",l)
        compute_frequency_words(l)

def compute_frequency_words(b):
        frequency = {}
        for word in b:
            frequency[word] = b.count(word)
        print(type(frequency))
        print(frequency)
        save_words_frequency(frequency,file_path="data/words_frequency.json")

def save_words_frequency(f,file_path="data/words_frequency.json"):
        with open('words_frequency', 'w') as outfile:
            json.dump(f,outfile)
            
file_path=input("enter a path: ")
readTextPath(file_path)
split_text(file_path)
rmStopWords(file_path)
    




