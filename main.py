import cv2

# Load YOLO model
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

# Load the COCO names for classes
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]


cap = cv2.VideoCapture(0)