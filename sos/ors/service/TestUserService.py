import os
import sys
import django
import datetime
from UserService import UserService

sys.path.append("C:/Users/LENOVO/OneDrive/Desktop/Django/sos")

# Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sos.settings")
django.setup()


def testadd():
    params = {
        'firstName': 'Manthan',
        'lastName': 'Bhawsar',
        'loginId': 'man123',
        'password': 'abc',
        'dob': datetime.date(2005, 7, 10),
        'address': 'Delhi'
    }
    service = UserService()
    service.add(params)

# def testupdate():
#     params = {
#         'firstName': 'Joshua',
#         'lastName': 'Mathew',
#         'loginId': 'josh123',
#         'password': 'chris',
#         'dob': datetime.date(2006, 6, 6),
#         'address': 'Delhi'
#         'id': 2
#     }
#     service = UserService()
#     service.update(params['firstname'], params['lastName'], params['loginId'], params['password'], params['dob'], params['address'], params['id'])

def testdelete():
    params = {
        'id': 2
    }
    service = UserService()
    service.delete(params['id'])

def testauth():
    params = {
        'loginId': 'man123',
        'password': 'abc'
    }

    service = UserService()
    service.auth(params['loginId'], params['password'])

def testget():
    params = {
        'id': 2
    }
    service = UserService()
    service.get(params['id'])

def testfindByLogin():
    params = {
        'loginId': 'man123',
    }
    service = UserService()
    service.findByLogin(params['loginId'])


#testadd()
#testupdate()
#testdelete()
#testauth()
#testget()
#testfindByLogin()
