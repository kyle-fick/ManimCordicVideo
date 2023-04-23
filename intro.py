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

        self.camera.save_state()
        self.play(self.camera.frame.animate.move_to(RIGHT * 2 + UP * 1.5).scale(0.6))
        self.wait(1)

        dot = Dot(radius=0.1, color=RED, z_index=1).move_to(circle_axes.c2p(np.sqrt(2)/2, np.sqrt(2)/2))
        dot_line = Line(start=unit_circle.get_center(), end=dot.get_center(), color=WHITE)
        line_label = MathTex(r'1').move_to(dot_line).shift(UL * .25)
        angle = Angle(Line(ORIGIN, RIGHT), dot_line, radius=0.5)
        theta_tex = MathTex(r'{\theta}', color=WHITE).move_to(angle).shift(UP * .2 + RIGHT * .35)
        self.play(Create(dot_line), Write(line_label))
        self.play(Create(dot))
        self.play(Create(angle), Write(theta_tex))
        self.wait(1)

        sin_line = DashedLine(start=[dot.get_center()[0], unit_circle.get_center()[1], 0], end=dot.get_center(), color=YELLOW)
        cos_line = DashedLine(start=[unit_circle.get_center()[0], dot.get_center()[1], 0], end=dot.get_center(), color=BLUE)

        self.play(Create(sin_line), Create(cos_line))

        sin_tex = MathTex(r'\sin', r'({{\theta}})', color=WHITE).set_color_by_tex(r'\sin', YELLOW).move_to(sin_line.get_center()).shift(RIGHT * 0.75).scale(0.75)
        cos_tex = MathTex(r'\cos', r'({{\theta}})', color=WHITE).set_color_by_tex(r'\cos', BLUE).move_to(cos_line.get_center()).shift(UP * 0.5).scale(0.75)

        sin_rect = BackgroundRectangle(sin_tex, color=BLACK, fill_opacity=0.5, corner_radius=0.1, buff=0.1)
        cos_rect = BackgroundRectangle(cos_tex, color=BLACK, fill_opacity=0.5, corner_radius=0.1, buff=0.1)

        self.play(Create(sin_rect), Create(cos_rect), Write(sin_tex), Write(cos_tex))
        self.wait(1)

        point_coords = MathTex(r'(', r'\cos', r'({{\theta}})', r',', r'\sin', r'({{\theta}})', r')', color=WHITE).set_color_by_tex(r'\cos', BLUE).set_color_by_tex(r'\sin', YELLOW).next_to(dot, UR)
        self.play(Write(point_coords))
        self.wait(1)

        r_tex = MathTex(r'r', color=ORANGE).move_to(line_label)
        r_point_coords = MathTex(r'(', r'r', r'\cos', r'({{\theta}})', r',', r'r', r'\sin', r'({{\theta}})', r')', color=WHITE).set_color_by_tex(r'\cos', BLUE).set_color_by_tex(r'\sin', YELLOW).set_color_by_tex(r'r', ORANGE).move_to(point_coords)
        self.play(ReplacementTransform(line_label, r_tex))
        self.wait(1)
        self.play(TransformMatchingTex(point_coords, r_point_coords))
        self.wait(1)