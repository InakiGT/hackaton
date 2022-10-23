from time import time
import cv2

def watch():
	cap = cv2.VideoCapture(0)

	majinBooClassif = cv2.CascadeClassifier('./interfaces/models/cascade.xml')

	timeout = 10   # [seconds]

	timeout_start = time()

	while time() < timeout_start + timeout:
		test = 0
		if test == 5:
			break
		test -= 1
		
		ret,frame = cap.read()
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		toy = majinBooClassif.detectMultiScale(gray,
		scaleFactor = 5,
		minNeighbors = 91,
		minSize=(70, 78))

		for (x,y,w,h) in toy:
			cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
			cv2.putText(frame,'oreja',(x,y-10),2,0.7,(0,255,0),2,cv2.LINE_AA)

		cv2.imshow('Siguiendo',frame)
		
		if cv2.waitKey(1) == 25:
			break
	cap.release()
	cv2.destroyAllWindows()