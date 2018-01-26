from timmytimer import timmy, timmyp, timmyprint
import logging
from time import sleep
from random import random

@timmy
def test_timmy(greeting, name='Henrik'):
    sleep(random())
    print('{} {}'.format(greeting, name))

@timmyprint
def test_timmyprint(greeting, name='Henrik'):
    sleep(random())
    print('{} {}'.format(greeting, name))

@timmyp
def test_timmyp(greeting, name='Henrik'):
    sleep(random())
    print('{} {}'.format(greeting, name))


if __name__ == '__main__':
    log = logging.getLogger()
    log.setLevel(logging.DEBUG)

    test_timmy('Hello', name='Gustav')
    test_timmyprint('Goodday', name='Ellinor')
    test_timmyp('P-man')
