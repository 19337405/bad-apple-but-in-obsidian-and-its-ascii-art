from PIL.Image import open as imopen
from sys import stdout
from datetime import timedelta
from cv2 import VideoCapture, imencode, resize
from io import BytesIO
import time
UNFINSHED = False
file = open("badapple.md", "w", encoding='utf8')
def I2T(File):
	im = imopen(File)
	(w, h) = im.size
	mim = im.convert("1")
	data = list(mim.getdata())
	counter = 0
	field = True
	for pixel in data:
		if field:
			if pixel > 127: file.write("@")
			else: file.write(".")
		counter = counter + 1
		if counter >= w:
			counter = 0
			if field: file.write("\n\n")
			field = not field
vidcap = VideoCapture('./video.mp4')
success, image = vidcap.read()
while success:
	if not UNFINSHED:
		print("Drawing...")
		I2T(BytesIO(imencode(".jpg", resize(image, (24, 32), interpolation = 3))[1]))
		time.sleep(1 / 10)
		print("Clearing...")
		file = open("badapple.md", "a")
		file.seek(0)  # sets  point at the beginning of the file
		file.truncate()
		vidcap.read()
		vidcap.read()
		success, image = vidcap.read()

file.close()