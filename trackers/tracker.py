from ultralytics import YOLO
import cv2
import os
import supervision as sv
import pickle


class Tracker:
    def __init__(self, model_path):
        self.model = YOLO(model_path)
        self.tracker = sv.ByteTrack()

    def detect_frames(self, frames):
        batch_size = 20
        detections = []

        # Split frames into batches of size batch_size
        # and detect each batch separately
        # for faster processing and avoid memory issues

        for i in range(0, len(frames), batch_size):
            batch = frames[i:i+batch_size]
            detections_batch = self.model.predict(batch, conf=0.1)
            detections += detections_batch

        return detections

    def get_object_tracks(self, frames, read_from_stub=False, stub_path=None):

        if read_from_stub and stub_path is not None and os.path.exists(stub_path):
            with open(stub_path, 'rb') as f:
                tracks = pickle.load(f)
            return tracks

        detections = self.detect_frames(frames)
        tracks = {
            'players': [],
            'referees': [],
            'ball': []
        }

        for frame_num, detection in enumerate(detections):
            class_names = detection.names
            class_names_inv = {i: j for j, i in class_names.items()}

            # convert the detection to supervison format
            detection_sv = sv.Detections.from_ultralytics(detection)

            # convert goalkeeper to player object
            for index, class_id in enumerate(detection_sv.class_id):
                if class_names[class_id] == 'goalkeeper':
                    detection_sv.class_id[index] = class_names_inv['player']

            # Track objects
            detections_with_tracks = self.tracker.update_with_detections(
                detection_sv)

            tracks['players'].append({})
            tracks['referees'].append({})
            tracks['ball'].append({})

            # Tracking the players and the referee since they are more than one.
            # No need to track the ball using the detection with tracks since there is
            # only one ball in the video hence only one bounding ball
            for frame_detection in detections_with_tracks:
                bounding_box = frame_detection[0].tolist()
                class_id = frame_detection[3]
                track_id = frame_detection[4]

                if class_id == class_names_inv['player']:
                    tracks['players'][frame_num][track_id] = {
                        "bounding_box": bounding_box}
                elif class_id == class_names_inv['referee']:
                    tracks['referees'][frame_num][track_id] = {
                        "bounding_box": bounding_box}

            # Tracking the ball...
            for frame_detection in detection_sv:
                bounding_box = frame_detection[0].tolist()
                class_id = frame_detection[3]

                if class_id == class_names_inv['ball']:
                    # We're using a constant one since there's only one ball
                    tracks['ball'][frame_num][1] = {
                        "bounding_box": bounding_box}

            if stub_path is not None:
                with open(stub_path, 'wb') as f:
                    pickle.dump(tracks, f)

            return tracks
