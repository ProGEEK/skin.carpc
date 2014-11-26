# Requires custom XBMC with maximise patch

import os
import xbmc

xbmc.executebuiltin('XBMC.Minimize');
os.system("mono /usr/bin/RouterMode.exe");
xbmc.executebuiltin('XBMC.Maximize');