# Football-Analysis-system

**By : Moruri Sammy Nyamweya**\
**Email : morurisammy5@gmail.com**\
**Phone : +254112686783**

A comprehensive Football Analysis System using Python, YOLO (You Only Look Once), and OpenCV to track and analyze player movements, ball trajectories, and game events in real-time.

**Dataset link : https://www.kaggle.com/competitions/dfl-bundesliga-data-shootout/data -- by Deutsche Fußball Liga e.V.** \
**Roboflow dataset link used for finetuning ball detection : https://universe.roboflow.com/roboflow-jvuqo/football-players-detection-3zvbc/dataset/1 -- used to improve our own model**

## Steps Followed

### 1. Detecting the players and the ball (Object detection)

This is just using a CNN to detect ocjects in the image and generate the bounding boxes of the objects.

**Libraries/Technologies/Architecture used**

- Google Colab -- chosen due to free GPU + gemini AI to assist in debugging errors
- ultralytics -- Python library with the YOLO model
- roboflow -- Python library to work with roboflow universe

**What was done** \
Some directories were not pushed due to Github's file size limit. (check .gitignore)

### 2. Tracking

This step involves tracking objects i.e assigning an object to a bounding box across multiple frames.\
What this step basically does is to ensure the object inside a particular bounding box is constant across multiple video frames\
This is achieved by use of a **tracker**, which assigns a bounding box an ID. The tracker also knows what is inside its\
bounding box among much more.

## References

- https://docs.ultralytics.com/models/yolov8/
