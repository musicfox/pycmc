"""
cm.py

Credential manager for pycm. Load, store (globally), and
automagically update credentials given response TTL seconds.

Usage:

>>> import cm
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

credentials.Update() # first refresh our credentials
_credentials_data = credentials.Load() # load new data
_starttime = time.time() # begin tracking seconds

# set the global variables
token = _credentials_data['token']
refreshtoken = _credentials_data['refreshtoken']
expires_in = int(_credentials_data['expires_in']) - (time.time() - _starttime)
scope = _credentials_data['scope']
_tol = 3 # seconds 
# do-while: update the credentials when TTL time has passed + _tol
while True:
    if not expires_in < _credentials_data['expires_in'] + _tol:
        credentials.Update()
        token = _credentials_data['token']
        refreshtoken = _credentials_data['refreshtoken']
        expires_in = int(_credentials_data['expires_in']) - (time.time() - _starttime)
        scope = _credentials_data['scope']
