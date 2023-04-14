from manim import *

# prove convergence of geometric series
class ConvergentSeries(Scene):
    def construct(self):
        self.camera.background_color="#213d4c"

        asumTex = MathTex(r'\sum_{n=0}^{\infty}',  r'45 (\frac{1}{2^{{n}}})')
        self.play(Write(asumTex))
        self.wait(1)

        gsumTex = MathTex(r'\sum_{n=0}^{\infty}', r'{{a}}{{r}}^{{n}}').set_color_by_tex('a', RED).set_color_by_tex('r', color=GREEN).set_color_by_tex('n', YELLOW)
        gsumTex[0].set_color(WHITE)
        self.play(TransformMatchingTex(asumTex, gsumTex))
        self.wait(1)