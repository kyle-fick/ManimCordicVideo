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
        
        fgsum_tex = MathTex(r'\sum_{n=0}^{{{N}}}', r'{{a}}{{r}}^{{n}}').set_color_by_tex('a', RED).set_color_by_tex('r', color=GREEN).set_color_by_tex('n', YELLOW)
        fgsum_tex[0].set_color(WHITE)
        self.play(TransformMatchingTex(gsumTex, fgsum_tex))
        self.wait(1)
        
        expanded_sum = MathTex(r'{{a}}', '+', r'{{a}}{{r}}', '+', r'\cdots', '+', r'{{a}}{{r}}^{{{N}} - 1}', color=WHITE).set_color_by_tex('a', RED).set_color_by_tex('r', GREEN)
        eq_sign = MathTex('=')
        ceq_sign = eq_sign.copy()
        g_series = Group(fgsum_tex, eq_sign, expanded_sum)
        self.play(FadeIn(eq_sign), FadeIn(expanded_sum), g_series.animate.arrange_submobjects())
        self.wait(1)
        
        ofgsum_tex = fgsum_tex.copy()
        oexpanded_sum = expanded_sum.copy()
        nfgsum_tex = MathTex(r'{{r}}', r'\cdot', '\sum_{n=0}^{{{N}}}', r'{{a}}{{r}}^{{n}}').set_color_by_tex('a', RED).set_color_by_tex('r', color=GREEN).set_color_by_tex('n', YELLOW)
        nfgsum_tex[1].set_color(WHITE)
        nfgsum_tex[2].set_color(WHITE)
        nexpanded_sum = MathTex(r'{{a}}{{r}}', '+', r'{{a}}{{r}}^2', '+', r'\cdots', '+', r'{{a}}{{r}}^{{{N}}}', color=WHITE).set_color_by_tex('a', RED).set_color_by_tex('r', GREEN)
        
        ng_series = Group(nfgsum_tex, ceq_sign, nexpanded_sum)
        ng_series.arrange_submobjects()
        self.play(TransformMatchingTex(fgsum_tex, nfgsum_tex), TransformMatchingTex(eq_sign, ceq_sign), TransformMatchingTex(expanded_sum, nexpanded_sum))
        self.wait(1)
        
        og_series = Group(ofgsum_tex, eq_sign, oexpanded_sum).arrange_submobjects()
        self.play(ng_series.animate.shift(DOWN), FadeIn(og_series.shift(UP)))
        self.wait(1)