# Football-Analysis-system

**By : Moruri Sammy Nyamweya**\
**Email : morurisammy5@gmail.com**\
**Phone : +254112686783**

A comprehensive Football Analysis System using Python, YOLO (You Only Look Once), and OpenCV to track and analyze player movements, ball trajectories, and game events in real-time.
Most of the project is done in Google Colab due to free GPU + gemini AI to assist in debugging errors.\
Local implementation was used in areas which required minimal resources

**Dataset link : https://www.kaggle.com/competitions/dfl-bundesliga-data-shootout/data -- by Deutsche Fußball Liga e.V.** \
**Roboflow dataset link used for finetuning ball detection : https://universe.roboflow.com/roboflow-jvuqo/football-players-detection-3zvbc/dataset/1 -- used to improve our own model**

## Steps Followed

### 1. Detecting the players and the ball (Object detection)

This is just using a CNN to detect ocjects in the image and generate the bounding boxes of the objects.

**Libraries/Technologies/Architecture used**

- ultralytics -- Python library with the YOLO model
- roboflow -- Python library to work with roboflow universe
- os
- json

**What was done** \
Some directories were not pushed due to Github's file size limit. (check .gitignore)

### 2. Tracking

This step involves tracking objects i.e assigning an object to a bounding box across multiple frames.\
What this step basically does is to ensure the object inside a particular bounding box is constant across multiple video frames\
This is achieved by use of a **byte tracker**, which assigns a bounding box an ID. The tracker also knows what is inside its\
bounding box among much more.

Definiton from Roboflow: _ByteTrack is a multi-object tracking computer vision algorithm. Using ByteTrack, you can allocate IDs for unique objects in a video for use in tracking objects. For example, you can track players on a football field and monitor them throughout a scene._

**Libraries/Technologies/Architecture used**

- ultralytics -- Python library with the YOLO model
- roboflow -- Python library to work with roboflow universe
- os
- cv2 -- convert the video format from mp4 to avi
- supervision -- Loads the byte tracker which helps to perfom majority of the tracking tasks
- pickle -- Saves the tracking result to avoid running the tracker everytime
- numpy

**What was done** \
.mp4 was converted to .avi\
The objects' tracks were generated and saved as pickle file.\
A pickle file was finally created (at the stubs directory) to reduce the time to load the file with the tracker results.
The bounding boxes were replaced by ellipses at the base of the player and referee objects and an inverted triangle as\
a pointer to the ball. The resulting frame were appended together to form a new output video.

### 3. Player (or Team) Color assignment

Our focus is now to assign each team its own color assignment so as to differentiate them.\
This will be achieved cv2 and matplotlib.

**Libraries/Technologies/Architecture used**

- os
- cv2
- scikit-learn - To use kmeans for clustering
- matplotlib
- numpy

**What was done**

A picture of a player was extracted from a single frame and used to train the k-means clustering algorithm.\
The result was the player's jersey colour. These, with players tracks from the previous steps form a team.\
K-means was the point of focus here. It was used extensively since this part involved a lot of classification

### 4. Ball interpolation

## References

- https://docs.ultralytics.com/models/yolov8/
