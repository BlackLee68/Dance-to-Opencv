"""
Author: lixiawei
Data: 20200625
Introduction: using opencv to read your computer's camera, there are some interesting
              questions
"""
import cv2
import numpy
import time

class CameraTest:
    def __init__(self):
        pass

    def testFunc(self, buffer_size, wait_time, show_flag, sleep_time):
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("camera is not open!")
            cap.open(0)
        cap.set(cv2.CAP_PROP_BUFFERSIZE, buffer_size)
        while 1:
            start = time.time()
            ret, frame = cap.read()
            end = time.time()
            print("read time: ", end - start, " s.")
            if not ret:
                print("Get empty frame!")
                continue
            time.sleep(sleep_time)
            if show_flag:
                cv2.imshow("cap", frame)
                if cv2.waitKey(wait_time) & 0xff == ord("q"):
                    break
        cap.release()
        if show_flag:
            cv2.destroyAllWindows()

if __name__ == "__main__":
    Test = CameraTest()
    Test.testFunc(1, 10, True, 0)



