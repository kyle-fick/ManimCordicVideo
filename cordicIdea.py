from manim import *

class CordicIdea(Scene):
    def construct(self):
        self.camera.background_color="#213d4c"

        angle = ValueTracker(0)

        rotcirc = Circle(3.5, WHITE)
        circAxes = Axes([-2, 2], [-2, 2], rotcirc.radius * 2, rotcirc.radius * 2, axis_config={'include_ticks': True}, tips=False).move_to(rotcirc)
        circGroup = Group(rotcirc, circAxes)

        self.play(Create(rotcirc), Create(circAxes))
        self.wait(1)

        vector = Arrow(start=circAxes.coords_to_point(0, 0), end=circAxes.coords_to_point(1, 0), color=BLUE_B, buff=0)
        vector.add_updater(lambda a: a.become(Arrow(start=circAxes.coords_to_point(0, 0), end=circAxes.coords_to_point(np.cos(angle.get_value()), np.sin(angle.get_value())), color=BLUE_B, buff=0)))
        angle_mark = Arc(.5, 0, 0)
        angle_mark.add_updater(lambda a: a.become(Arc(.5, 0, angle.get_value())))
        self.play(Create(vector))
        self.add(angle_mark)
        self.wait(1)

        def rotateVector(ang):
            self.play(angle.animate.set_value(angle.get_value() + ang))

        self.play(angle.animate.set_value(PI/4))
        self.wait(1)
        self.play(angle.animate.set_value(PI/6))