from sys import argv
from math import log
import MySQLdb

def read_words(words_file):
    return [word for line in open(words_file, 'r') for word in line.split()]

script,filename = argv

target = read_words(filename)
db = MySQLdb.connect("localhost","root","cic","naive" )
cursor = db.cursor()


sql = "select * from probability_class"
cursor.execute(sql)
resultSet=cursor.fetchall()
class_prob={}
for row in resultSet:
	class_prob[row[0]]=row[1]

sql = "select * from probability_word_given_class"
cursor.execute(sql)
resultSet=cursor.fetchall()
prob = {}
for row in resultSet:
	if row[1] not in prob:
		prob[row[1]]={}
	prob[row[1]][row[0]]=row[2]

max_prob = float("-inf")
max_class = ""
for _class in class_prob:
	_prob = log(class_prob[_class])
	for _word in target:
		if _word in prob:
			_prob += log(prob[_word][_class])
	if _prob>max_prob:
		max_prob = _prob
		max_class = _class

print max_class

db.close()
