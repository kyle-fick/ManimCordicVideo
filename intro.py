from manim import *

class Intro(MovingCameraScene):
    def construct(self):
        self.camera.background_color="#213d4c"

        calculator = SVGMobject("media/images/intro/calculator.svg").set_color(WHITE)
        calculator.scale(2)

        self.play(Create(calculator),  run_time=2)
        self.wait(1)

        self.play(calculator.animate.shift(LEFT*3))
                  
        func_axes = Axes([-PI, PI], [-2,2], 4, 3, tips=False).shift(RIGHT * 3)
        offset = ValueTracker(0)
        sin_func = always_redraw(lambda: func_axes.plot(lambda x: np.sin(x + offset.get_value()), color=RED))
        self.play(FadeIn(func_axes), Create(sin_func))
        self.play(offset.animate.set_value(2*PI), run_time=5)