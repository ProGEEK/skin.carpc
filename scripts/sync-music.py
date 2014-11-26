# Requires custom XBMC with maximise patch

import os
import xbmc

xbmc.executebuiltin('XBMC.Minimize');
os.system("sakura -s -x carpc-sync-music");
xbmc.executebuiltin('XBMC.Maximize');