import vision_definitions

ROBOT_IP = "10.0.7.113"
ROBOT_PORT = 9559


CAMERA_NAME = "c1Name"
CAMERA_RESOLUTION = 2  
CAMERA_COLOR = vision_definitions.kRGBColorSpace # 11
CAMERA_FPS = 30
CAMERA_INDEX = 0
CAMERA_NAME = "Camera Name"

WINDOW_SIZE = 2

INDEX_TO_POINT = {
    1: "UL",
    2: "U",
    3: "UR",
    4: "L",
    5: "M",
    6: "R",
    7: "DL",
    8: "D",
    9: "DR"
}




DIRECTIONS = ["U", "D", "M", "R", "L", "UR", "UL", "DR", "DL"]
DIRECTION_MAP = ["UL", "U", "UR", "L", "M", "R", "DL", "D", "DR"]


POINT = {}

heightOffset = 0.3
widthOffset = 0.35

for d in DIRECTIONS:
    POINT[d] = [0.2, 0.0, 0.1] # center
    
POINT["U"][2] += heightOffset
POINT["D"][2] -= heightOffset
POINT["L"][1] += widthOffset
POINT["R"][1] -= widthOffset
POINT["UL"][2] += heightOffset
POINT["UL"][1] += widthOffset
POINT["UR"][2] += heightOffset
POINT["UR"][1] -= widthOffset
POINT["DL"][2] -= heightOffset
POINT["DL"][1] += widthOffset
POINT["DR"][2] -= heightOffset
POINT["DR"][1] -= widthOffset

    
    
    

SPEACH = {
    "U": "I want to play top mid",
    "D": "I want to play bottom mid",
    "M": "I want to play in the middle",
    "R": "I want to play middle right",
    "L": "I want to play middle left",
    "UR": "I want to play top right",
    "UL": "I want to play top left",
    "DR": "I want to play bottom right",
    "DL": "I want to play bottom left"
}

 

BALL_SIZE = 0.06
