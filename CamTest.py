#All changed must be made in the pi version

from goprocam import GoProCamera
from goprocam import constants
import time

gpCam = GoProCamera.GoPro(constants.auth)
time.sleep(4)
gpCam.mode(constants.Mode.PhotoMode)
time.sleep(2)
for i in range(3):
	gpCam.downloadLastMedia(gpCam.take_photo())
	time.sleep(10)
gpCam.power_off()


"""
Tip:
Changing network on mac is done like this in the command line:
networksetup -setairportnetwork en0 _WiFiNAME_ _Password_
ex: networksetup -setairportnetwork en0 LosAngeles-LAX Rabarbersuppe85
Der er en fucking typo i wifinavnet

"""