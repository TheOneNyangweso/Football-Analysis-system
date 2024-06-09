import cv2


def read_video(video_path):
    """read_video : reads a video file and returns the frames

    Args:
        video_path : frames of the video
    """
    cap = cv2.VideoCapture(video_path)
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    return frames


def save_video(output_video_frames, output_video_path):
    # XVID is the output format
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    # generate a video at the path, of type fourcc @ 24 frames/second and framesize as
    # the last parameter (width, height)
    out = cv2.VideoWriter(output_video_path, fourcc, 24,
                          (output_video_frames[0].shape[1], output_video_frames[0].shape[0]))
    for frame in output_video_frames:
        out.write(frame)
    out.release
