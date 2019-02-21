import cv2
from threading import Thread

def create_instances( source_list ):
    '''
    Create instances of system
    @param get list of sources, int for webcams and str for rtsp
    @param out_array, array of variables for out data
    '''
    thread_list = list()

    if(type(source_list) == type(list())):
        amount = len(source_list)
        for i in range(0, amount):
            if (type(source_list[i]) == type(list()) or (type(source_list[i]) == type(tuple()))):
                thread = Camera( address=source_list[i][0], name=source_list[i][1],
                visualize = source_list[i][2])
                thread_list.append( thread)
                thread.start()
            elif(type(source_list[i]) == type(int())): # webcam
                thread = Camera(name = i, address=source_list[i])
                thread_list.append(thread )
                thread.start()
            else:

                thread = Camera(name = i, address=source_list[i])
                thread_list.append(thread)
                thread.start()

    elif source_list is not None:
        thread = Camera(name = i, address=source_list)
        thread_list.append(thread)
        thread.start()
    else:
        print("Incorrect input to create_instances!")

    return thread_list

class Camera(Thread):
    '''
    Camera class used to simplify multithreaded access to camera stream.
    '''
    running = False
    cap = None
    frame = None

    def __init__(self, address, name = None, visualize = False):
        Thread.__init__(self)
        self.name = name
        self.address = address
        self.visualize = visualize

    def stop(self):
        self.cap.release()
        cv2.destroyAllWindows()

    def paus(self):
        self.running = False

    def play(self):
        self.run()

    def run(self):

        self.running = True

        try:
            if self.cap is None:
                self.cap = cv2.VideoCapture(self.address)

            if not self.cap.isOpened:
                self.cap = cv2.VideoCapture(self.address)
        except:
            raise Exception("Failed to capture ", str(self.address))

        # our loop
        while self.cap.isOpened and self.running:
            ret, self.frame = self.cap.read()

            if self.visualize:
                if frame is not None:
                    cv2.imshow(self.name, frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.stop()
