import abc


class AbstractKS(object):
    
    __metaclass__ = abc.ABCMeta

    def __init__(self, blackboard):
        self.blackboard = blackboard

    @abc.abstractproperty
    def checkCondition(self):
        raise NotImplementedError('Must provide implementation in subclass.')

    @abc.abstractmethod
    def action(self, lock):
        raise NotImplementedError('Must provide implementation in subclass.')