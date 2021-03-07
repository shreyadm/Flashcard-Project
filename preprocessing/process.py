import pandas

data = pandas.read_csv('wordsWithFrequency.txt', delimiter=" ")
data.to_csv('data.csv')