import pyglet
import pymunk
import pymunk.pyglet_util
from pyglet.window import key
from math import pi
from . import Robot
from ..common import M_TO_PIXELS, VISUAL_RATE


class Simulation(object):

    def __init__(self):
        self.space = pymunk.Space()

    def reset_space(self):
        pass

    def handle_collision(self, space, arbiter, *args, **kwargs):
        pass  # bool

    def forward_update(self, dt):
        pass

    def run(self):
        # timed loop
        pass

    def visualize(self):
        window = pyglet.window.Window(visible=False)

        @window.event
        def on_draw():
            # always clear and redraw
            window.clear()
            pymunk.pyglet_util.draw(self.space)

        pyglet.clock.schedule_interval(self.forward_update, 1/VISUAL_RATE)



def run():
    window = pyglet.window.Window(visible=False)
    keyboard = key.KeyStateHandler()
    window.push_handlers(keyboard)
    fps = pyglet.clock.ClockDisplay()
    space = pymunk.Space()
    space.gravity = 0., 0.
    robot = Robot()
    robot.body.position = 200, 200
    space.add(robot.body, robot.shape)

    def move_robot(dt):
        linear_delta = 0.01 * M_TO_PIXELS * dt/RUN_RATE
        rads_per_sec = 2*pi/8
        angular_delta = rads_per_sec * dt
        if keyboard[key.RIGHT]:
            robot.body.angle -= angular_delta
        if keyboard[key.LEFT]:
            robot.body.angle += angular_delta
        # TODO trig: direction from angle
        if keyboard[key.UP]:
            robot.body.position += 0, linear_delta
        if keyboard[key.DOWN]:
            robot.body.position -= 0, linear_delta

    @window.event
    def on_draw():
        # always clear and redraw
        window.clear()
        pymunk.pyglet_util.draw(space)
        fps.draw()

    pyglet.clock.schedule_interval(space.step, RUN_RATE)
    pyglet.clock.schedule_interval(move_robot, RUN_RATE)
    window.set_visible(True)
    pyglet.app.run()
