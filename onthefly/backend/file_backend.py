import json
from onthefly.backend import AbstractBackend
from redis import Redis


class FileBackend(AbstractBackend):
    def __init__(self, options, **kwargs):
        file_name = "filebackendstorage.ini"
        try:
            file_storage = open(file_name,'r')
        except IOError:
            file_storage = open(file_name, 'w')
        self.file_storage = file_storage
        super(FileBackend, self).__init__(options, **kwargs)

    def set(self, name, value):
        #DEBUG=True
        record = '%s:%v' % (name,value)
        self.file_storage.write()


