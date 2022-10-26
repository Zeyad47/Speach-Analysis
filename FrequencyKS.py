from AbstractKS import AbstractKS
from Blackboard import Blackboard

# to import textblob lib
from textblob import TextBlob

class FrequencyKS(AbstractKS):

    def __init__(self, blackboard):
        self.blackboard = blackboard
        self.processedTextBefore = ""
        self.kSName = 'FrequencyKS'

    def checkCondition(self):
        current = self.blackboard.getText()
        corrected = TextBlob(current).correct()
        # Check whether the words within the current text are spelled correctly
        if(current == corrected):
            return True
        # Check whether the text have been processed before
        if(current != self.processedTextBefore):
            return True
        else:
            return False

    def action(self, lock):
        current = self.blackboard.getText()
        blob = TextBlob(current)

        # creating a list to store the character, word and sentence frequency of the current text
        frequency = []

        # Remove all the whitespaces from the string and count character frequency within current text
        characterFrequency = len(current.replace(" ", ""))
        # Count word frequency within current text
        wordFrequency = len(blob.words)
        # Count sentence frequency within current text
        sentenceFrequency = len(blob.sentences)

        # First number within the frequency list will have character frequency
        # Second number within the frequency list will have word frequency
        # Third number within the frequency list will have the sentence frequency
        frequency = [characterFrequency,wordFrequency,sentenceFrequency]

        # Save current processed text so it wont run again when the condition is ran
        self.processedTextBefore = current

        return frequency