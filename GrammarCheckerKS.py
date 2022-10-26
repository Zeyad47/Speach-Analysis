from AbstractKS import AbstractKS

# import lib
import language_tool_python  

# There is a 10% error margin in this library 

class GrammarCheckerKS(AbstractKS):
    
    # init blackboard & KS
    def __init__(self, blackboard):
        self.Blackboard = blackboard
        self.kSName = 'GrammarCheckerKS'

    # Check Condition (contain grammar errors)
    def checkCondition(self):
        my_tool = language_tool_python.LanguageTool('en-US')  
        current = self.Blackboard.getText()
        grammared = my_tool.correct(current)
        if(current == grammared):
            self.Blackboard.state = 'unchanged'
            return False
        else:
            return True

    # Action (correct grammar)
    def action(self, lock):
        current = self.Blackboard.getText()
        my_tool = language_tool_python.LanguageTool('en-US')  
        grammared_text = my_tool.correct(current)
        self.Blackboard.setText(str(grammared_text), lock)
        self.Blackboard.state = 'changed'
        return True


