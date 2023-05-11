from manim import *

class AtanSeries(Scene):
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

        self.play(FadeOut(atan_series), FadeOut(angle_series), FadeOut(ratio_rect), ratio_test.animate.move_to(ORIGIN))
        self.wait(1)

        ratio_test_2 = MathTex(r'\lim_{n\to\infty}', r'\left| \tan^{-1} \left( \frac{1}{2^{n+1}} \right) \over \tan^{-1} \left( \frac{1}{2^n} \right) \right|').scale(1.5)
        self.play(Transform(ratio_test, ratio_test_2))
        self.wait(1)

        ratio_test_3 = MathTex(r'\lim_{n\to\infty}', r'\left| \frac{2^{n+1} \ln(2)}{1 + 4^{n+1}} \over \frac{2^n \ln(2)}{1 + 4^n} \right|').scale(1.5)
        self.play(Transform(ratio_test, ratio_test_3))
        self.wait(1)

        ratio_test_4 = MathTex(r'\lim_{n\to\infty}', r'2 \cdot \frac{4^n + 1}{4^{n+1} + 1}').scale(1.5)
        self.play(Transform(ratio_test, ratio_test_4))
        self.wait(1)

        ratio_test_5 = MathTex(r'\lim_{n\to\infty}', r'\frac{1}{2} \cdot \frac{4^x + 1}{4^x + \frac{1}{4}}').scale(1.5)
        self.play(Transform(ratio_test, ratio_test_5))
        self.wait(1)

        ratio_test_final = MathTex(r'\frac{1}{2}').scale(1.5)
        self.play(Transform(ratio_test, ratio_test_final))
        self.wait(1)