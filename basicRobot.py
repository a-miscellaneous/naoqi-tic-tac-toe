import config as cfg
from naoqi import ALProxy


class BasicRobot():
    def __init__(self):
        self.ip = cfg.ROBOT_IP
        self.port = cfg.ROBOT_PORT
        self.proxys = {}
        
        
    ############################ PROXY CREATION ############################

    def getProxy(self, name):
        if name in self.proxys:
            return self.proxys[name]
        
        self.proxys[name] = self.createProxy(name)
        
        if name == "ALVideoDevice":
            self.generateCameraListener()
        
        return self.proxys[name]

    def generateCameraListener(self):
        proxy = self.getProxy("ALVideoDevice")
        self.camera = proxy.subscribeCamera(cfg.CAMERA_NAME , cfg.CAMERA_INDEX, cfg.CAMERA_RESOLUTION, cfg.CAMERA_COLOR, cfg.CAMERA_FPS)
        print self.camera

    def createProxy(self, name):
        try:
            proxy = ALProxy(name, self.ip, self.port)
        except Exception, e:
            print "Could not create proxy: " + name
            quit()
        return proxy
    
    
    ############################ BASIC MOVEMENTS ############################

    def rest(self):
        self.getProxy("ALMotion").rest()

    def goToPosture(self, posture):
        self.getProxy("ALRobotPosture").goToPosture(posture, 1.0)

    def changeHand(self, lHand, openHand):
        hand = "LHand" if lHand else "RHand"
        if openHand:
            self.getProxy("ALMotion").openHand(hand)
        else:
            self.getProxy("ALMotion").closeHand(hand)
            
        
    def sayWords(self, words):
        self.getProxy("ALTextToSpeech").say(words)


