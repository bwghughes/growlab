import picamera
import io
import time
from subprocess import call


# class camera:
#     def __init__(self, camera_opts):
#         self.camera_opts = camera_opts
# 
#     def get_frame(self):
#         stream = io.BytesIO()
#         with picamera.PiCamera() as camera:
#             camera.start_preview()
#             camera.vflip = self.camera_opts["vertical_flip"]
#             camera.hflip = self.camera_opts["horizontal_flip"]
#             camera.meter_mode = self.camera_opts["meter_mode"]
#             camera.exposure_mode = "auto"
#             camera.resolution = (self.camera_opts["width"], self.camera_opts["height"])
#             # Camera warm-up time
#             time.sleep(self.camera_opts["preview_seconds"])
#             camera.capture(stream, format=self.camera_opts["encoding"], quality=self.camera_opts["image_quality"])
# 
#         return stream
        
        
class camera:
    def __init__(self, opts):
        self.camera_opts = opts
        
        
    def get_frame(self):
        """ fswebcam -r 1280x720 image2.jpg """
        call(["fswebcam", "-r", "1280x720", "--set", "brightness=20%", "images/image.jpg"])
        time.sleep(2)
        with open("images/image.jpg", 'rb') as fh:
            buf = io.BytesIO(fh.read())
        
        return buf
