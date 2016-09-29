import sys
import cv2
import numpy as np


CV_CAP_PROP_FRAME_COUNT = 7
CV_CAP_PROP_FPS = 5
CV_CAP_PROP_FRAME_WIDTH = 3
CV_CAP_PROP_FRAME_HEIGHT = 4


# python correct-video.py ../Flight/20130714/GOPR0036.MP4 /Users/bendyer/Projects/UAV\ Samples/Flight/20130714/GOPR0036-Corrected.avi

if __name__ == '__main__':
    if not sys.argv[2] or not sys.argv[2].startswith('/') or not sys.argv[2].endswith('.avi'):
        print 'Second argument must be the FULL output video path, ending in .avi'

    video = cv2.VideoCapture(sys.argv[1])

    num_frames = int(video.get(CV_CAP_PROP_FRAME_COUNT))
    fps = video.get(CV_CAP_PROP_FPS)
    width = int(video.get(CV_CAP_PROP_FRAME_WIDTH))
    height = int(video.get(CV_CAP_PROP_FRAME_HEIGHT))

    print "%d frames @ %d fps" % (num_frames, fps)

    intrinsic = np.array(
        [[ 299.39646639,    0.,          419.96165812],
         [   0.,          302.5602385,   230.25411049],
         [   0.,            0.,            1.        ]]
    )
    distortion = np.array(
        [-0.16792771, 0.03121603, 0.00218195, -0.00026904, -0.00263317]
    )

    writer = cv2.VideoWriter(
        filename=sys.argv[2],
        fourcc=(ord('X') << 24) + (ord('V') << 16) + (ord('I') << 8) + ord('D'),
        fps=fps,
        frameSize=(width,height),
        isColor=1)
    horizonf = open(sys.argv[2].rpartition(".")[0] + "-horizon.txt", "wb")

    for f in xrange(num_frames):
        success, img = video.read()
        if not success or img is None:
            print "Error on frame %s" % f
            break

        img = cv2.undistort(img, intrinsic, distortion)
        edges = cv2.Canny(
            cv2.resize(cv2.split(img)[0], (width / 4, height / 4), 0, 0, cv2.INTER_NEAREST),
            200, 600, apertureSize=3)
        vx, vy, x0, y0 = cv2.fitLine(np.argwhere(edges == 255), 2, 0, 0.01, 0.01)  # 2 = CV_DIST_L2
        horizonf.write("%.6f,%.6f,%.6f,%.6f\n" % (vx * 4, vy * 4, x0 * 4, y0 * 4))

        writer.write(img)

        if f % 2400 == 0:
            print 100.0 * (f / float(num_frames)), "%"

    horizonf.close()
    writer.release()




def attitude_from_horizon(x0, y0, x1, y1, expected_roll):
    # Determine pitch and roll from a horizon line segment identified by the
    # points (x0, x1) and (y0, y1) in an image.
    # Uses the CAMERA_INTRINSICS values (fx, 0, cx, 0, fy, cy, 0, 0, 1) to
    # convert the point to a normalized (u, v) representation, then uses
    # formulas 27 and 33 from http://eprints.qut.edu.au/12839/1/3067a485.pdf
    # to determine pitch and roll.

    x, y = x0, y0
    mx, my = x1 - x0, y1 - y0
    fx, fy = CAMERA_INTRINSICS[0][0], CAMERA_INTRINSICS[1][1]
    cx, cy = CAMERA_INTRINSICS[0][2], CAMERA_INTRINSICS[1][2]

    # X and Y are flipped in the intrinsics matrix relative to the fitLine
    # output -- no, I don't know why.
    u = (y - cx) / fx
    v = (x - cy) / fy
    f = 1.0

    roll = math.atan2(-mx, my)
    # Ensure that roll is pointing in approx the same direction as
    # expected_roll
    if expected_roll - math.degrees(roll) > 135.0:
        roll += math.pi
    elif expected_roll - math.degrees(roll) < -135.0:
        roll -= math.pi

    pitch = math.atan((u * math.sin(roll) + v * math.cos(roll)) / f)

    return math.degrees(pitch), math.degrees(roll)    