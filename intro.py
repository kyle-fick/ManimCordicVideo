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
        self.wait(1)

        unit_circle = Circle(radius=3, color=WHITE)
        circle_axes = Axes([-1, 1, 0.1], [-1, 1, 0.1], unit_circle.radius*2, unit_circle.radius*2, tips=False)   
        self.play(ReplacementTransform(VGroup(func_axes, sin_func), unit_circle), FadeOut(calculator, shift=DOWN))
        self.play(Create(circle_axes))
        self.wait(1)

        self.play(self.camera.frame.animate.move_to(RIGHT * 2 + UP * 1.5).scale(0.6))
        self.wait(1)

        dot = Dot(radius=0.1, color=RED).move_to(circle_axes.c2p(np.sqrt(2)/2, np.sqrt(2)/2))
        dot_line = Line(start=unit_circle.get_center(), end=dot.get_center(), color=WHITE)
        line_label = MathTex(r'1').move_to(dot_line).shift(UL * .25)
        self.play(Create(dot_line), Write(line_label))
        self.play(Create(dot))
        self.wait(1)