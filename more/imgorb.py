import numpy as np
import cv2

img1 = cv2.imread('cameraman.png', 0) # Original image - ensure grayscale
img2 = cv2.imread('cameraman_rot55.png', 0) # Rotated image - ensure grayscale

# Create ORB detector with 1000 keypoints with a scaling pyramid factor
# of 1.2
orb = cv2.ORB(1000, 1.2)

# Detect keypoints of original image
(kp1,des1) = orb.detectAndCompute(img1, None)

# Detect keypoints of rotated image
(kp2,des2) = orb.detectAndCompute(img2, None)

# Create matcher
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# Do matching
matches = bf.match(des1,des2)

# Sort the matches based on distance.  Least distance
# is better
matches = sorted(matches, key=lambda val: val.distance)

# Show only the top 10 matches - also save a copy for use later
out = drawMatches(img1, kp1, img2, kp2, matches[:10])
