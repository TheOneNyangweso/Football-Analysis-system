# Football-Analysis-system

A comprehensive Football Analysis System using Python, YOLO (You Only Look Once), and OpenCV to track and analyze player movements, ball trajectories, and game events in real-time.\

**Dataset link : https://www.kaggle.com/competitions/dfl-bundesliga-data-shootout/data -- by Deutsche Fußball Liga e.V.**
**Roboflow dataset link used for finetuning : https://universe.roboflow.com/roboflow-jvuqo/football-players-detection-3zvbc/dataset/1 -- used to improve our own model**

## Steps Followed

### 1. Detecting the players and the ball (Object detection)

This is just using a CNN to detect ocjects in the image and generate the bounding boxes of the objects.

**Libraries/Technologies/Architecture used**

- Google Colab -- chosen due to free GPU + gemini AI to assist in debugging errors
- ultralytics -- Python library with the YOLO model
- roboflow -- Python library to work with roboflow universe

**What was done**
Some directories were not pushed due to Github's file size limit. (check .gitignore)

## References

- https://docs.ultralytics.com/models/yolov8/
