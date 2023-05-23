from manim import *

class Outro(Scene):
    def construct(self):
        self.camera.background_color="#213d4c"

        sinx = MathTex(r'\sin (x)').move_to(UP * 2 + LEFT * 1.5).scale(1.5)
        cosx = MathTex(r'\cos (x)').move_to(RIGHT)
        atanx = MathTex(r'\tan^{-1} (x)').move_to(DOWN * 2.5 + LEFT)
        lnx = MathTex(r'\ln (x)').move_to(RIGHT * 3 + UP * 2).scale(1.5)
        ex = MathTex(r'e^x').move_to(LEFT * 4).scale(1.5)
        sqrtx = MathTex(r'\sqrt{x}').move_to(RIGHT * 4 + DOWN * 2).scale(1.5)
        cordic_title = Title('C.O.R.D.I.C.', color=YELLOW, match_underline_width_to_text=True)

        self.add(cordic_title)
        self.wait(1)
        self.play(LaggedStart(FadeIn(sinx), FadeIn(cosx), FadeIn(atanx), FadeIn(lnx), FadeIn(ex), FadeIn(sqrtx)))
        self.wait(1)