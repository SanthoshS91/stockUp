from parse_seekingalpha import getNewsArticles
from symbol_lookup import symbolLookUp
from parse_stocktwits import parseStockTwits
from sentiment_analysis import getSentiment
from stockvalue import getStockValue
from historicalData import gethistoricalStockValues



# print getNewsArticles('FB')
# print ''
# print symbolLookUp('facebook')
# print ''
# print parseStockTwits('FB')


try:
	input_var = raw_input("Enter company name OR ticker symmbol: ")
	ticker = symbolLookUp(input_var)
	getStockValue(ticker)
	newsArticles = getNewsArticles(ticker)
	tweets = parseStockTwits(ticker)
	data = tweets + newsArticles
	sentiment = getSentiment(data)
	print "General attitude towards company: " + sentiment
	print ''
	gethistoricalStockValues(ticker)
except:
	print 'Could not fetch data'