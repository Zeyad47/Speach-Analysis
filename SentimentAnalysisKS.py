from AbstractKS import AbstractKS
from textblob import TextBlob

class SentimentAnalysisKS(AbstractKS):

    def __init__(self, blackboard):
        self.blackboard = blackboard
        self.processedTextBefore = ''
        self.kSName = 'SentimentAnalyKS'

    def checkCondition(self):
        current = self.blackboard.text
        if(current != self.processedTextBefore):
            return True
        else:
            return False
    
    # this function performs the sentiment analysis
    def action(self, lock):
        current = self.blackboard.text
        blob = TextBlob(current)
        analysis = blob.sentiment
        
        # creating a list to store the percentages of the sentiment values
        # first number in the list will be the positive sentiment, second number is the negative sentiment
        sentiments = []
        if(analysis.polarity < 0):
            sentiments = [round(analysis.polarity * -1, 3), round(1 - (analysis.polarity * -1), 3)]
        else:
            sentiments = [round(analysis.polarity, 3) , round(1 - analysis.polarity, 3)]

        # Save current processed text so it wont run again when the condition is ran
        self.processedTextBefore = current

        return sentiments
