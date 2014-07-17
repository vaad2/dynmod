# -*- coding: utf-8 -*-
import os
import StringIO
import pprint


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dynmod.settings")
from frontend import models

from frontend import models

from django.core import serializers
# from django.core.management.commands.syncdb import Command
from django.utils.datastructures import SortedDict

def tt():
    import yaml
    data ='''
    users:
        title: Пользователи
        fields:
            - {id: name, title: Имя, type: char}
            - {id: paycheck, title: Зарплата, type: int}
            - {id: date_joined, title: Дата поступления на работу, type: date}

    rooms:
        title: Комнаты
        fields:
            - {id: department, title: Отдел, type: char}
            - {id: spots, title: Вместимость, type: int}
    '''
    docs = yaml.load_all(data)
    for doc in docs:
        for key, item in doc.iteritems():
            print key, item
            print '***' * 40
    # for obj in serializers.deserialize('yaml', data):
    #     print obj

    class Tt:
        pass


mm = 'jopa'

class Temp:
    for i in xrange(10):
        locals()['jopa_%s' % i] = i

print Temp