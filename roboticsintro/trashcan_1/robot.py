import pymunk
from ..common import M_TO_PIXELS


class Robot(object):

    def __init__(self):
        body_mass = 1
        radius = 0.1 * M_TO_PIXELS
        body_I = pymunk.moment_for_circle(body_mass, 0, radius)
        self.body = pymunk.Body(body_mass, body_I)
        self.body.position = 0., 0.
        self.body.angle = 0
        self.shape = pymunk.Circle(self.body, radius)
        self.shape.color = 255, 0, 0
        self.shape.elasticity = 0.05
