from . import credentials

# set the creds dir to HOME

import os

credentials.CredentialsDir = os.path.join(
    os.environ.get("HOME"), ".pycm", ".credentials.json"
)
from . import credentials_manager
from .charts import (
    youtube, applemusic, spotify, shazam, soundcloud, beatport,
    itunes, youtube,
)
from . import track
from . import album
from . import artist
from . import utilities
from . import curator
from . import playlist
#from .
#from .
#from .
#from .
#from .
#from .
#from .
#from .
#
#import pycm.charts.applemusic
#import pycm.charts.beatport
#import pycm.charts.itunes
#import pycm.charts.shazam
#import pycm.charts.soundcloud
#import pycm.charts.spotify
#import pycm.charts.youtube
#
#import pycm.track
#import pycm.album
#import pycm.artist
#
#import pycm.utilities
#import pycm.background
#import pycm.curator
#import pycm.playlist
