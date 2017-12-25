# Timmy
Named after the childrens TV-show Timmy Time
In Norwegian they call it "Timmy time!"

A simple wrapper to log/print functionname, \*args and \**kwargs.

## Example Usage

```
from timmytime import timmy, timmyprint

# set up logger
log.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
log.addHandler(ch)

@timmy  # this goes to logging
def func(greeting, name='Henrik'):
    print('{} {}'.format(greeting, name))

@timmyprint  # this just prints
def funcprint(greeting, name='Henrik'):
    print('{} {}'.format(greeting, name))

func('Hello', name='Gustav')
funcprint('Hello', name='Ellinor')
```

## SETUP
pip install [githublink]

from timmytime import timmy

and then add @timmy above any defined function or procedure
