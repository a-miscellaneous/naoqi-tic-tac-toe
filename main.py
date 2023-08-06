import config as cfg
from naoqi import ALProxy
from PIL import Image
import time
from processImage import processImage as getBoardState
from basicRobot import BasicRobot
from ticTacToe import solve as solver
# import cv2 

class RobotVision(BasicRobot):
    def __init__(self):
        BasicRobot.__init__(self)
        self.window = []


    def getCameraImage(self):
        try:
            while True:
                naoImage = self.getProxy("ALVideoDevice").getImageRemote(self.camera)
                imageWidth = naoImage[0]
                imageHeight = naoImage[1]
                array = naoImage[6]
                im = Image.frombytes("RGB", (imageWidth, imageHeight), array)
                path = "./pictures/"+str(cfg.CAMERA_RESOLUTION) + "-" +str(int(time.time()))+".png"
                im.save(path, "PNG")
                self.handleImage(path)
        except KeyboardInterrupt, e:
            print e
            self.getProxy("ALVideoDevice").unsubscribe(self.camera)

    def handleImage(self, imagePath):
        boardState = getBoardState(imagePath)
        print boardState
        if boardState == None:
            self.window = []
            return
        if len(self.window) == cfg.WINDOW_SIZE:
            self.window.pop(0)
            
        self.window.append(boardState)
        self.handleWindow()
            
    def handleWindow(self):
        if len(self.window) < cfg.WINDOW_SIZE:
            return
        
        finalBoard = [["-" for i in range(3)] for i in range(3)]
        # collapse the window into a single board
        for board in self.window:
            for i in range(0, len(board)):
                for j in range(0, len(board[i])):
                    if board[i][j] != " ":
                        finalBoard[i][j] = board[i][j]
        print "Handler"
        sol = solver(finalBoard)
        print sol
        if sol == (None, None):
            return
        solution = cfg.DIRECTION_MAP[sol[0]-1]
        self.handleSpeach(solution)
        self.handlePoint(solution)


    def handlePoint(self, position):
        print "pointing"
        arm = "LArm" if ("L" in position) else "RArm" if ("R" in position) else "Arms"
        self.getProxy("ALTracker").pointAt(arm, cfg.POINT[position], 0, 1.0)
        time.sleep(2)
        self.getProxy("ALTracker").pointAt(arm, [0, 0, -1], 0, 1.0)
        
        

        
        
    def handleSpeach(self, position):
        words = cfg.SPEACH[position]
        self.sayWords(words)
        time.sleep(1)



if __name__ == "__main__":
    robot = RobotVision()
    # robot.goToPosture("Stand")
    robot.getProxy("ALAutonomousLife").setState("disabled")
    robot.getProxy("ALMotion").wakeUp()

    robot.getCameraImage()
    robot.handleSpeach("D")
    robot.rest()