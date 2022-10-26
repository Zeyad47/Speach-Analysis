from Blackboard import Blackboard
from threading import Lock
import concurrent.futures

class Controller(Blackboard):
    ## initializing the controller class
    def __init__(self, blackboard):
        self.blackboard = blackboard
        self.sentiments = []
        self.frequency = []
        self.trace = ""
        self.lock = Lock()

    ## start controller method
    def startController(self):
        futures = [None] * len(self.blackboard.knowledgeSources)

        ## using thread pool executor from the concurrent.futures library
        with concurrent.futures.ThreadPoolExecutor() as executor:
            ## checking if the blackboard state is changed or not
            while self.blackboard.state == 'changed':
                ## looping through each of the knowledege sources in the blackboard
                for i in range(len(self.blackboard.knowledgeSources)):  
                    ## if the condition is met for a particular ks, then execute its action              
                    if self.blackboard.knowledgeSources[i].checkCondition():
                        ## adding the trace of the ks which performed the action
                        if (self.blackboard.knowledgeSources[i].kSName == 'GrammarCheckerKS' or self.blackboard.knowledgeSources[i].kSName == 'SpellCheckKS'):
                            self.trace = self.trace + self.blackboard.knowledgeSources[i].kSName + " updated the blackboard \n"
                        else:
                            self.trace = self.trace + self.blackboard.knowledgeSources[i].kSName + " analyzed the blackboard \n"
                        ## the knowledge sources will be exectued and result stored in the future object
                        futures[i] = executor.submit(self.blackboard.knowledgeSources[i].action, self.lock)
                        if self.blackboard.knowledgeSources[i].kSName == 'FrequencyKS':
                            self.frequency = futures[i].result()
                        elif self.blackboard.knowledgeSources[i].kSName == 'SentimentAnalyKS':
                            self.sentiments = futures[i].result()
                    ## else set the blackboard state as unchanged since no change on the blackboard
                    else:
                        self.blackboard.state = 'unchanged'