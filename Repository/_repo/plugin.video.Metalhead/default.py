# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Thanks to the Authors of the base code
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#
# modified by: ILoveSlam
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.Metalhead'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "LoudwireMusic" 							#Loudwire
YOUTUBE_CHANNEL_ID_2 = "PLvXmarOi5xICV0X4HfMH7S29EpvDpTQgd" 	#Wikipedia Fact or Fiction
YOUTUBE_CHANNEL_ID_3 = "PLvXmarOi5xICqisBHpBmnpiQoNljd5ohS" 	#Loudwire Interviews
YOUTUBE_CHANNEL_ID_4 = "MetalHammerTV" 							#MetalHammer
YOUTUBE_CHANNEL_ID_5 = "MetalHammerTV/videos" 					#Metalhammer Uploads
YOUTUBE_CHANNEL_ID_6 = "PitCamProduction"						#Pitcam TV
YOUTUBE_CHANNEL_ID_7 = "PL202C9E6689E59604"						#Pitcam Interviews 

# Entry point
def run():
    plugintools.log("docu.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("docu.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="Loudwire",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://yt3.ggpht.com/-0HgaBbAv914/AAAAAAAAAAI/AAAAAAAAAAA/iMtX0zs7KoA/s200-c-k-no-mo-rj-c0xffffff/photo.jpg",
		fanart="http://loudwire.com/files/2016/12/Most-Devoted-Fans-6th-Annual-LMA.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Wikipedia Fact or Fiction",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://i.ytimg.com/vi/FtFSAMw-GBw/maxresdefault.jpg",
		fanart="https://i.ytimg.com/vi/GKm2eQ7XftM/maxresdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Loudwire Interviews",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="http://i3.ytimg.com/vi/0EfRYGcEIUE/maxresdefault.jpg",
		fanart="https://i.ytimg.com/vi/d9jqCVNK2ZI/hq720.jpg",
        folder=True )

		
run()plugintools.add_item( 
        #action="", 
        title="MetalHammer",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://yt3.ggpht.com/-H4gPGFMI0vY/AAAAAAAAAAI/AAAAAAAAAAA/yiUdYkhqX1M/s200-c-k-no-mo-rj-c0xffffff/photo.jpg",
		fanart="",
        folder=True )
		
		plugintools.add_item( 
        #action="", 
        title="Metalhammer Uploads",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="http://i3.ytimg.com/vi/soNpZYIfNNE/maxresdefault.jpg",
		fanart="http://3.bp.blogspot.com/-dGdKJnfAge0/UD7BMhl5kpI/AAAAAAAAAG0/K1QySiN-gfo/s1600/1345444213.jpg",
        folder=True )

		plugintools.add_item( 
        #action="", 
        title="Pitcam TV",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://yt3.ggpht.com/-9abntThr7ZI/AAAAAAAAAAI/AAAAAAAAAAA/B_6ohkFWNxo/s200-c-k-no-mo-rj-c0xffffff/photo.jpg",
		fanart="http://www.konbini.com/fr/files/2013/02/Mosh-Pit-at-Endfest.jpg",
        folder=True )

		plugintools.add_item( 
        #action="", 
        title="Pitcam Interviews ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="http://i3.ytimg.com/vi/OV0qgf7RuXo/maxresdefault.jpg",
		fanart="https://i.ytimg.com/vi/2FDRic7_nh4/maxresdefault.jpg",
        folder=True )
        #action="", 
        title="",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="",
		fanart="",
        folder=True )

