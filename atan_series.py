from manim import *

class AtanSeries(Scene):
    def construct(self):
        self.camera.background_color="#213d4c"
        
        atan_series = MathTex(r"\sum_{n=0}^{\infty} \tan^{-1} \left(\frac{1}{2^n}\right)")
        self.play(Write(atan_series))
        self.wait(1)

        angle_series = MathTex(r'\approx', r'45', r'+', r'22.625', r'+', r'\cdots')
        self.play(atan_series.animate.shift(UP), Write(angle_series.shift(DOWN)))
        self.wait(1)

        ratio_test = MathTex(r'\lim_{n\to\infty}', r'\left|', r'a_{n+1} \over a_{n}', r'\right|')
        self.play(Write(ratio_test.shift(DOWN * 3)))
        self.wait(1)
