from AbstractKS import AbstractKS

# to import textblob lib
from textblob import TextBlob

class SpellingCheckerKS(AbstractKS):
    
    def __init__(self, blackboard):
        self.blackboard = blackboard
        self.kSName = 'SpellCheckKS'

    # this function checks if the blackboard has spelling mistakes
    def checkCondition(self):
        current = self.blackboard.getText()
        corrected = TextBlob(current).correct()
        if(current == corrected):
            self.blackboard.state = 'unchanged'
            return False
        else:
            return True

    # this function performs the spelling correction
    def action(self, lock):
        current = self.blackboard.getText()
        corrected = TextBlob(current).correct()
        self.blackboard.setText(str(corrected), lock)
        self.blackboard.state = 'changed'
        return True
        