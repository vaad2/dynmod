# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import get_model
from django.utils.datastructures import SortedDict
from django.utils.translation import gettext_lazy as _

# Create your models here.
# class Go(models.Model):
#     name = models.CharField(verbose_name=_('name'), max_length=255)
#     paycheck = models.PositiveIntegerField(verbose_name=_('paycheck'))
#     date_joined = models.DateField(verbose_name=_('date joined'))
#
import six


def dyn_init():
    gl = globals()
    # if hasattr(gl, '__serialize__init__'):
    #     return

    from django.contrib import admin

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
            - {id: spots, title: Вместимость, type: int}
            - {id: department, title: Отдел, type: char}
    '''
    yml_to_orm = {
        'char' : [models.CharField, {'max_length':255}],
        'int' : [models.PositiveIntegerField, {}],
        'date' : [models.DateTimeField, {}]
    }

    docs = yaml.load_all(data)

    for doc in docs:
        for key, item in doc.iteritems():
            model_attrs = SortedDict()
            model_fields = []
            for field in item['fields']:
                mp = yml_to_orm[field['type']]
                field_attrs = dict(mp[1].items() + {'verbose_name' : field['title']}.items())
                model_attrs[field['id']] = mp[0](**field_attrs)
                model_fields.append(field['id'])


            # model_attrs['Meta'] = type('Meta', (), {'fields' : model_fields })
            model_attrs['__module__'] = 'frontend.models'

            gl[key] = type(key, (models.Model,), model_attrs)

            admin.site.register(gl[key])
            print key, item
            print '***' * 40


    # gl['__serialize__init__'] = True

def dyn_init_2():
    gl = globals()

    # if hasattr(gl, '__serialize__init__'):
    #     return

    from django.contrib import admin

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
            - {id: spots, title: Вместимость, type: int}
            - {id: department, title: Отдел, type: char}
    '''

    from django.db.models import base


    docs = yaml.load_all(data)

    class ExM(base.ModelBase):
        def __new__(cls, name, bases, attrs):
            return super(ExM, cls).__new__(cls, attrs['__real__name__'], bases, attrs)

    for doc in docs:
        for key, item in doc.iteritems():

            class Temp(models.Model):
                __real__name__ = key
                __module__ = 'frontend.models'

                for field in item['fields']:
                    if field['type'] == 'char':
                        locals()[field['id']] = models.CharField(verbose_name=field['title'], max_length=255)

                    if field['type'] == 'int':
                        locals()[field['id']] = models.PositiveIntegerField(verbose_name=field['title'])

                    if field['type'] == 'date':
                        locals()[field['id']] = models.DateField(verbose_name=field['title'])

                __metaclass__ = ExM

            gl[key] = Temp
            admin.site.register(gl[key])
    gl['__serialize__init__'] = True


dyn_init_2()


