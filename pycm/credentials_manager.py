"""
credentials_manager.py

Credential manager for pycm. Load, store (globally), and
automagically update credentials given response TTL seconds.

Usage:

>>> import credential_manager as cm
>>> print(cm.token)
>>> print(cm.refreshtoken)
>>> print(cm.expires_in) # gives actual seconds to expiry as integer
>>> print(cm.scope)

Note:

expires_in global variable here IS NOT a string, as is required for 
the api queries; here it is the actual representative TTL count since
our last refresh. **Don't forget to str(expires_in)** for API use.
"""

import time
import pycm.credentials as credentials
import pycm.background as background


@property
def token(string):
    return string

@property
def refreshtoken(string):
    return string

@property
def expires_in(string):
    return str(int(string))

@property
def scope(string):
    return string


def UpdateCredentials():
    global token, refreshtoken, expires_in, scope, _starttime
    credentials.Update()
    newdata = credentials.Load()
    token = newdata['token']
    refreshtoken = newdata['refreshtoken'] # refresh_token?
    expires_in = newdata['expires_in'] 
    scope = newdata['scope'] 


@background.task
def TimedLoop():
    while True:
        sleep(3601) # an extra second, just in case ;-)
        UpdateCredentials()


# INIT globals
credentials.Update() # first refresh our credentials
_data = credentials.Load() # load new data
token = _data['token']
refreshtoken = _data['refreshtoken']
expires_in = _data['expires_in']
scope = _data['scope']


# run the loop until the program quits
TimedLoop()
