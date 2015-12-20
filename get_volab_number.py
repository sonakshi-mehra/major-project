import MySQLdb
from sys import argv

#take the name of the file containing the training data from command line
script,filename=argv

target = open(filename,'r')

lines = target.readlines()
vocab = []
for line in iter(lines):
	word = line.split()
	vocab=vocab+word[1:]

vocab = list(set(vocab))
print "Vocabulary size : "+str(len(vocab))
while True:
	word = raw_input('Enter word : ')
	try:
		print vocab.index(word)+1
	except Exception as e:
		print e
		print 
