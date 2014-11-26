# Requires custom XBMC with maximise patch

import os
import xbmc

xbmc.executebuiltin('XBMC.Minimize');
os.system("sakura -s -x carpc-update");
xbmc.executebuiltin('XBMC.Maximize');