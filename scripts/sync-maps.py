# Requires custom XBMC with maximise patch

import os
import xbmc

xbmc.executebuiltin('XBMC.Minimize');
os.system("sakura -s -x \"map-sync\"");
xbmc.executebuiltin('XBMC.Maximize');