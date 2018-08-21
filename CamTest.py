#All changed must be made in the pi version
#This is a test module

from goprocam import GoProCamera
from goprocam import constants
import time

#Initialize an instance of cam
gpCam = GoProCamera.GoPro(constants.auth)
time.sleep(4)

#Set mode to single photo
gpCam.mode(constants.Mode.PhotoMode)
time.sleep(2)

#Take 3 photos with 10 sec interval to prevent a bird blocking the view etc.
for i in range(3):
	gpCam.downloadLastMedia(gpCam.take_photo())
	time.sleep(10)

#Turn off
gpCam.power_off()


"""
Tip:
Changing network on mac is done like this in the command line:
networksetup -setairportnetwork en0 _WiFiNAME_ _Password_
ex: networksetup -setairportnetwork en0 LosAngeles-LAX Rabarbersuppe85
Der er en fucking typo i wifinavnet

"""