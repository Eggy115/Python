from cv2.cv import *
# Initialize the camera
capture = CaptureFromCAM(0)  # 0 -> index of camera
if capture:     # Camera initialized without any errors
   NamedWindow("cam-test",CV_WINDOW_AUTOSIZE)
   f = QueryFrame(capture)     # capture the frame
   if f:
       ShowImage("cam-test",f)
       WaitKey(0)
DestroyWindow("cam-test")
