from abc import ABCMeta, abstractmethod


class Check(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def para_check(self):
        raise NotImplementedError("Users must implement para_check for their parameters!")