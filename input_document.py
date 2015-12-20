from nltk import word_tokenize  #punctuation not accurate
from nltk.tokenize import RegexpTokenizer
from nltk.stem import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import code_for_classification
import string
from sys import argv

sys,argv=argv #filename to be classified in the command line
text = open(argv,'r').read()

### Initialize tokenizer, stopset, stemmer and lemmatizer ###
tokenizer = RegexpTokenizer(r'\w+')  #used this because this regex gets rid of punctuations al well....alternativly word_tokenize could also have been used
stopset = set(stopwords.words('english'))
porter_stemmer=PorterStemmer()
#lemm = WordNetLemmatizer()
#stemmer = SnowballStemmer('english')
##################################################



tokens = tokenizer.tokenize(text) #tokenize the text

tokens = list(set(tokens))   ##doubt about this in the algorithm

#tokens = [stemmer.stem(w) for w in tokens if not w in stopset] #stem the tokens and remove stop words

#tokens = [lemm.lemmatize(w,'v') for w in tokens]

tokens = [porter_stemmer.stem(w) for w in tokens if not w in stopset]

print tokens

print code_for_classification.findClass(tokens)