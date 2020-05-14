"""
Credential manager for pycm. Load, store (globally), and
automagically update credentials given response TTL seconds.

> &#57938; You probably shouldn't do anything with this manually!
> All you need to do is set your `CMCREDENTIALS` environment variable to
> your JSON string of your Chartmetric API token.

##### Usage:
```python
>>> import credential_manager as cm
>>> print(cm.token)
>>> print(cm.refreshtoken)
>>> print(cm.expires_in) # gives actual seconds to expiry as integer
>>> print(cm.scope)
```
> Note:
>
> The `expires_in` global variable here IS NOT a string, as is required for 
> the api queries; here it is the actual representative TTL count since
> our last refresh. **Don't forget to str(expires_in)** for API use.
"""

import time
import os

from . import credentials
from . import background


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


# INIT globals
credentials.Update()  # first refresh our credentials

_data = credentials.Load()  # load new data
token = _data["token"]
refreshtoken = _data["refreshtoken"]
expires_in = _data["expires_in"]
scope = _data["scope"]

# run the loop until the program quits
def UpdateCredentials():
    """
    TODO Write documentation here.
    """
    global token, refreshtoken, expires_in, scope, _starttime
    credentials.Update()
    newdata = credentials.Load()
    token = newdata["token"]
    refreshtoken = newdata["refreshtoken"]  # refresh_token?
    expires_in = newdata["expires_in"]
    scope = newdata["scope"]


@background.task
def TimedLoop():
    """
    TODO Write documentation here.
    """
    while True:
        sleep(
            3000
        )  # api calls can be inconsistent so using conservative 3000 vs 3600
        UpdateCredentials()


TimedLoop()
