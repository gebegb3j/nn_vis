from enum import IntEnum, IntFlag, auto
from typing import List

from pyrr import Vector3


class ProcessRenderMode(IntFlag):
    FINAL = auto()
    NODE_ITERATIONS = auto()
    EDGE_ITERATIONS = auto()
    SMOOTHING = auto()


class CameraPose(IntEnum):
    FRONT = 0
    RIGHT = 1
    LEFT = 2
    LOWER_BACK_RIGHT = 3
    BACK_RIGHT = 4
    UPPER_BACK_LEFT = 5
    UPPER_BACK_RIGHT = 6
    BACK = 7
    DEFAULT = 8


CAMERA_POSE_POSITION: List[Vector3] = [
    Vector3([3.5, 0.0, 0.0]),
    Vector3([0.0, 0.0, 2.5]),
    Vector3([0.0, 0.0, -2.5]),
    Vector3([-2.75, -1.0, 1.25]),
    Vector3([-2.5, 0.0, 2.5]),
    Vector3([-2.0, 2.0, -2.0]),
    Vector3([-2.0, 2.0, 2.0]),
    Vector3([-4.0, 0.0, 0.0]),
    Vector3([-3.5, 0.0, 0.0])
]
