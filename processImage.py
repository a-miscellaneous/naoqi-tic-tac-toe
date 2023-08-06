import numpy as np
import cv2
import sys


class ProcessImage:
    def __init__(self, imagePath, show=False):
        self.imagePath = imagePath
        self.image = cv2.imread(imagePath)
        
        self.imageWidth = self.image.shape[0]
        self.imageHeight = self.image.shape[1]
        self.smoothingKernel = np.ones((3, 3), np.uint8)
        self.threshholdField = 150
        self.showBool = show
        

    def run(self):
        self.show(self.image)
        self.getGreyscaleImage()
        self.getThresholdedImage()
        self.getSmoothedImage()
        self.getContours()
        self.processTiles()
        return self.buildGameState()

    def show(self, image):
        if self.showBool is False:
            return
        cv2.imshow('image', image)
        cv2.waitKey(0)

    def showContours(self, contors, image=None):
        if image is None:
            image = self.image
        im = image.copy()
        cv2.drawContours(im, contors, -1, (0, 255, 0), 3)
        self.show(im)

    def getGreyscaleImage(self):        
        self.greyScaleImage = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.show(self.greyScaleImage)
        return self.greyScaleImage

    def getThresholdedImage(self):
        ret, thresh1 = cv2.threshold(
            self.greyScaleImage, self.threshholdField, 255, cv2.THRESH_BINARY)
        self.show(thresh1)
        self.threshBoard = thresh1
        return thresh1

    def getSmoothedImage(self):
        self.threshBoard = cv2.morphologyEx(
            self.threshBoard, cv2.MORPH_OPEN, self.smoothingKernel)
        self.show(self.threshBoard)
        return self.threshBoard

    def getContours(self):
        contours, hierearchy = cv2.findContours(
            self.threshBoard, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        self.boardContours = contours
        self.showContours(contours)
        return contours

    def processTiles(self):
        tiles = []
        for cnt in self.boardContours:
            # ignore small contours that are not tiles
            if cv2.contourArea(cnt) < 3000:
                continue
            rect = cv2.minAreaRect(cnt)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            self.showContours([box])
            tileImg = self.getCutout(rect, box)
            symbol = self.processTile(tileImg)
            tiles.append({"symbol": symbol, "coordinates": rect[0]})
        self.tiles = tiles
        return tiles

    def getCutout(self, rect, box):
        width = int(rect[1][0])
        height = int(rect[1][1])
        sPoints = box.astype("float32")
        dPoints = np.array([[0, height-1],
                            [0, 0],
                            [width-1, 0],
                            [width-1, height-1]], dtype="float32")
        M = cv2.getPerspectiveTransform(sPoints, dPoints)
        warped = cv2.warpPerspective(self.threshBoard, M, (width, height))
        self.show(warped)
        warped = cv2.copyMakeBorder(
            warped, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=(0, 0, 0))
        self.show(warped)
        warped = cv2.floodFill(warped, None, (0, 0), 255)[1]
        self.show(warped)
        warped = cv2.medianBlur(warped, 5)
        self.show(warped)
        return warped

    def processTile(self, img):
        # find contours in the tile
        cont, hier = cv2.findContours(
            img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cont = sorted(cont, key=cv2.contourArea, reverse=True)
        if len(cont) == 1:  # only one contour
            return ' '

        cont = cont[1]
        area = cv2.contourArea(cont)
        hull = cv2.convexHull(cont)
        hull_area = cv2.contourArea(hull)
        solidity = float(area)/hull_area

        if solidity > 0.5:
            return 'O'
        else:
            return 'X'

    def buildGameState(self):
        gameState = [["-" for _ in range(3)] for _ in range(3)]
        ySorted = sorted(self.tiles, key=lambda k: k['coordinates'][1])
        for i in range(3):
            row = ySorted[i*3:i*3+3]
            xSorted = sorted(row, key=lambda k: k['coordinates'][0])
            for j in range(3):
                gameState[i][j] = xSorted[j]['symbol']
            
        return gameState




def processImage(imagePath, b= False):
    try:
        res = ProcessImage(imagePath, b).run()
        print(res)
        return res
    except Exception as e:
        print("unclear Image")
        return None
        
    
    
    

if __name__ == "__main__":
    processImage('./pictures/2-1691069256.png', True)