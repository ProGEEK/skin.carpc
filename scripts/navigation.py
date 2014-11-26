import os
import xbmc

xbmc.executebuiltin('XBMC.Minimize');
os.system("/usr/bin/navigation-engine");
xbmc.executebuiltin('XBMC.Maximize');