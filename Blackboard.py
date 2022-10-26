class Blackboard:
    
    def __init__(self, text):
        self.knowledgeSources = []
        self.text = text
        self.state = ''

    # to register knowledge sources with the blackboard
    def registerKnowledgeSource(self, ks):
        self.knowledgeSources.append(ks)

    # to get the text
    def getText(self):
        return self.text

    # to set the text
    def setText(self, newText, lock):
        # to lock the blackboard (synchronization)
        lock.acquire()
        self.text = newText
        # to indicate that the status of blackboard has changed
        self.state = 'changed'
        # to unlock the blackboard (synchronization)
        lock.release()

