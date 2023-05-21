from manim import *

class MulExplanation(Scene):
    def construct(self):
        self.camera.background_color="#213d4c"

        x_label = Text("A", color=ORANGE).shift(UP * 3 + RIGHT * 4)
        x_val = DecimalNumber(0, 0).next_to(x_label, DOWN)
        x_tracker = ValueTracker(0)
        x_group = Group(x_label, x_val)
        y_label = Text("B", color=BLUE).shift(UP * 0.5 + RIGHT * 4)
        y_val = DecimalNumber(0, 0).next_to(y_label, DOWN)
        y_tracker = ValueTracker(0)
        y_group = Group(y_label, y_val)
        p_label = Text("P", color=GREEN).shift(DOWN * 2 + RIGHT * 4)
        p_val = DecimalNumber(0, 0).next_to(p_label, DOWN)
        p_tracker = ValueTracker(0)
        p_group = Group(p_label, p_val)

        b1 = SurroundingRectangle(x_group, color=WHITE, buff=MED_SMALL_BUFF).stretch_to_fit_width(3)
        b2 = SurroundingRectangle(y_group, color=WHITE, buff=MED_SMALL_BUFF).stretch_to_fit_width(3)
        b3 = SurroundingRectangle(p_group, color=WHITE, buff=MED_SMALL_BUFF).stretch_to_fit_width(3)
        self.play(FadeIn(x_label, x_val, y_label, y_val, p_label, p_val),
                  Create(b1), Create(b2), Create(b3))
        self.wait(1)
        
        mul_expr = MathTex(r'7 \times 16', font_size=100).move_to([-2, -2, 0])
        self.play(Write(mul_expr))
        self.wait(1)

        x_val.add_updater(lambda x: x.set_value(x_tracker.get_value()))
        y_val.add_updater(lambda y: y.set_value(y_tracker.get_value()))
        p_val.add_updater(lambda p: p.set_value(p_tracker.get_value()))

        self.play(x_tracker.animate.set_value(7), y_tracker.animate.set_value(16))
        self.wait(1)

        while x_tracker.get_value() > 0:
            self.play(p_tracker.animate.set_value(p_tracker.get_value() + y_tracker.get_value()),
                      x_tracker.animate.set_value(x_tracker.get_value() - 1))
            self.wait(1)

        p_rect = SurroundingRectangle(b3, buff=MED_LARGE_BUFF, color=RED)
        self.play(Create(p_rect))
        self.wait(1)