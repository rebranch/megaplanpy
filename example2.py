#-------------------------------------------------------------------------------
# Name:        example
# Purpose:
#
# Author:      Sergey Pikhovkin (s@pikhovkin.ru)
#
# Created:     04.02.2011
# Copyright:   (c) Sergey Pikhovkin 2011
# Licence:     MIT
#-------------------------------------------------------------------------------
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from megaplanpy import Megaplan


CODE = 'utf-8'

def PrintDict(D):
    tmpl1 = '{0}: {1}'
    tmpl2 = '    {0}: {1}'
    for key, value in D.iteritems():
        if isinstance(value, dict):
            print('{0}:'.format(key))
            for k, v in value.iteritems():
                if isinstance(v, (str, unicode)):
                    print(tmpl2.format(k, v.encode(CODE)))
                else:
                    print(tmpl2.format(k, v))
        else:
            if isinstance(value, (str, unicode)):
                print(tmpl1.format(key, value.encode(CODE)))
            else:
                print(tmpl1.format(key, value))

def main():
    account = 'my_account'
    login = 'my_login'
    password = 'my_password'
    self_id = '0000000' # <-- input self Id

    create_task = False
    edit_task = False

    mplan = Megaplan(account, login, password)


    # Добавление клиента
    print('Payer create')
    params = {
        'Model[Name]': 'New task',

        'Model[TypePerson]': 'human', #	string	Тип клиента, принимает значения: human и company
        'Model[FirstName]' : u'sdfsdf', 	# string	Имя, обязательное если тип human
        'Model[LastName]': u'wer', #	string	Фамилия, обязательное если тип human
        'Model[MiddleName]': u'sdfsd',#	string	Отчество, обязательное если тип human
        #        Model[CompanyName]	string	Наименование компании, обязательное если тип company
        #        Model[ParentCompany]	int	Id компании, используется для связи контактного лица с компанией
        'Model[Email]': 'test@sdfsdfserwef.ru', #	string	Email
        #'Model[Phones]': [{'79565467864'},],	#array	Массив телефонов*
        #        Model[Birthday]	array	День основания компании или день рождения клиента, формат: Y-m-d (Пример: '1999-03-27')
        #        Model[Responsibles]
        #'Model[Deadline]': '2011-02-05 12:00',
        #'Model[DeadlineDate]': '2011-02-05',
        #'Model[DeadlineType]': 'soft',
        'Model[Responsible]': self_id, # <-- input self Id Идентификаторы ответственных сотрудников перечисленных через запятую (Пример: '1000005,1013202')

        #'Model[Executors]': '0',
        #'Model[Auditors]': '0',
        #'Model[Severity]': '1',
        #'Model[SuperTask]': '0',
        #'Model[Customer]': '0',
        #'Model[IsGroup]': '0',
        #'Model[Statement]': 'Create new task from Python'
    }

    obj = mplan.Contractor(**params).data

    print obj

    # Добавление сделки
    payer_id = obj['contractor']['PayerId']

    params = {
        'ProgramId': 3, # Выбор дерева решений
        'Model[Contractor]': payer_id,
    }
    obj = mplan.Deal(**params).data
    print obj



if __name__ == '__main__':
    main()
