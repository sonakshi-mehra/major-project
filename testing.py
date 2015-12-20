import code_for_classification
import string
from sys import argv

script,filename=argv

target = open(filename,'r')

lines = target.readlines()

target_correct = open('correct_output.txt','w')

i=1

for line in iter(lines):
	words = [word for word in line.split()]
	print str(i)+" "+code_for_classification.findClass(words[1:])
	target_correct.write(str(i)+" "+words[0]+"\n")
	i+=1

target.close()
target_correct.close()