from manim import *

class AtanSeries(Scene):
    def construct(self):
        self.camera.background_color="#213d4c"
        
        atan_series = MathTex(r"\sum_{n=0}^{\infty} \tan^{-1} \left(\frac{1}{2^n}\right)")
        self.play(Write(atan_series))
        self.wait(1)

        angle_series = MathTex(r'\approx', r'45', r'+', r'22.625', r'+', r'\cdots')
        self.play(atan_series.animate.shift(UP*2), Write(angle_series.shift(DOWN*0.5)))
        self.wait(1)

        # not showing right abs value side for some reason
        ratio_test = MathTex(r'\lim_{n\to\infty}', r'\left| a_{n+1} \over a_{n} \right|', r'<', r'1')
        self.play(Write(ratio_test.shift(DOWN * 2)))
        self.wait(1)
