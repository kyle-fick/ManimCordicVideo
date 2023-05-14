from manim import *

class AtanSeries(MovingCameraScene):
    def construct(self):
        self.camera.background_color="#213d4c"
        
        atan_series = MathTex(r"\sum_{n=0}^{\infty} \tan^{-1} \left(\frac{1}{2^n}\right)")
        self.play(Write(atan_series))
        self.wait(1)

        angle_series = MathTex(r'\approx', r'45', r'+', r'22.625', r'+', r'\cdots')
        self.play(atan_series.animate.shift(UP*2), Write(angle_series))
        self.wait(1)

        ratio_test = MathTex(r'\lim_{n\to\infty}', r'\left| a_{n+1} \over a_{n} \right|', r'<', r'1')
        self.play(Write(ratio_test.shift(DOWN * 2)))
        self.wait(1)

        ratio_rect = SurroundingRectangle(ratio_test, color=RED, buff=MED_LARGE_BUFF)
        self.play(Create(ratio_rect))
        self.wait(1)

        self.play(FadeOut(atan_series), FadeOut(angle_series), FadeOut(ratio_rect, shift=UP), ratio_test.animate.move_to(ORIGIN))
        self.wait(1)

        ratio_test_2 = MathTex(r'\lim_{n\to\infty}', r'\left| \tan^{-1} \left( \frac{1}{2^{n+1}} \right) \over \tan^{-1} \left( \frac{1}{2^n} \right) \right|').scale(1.5)
        zero_tex = MathTex(r'0').scale(1.5).next_to(ratio_test_2[1], direction=DOWN, buff=1.5)
        zero_tex_2 = zero_tex.copy().next_to(ratio_test_2[1], direction=UP, buff=1.5)
        arrow_1 = Arrow(start=ratio_test_2[1].get_bottom(), end=zero_tex.get_top(), buff=0.25)
        arrow_2 = Arrow(start=ratio_test_2[1].get_top(), end=zero_tex_2.get_bottom(), buff=0.25)
        self.play(Transform(ratio_test, ratio_test_2))
        self.wait(1)
        self.play(Write(zero_tex), Write(zero_tex_2),
                  Create(arrow_1), Create(arrow_2))
        self.wait(1)

        lhop_axes = Axes([0, 5], [-2, 2], tips=False)
        f_x = lambda x: (x-2)**2 - 1
        g_x = lambda x: -(x-3)
        func_f = lhop_axes.plot(f_x, color=RED)
        func_g = lhop_axes.plot(g_x, color=BLUE)
        self.play(FadeOut(ratio_test, zero_tex, zero_tex_2, arrow_1, arrow_2), FadeIn(lhop_axes))
        self.wait(1)

        self.play(Create(func_f), Create(func_g))
        self.wait(1)

        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.move_to(lhop_axes.c2p(3, 0)).scale(0.1), 
                  func_f.animate.set(stroke_width=1),
                  func_g.animate.set(stroke_width=1))
        self.wait(1)

        dx = 0.1
        dy_f = f_x(3 + dx)
        dy_g = g_x(3 + dx)
        
        dx_line = DashedLine(lhop_axes.c2p(3, 0), lhop_axes.c2p(3 + dx, 0), stroke_width=1, color=ORANGE, dash_length=0.02)
        dy_f_line = DashedLine(start=lhop_axes.c2p(3 + dx, 0), end=lhop_axes.c2p(3 + dx, dy_f), stroke_width=1, color=RED, dash_length=0.02)
        dy_g_line = DashedLine(start=lhop_axes.c2p(3 + dx, 0), end=lhop_axes.c2p(3 + dx, dy_g), stroke_width=1, color=BLUE, dash_length=0.02)
        self.play(Create(dx_line), Create(dy_f_line), Create(dy_g_line))
        self.wait(1)

        dx_tex = MathTex(r'dx', color=ORANGE).next_to(dx_line, DOWN, buff=0.01).scale(0.25)
        dy_f_tex = MathTex(r'dy', color=RED).next_to(dy_f_line, RIGHT).shift(LEFT * 0.35).scale(0.25)
        dy_g_tex = MathTex(r'dy', color=BLUE).next_to(dy_g_line, RIGHT).shift(LEFT * 0.35).scale(0.25)
        self.play(Write(dy_f_tex), Write(dy_g_tex), Write(dx_tex))
        self.wait(1)

        # not working
        dy_dx_tex = MathTex(r'{ {{dy}}', r'\over', r'{{dx}} }', r'\over', r'{ {{dy}}', r'\over', r'{{dx}} }').scale(0.25).move_to(dx_line).shift(LEFT * 0.5)
        dy_dx_tex[1].set_color(RED)
        dy_dx_tex[3].set_color(ORANGE)
        dy_dx_tex[7].set_color(BLUE)
        dy_dx_tex[9].set_color(ORANGE)

        dy_dy_tex = MathTex(r'{ {{dy}}', r'\over', r'{{dy}} }').scale(0.25).move_to(dy_dx_tex)
        dy_dy_tex[1].set_color(RED)
        dy_dy_tex[3].set_color(BLUE)

        dy_dx_back = BackgroundRectangle(dy_dx_tex, BLACK, fill_opacity=0.7, buff=0.02, corner_radius=0.05)
        dy_dy_back = BackgroundRectangle(dy_dy_tex, BLACK, fill_opacity=0.7, buff=0.02, corner_radius=0.05)

        self.play(FadeIn(dy_dx_back, dy_dx_tex))
        self.wait(1)

        self.play(TransformMatchingTex(dy_dx_tex, dy_dy_tex), Transform(dy_dx_back, dy_dy_back))
        self.wait(1)

        self.play(Restore(self.camera.frame),
                  func_f.animate.set(stroke_width=4),
                  func_g.animate.set(stroke_width=4))
        self.play(FadeOut(lhop_axes, func_f, func_g, dx_line, dy_f_line, dy_g_line, dx_tex, dy_f_tex, dy_g_tex, dy_dy_tex, dy_dx_back), FadeIn(ratio_test))
        self.wait(1)

        ratio_test_3 = MathTex(r'\lim_{n\to\infty}', r'\left| \frac{2^{n+1} \ln(2)}{1 + 4^{n+1}} \over \frac{2^n \ln(2)}{1 + 4^n} \right|').scale(1.5)
        self.play(Transform(ratio_test, ratio_test_3))
        self.wait(1)

        ratio_test_4 = MathTex(r'\lim_{n\to\infty}', r'2 \cdot \frac{4^n + 1}{4^{n+1} + 1}').scale(1.5)
        self.play(Transform(ratio_test, ratio_test_4))
        self.wait(1)

        ratio_test_5 = MathTex(r'\lim_{n\to\infty}', r'\frac{1}{2} \cdot \frac{4^n + 1}{4^n + \frac{1}{4}}').scale(1.5)
        self.play(Transform(ratio_test, ratio_test_5))
        self.wait(1)

        ratio_test_6 = MathTex(r'\frac{1}{2}').scale(1.5)
        self.play(Transform(ratio_test, ratio_test_6))
        self.wait(1)

        ratio_test_final = MathTex(r'\frac{1}{2}', r'<', r'1').scale(1.5)
        self.play(Transform(ratio_test, ratio_test_final))
        self.wait(1)