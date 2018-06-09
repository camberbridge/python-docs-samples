# coding: utf-8

"""
About parameter
    - num_cut: a number of offsets

usage
    - python video2frames.py hoge.py
"""


import os, sys, cv2

def video_to_frames(video_file=sys.argv[1], image_dir='./image_dir/', num_cut=10):
    if not os.path.exists(image_dir):
        # Make the directory if it doesn't exist.
        os.makedirs(image_dir)

    cap = cv2.VideoCapture(video_file)
    img_counter = 0  # A number of save images
    frame_counter = 0 # A number of read frames
    while(cap.isOpened()):
        flag, frame = cap.read()  # Capture frame-by-frame
        if flag == False: 
            break

        if frame_counter % num_cut == 0:
            img_file_name = image_dir + str(img_counter) + ".png"
            cv2.imwrite(img_file_name, frame)
            img_counter += 1
        frame_counter += 1

    cap.release()  # When everything done, release the capture


if __name__ == '__main__':
    video_to_frames()
