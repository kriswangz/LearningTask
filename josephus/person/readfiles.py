import abc

# ReadFiles is a abstract base class, implmented in entities level.
# Sub class of ReadFiles must implement read function or errors would occur.
class ReadFiles(metaclass=abc.ABCMeta):

    @abc.abstractclassmethod
    def read(self, path, filename, mode='r'):
        raise NotImplementedError