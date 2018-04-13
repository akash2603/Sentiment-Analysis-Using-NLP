import sys
import operator

Count_of_hashtag = 0
previousTag = None
tweets_data = dict()

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		continue

	thisTag, thisCount = data_mapped

	if thisTag in tweets_data.keys():
		tweets_data[thisTag] += int(thisCount)
	else:
		tweets_data[thisTag] = int(thisCount)

sorted_tweet = sorted(tweets_data.items(), key = operator.itemgetter(1), reverse = True)[:20]


for data in sorted_tweet:
	print ("{0}\t{1}".format(data[0], data[1]))
