import os
from utils.video_utils import read_video, save_video


def main():
    # Read video
    video_frames = read_video('clips/input/08fd33_4.mp4')

    # save video
    save_video(video_frames, 'clips/output/08fd33_4.avi')


if __name__ == 'main':
    # Setting PYTHONPATH to include the current directory
    os.environ['PYTHONPATH'] = os.path.join(os.getcwd(), '')
    main()
