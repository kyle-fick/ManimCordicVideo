from manim import *

# prove convergence of geometric series
class ConvergentSeries(Scene):
    def construct(self):
        self.camera.background_color="#213d4c"

        asumTex = MathTex(r'\sum_{n=0}^{\infty}',  r'45 (\frac{1}{2^n})')
        self.play(Write(asumTex))
        self.wait(1)

        gsumTex = MathTex(r'\sum_{n=0}^{{{\infty}}}', r'{{a}}{{r}}^{{n}}').set_color_by_tex('a', RED).set_color_by_tex('r', color=GREEN).set_color_by_tex('n', YELLOW)
        gsumTex[0].set_color(WHITE)
        gsumTex[1].set_color(WHITE)
        self.play(ReplacementTransform(asumTex, gsumTex))
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

        tg_sub = MathTex(r'\sum_{n=0}^{{{N}}}', r'{{a}}{{r}}^{{n}}', r'-', r'{{r}}', r'\cdot', r'\sum_{n=0}^{{{N}}}', r'{{a}}{{r}}^{{n}}', color=WHITE).set_color_by_tex('a', RED).set_color_by_tex('r', color=GREEN).set_color_by_tex('n', YELLOW)
        tg_sub[0].set_color(WHITE)
        tg_sub[7].set_color(WHITE)
        tg_sub[10].set_color(WHITE)
        eq_sign_2 = MathTex('=', color=WHITE)
        tg_exp = MathTex(r'{{a}}', r'-', r'{{a}}{{r}}^{{N}}', color=WHITE).set_color_by_tex('a', RED).set_color_by_tex('r', GREEN)

        tg_series = Group(tg_sub, eq_sign_2, tg_exp).arrange_submobjects()
        self.play(ReplacementTransform(Group(ng_series, og_series), tg_series))
        self.wait(1)
        
        fg_left = MathTex(r'(1 - {{r}})', r'\sum_{n=0}^{{{N}}}', r'{{a}}{{r}}^{{n}}', color=WHITE).set_color_by_tex('a', RED).set_color_by_tex('r', color=GREEN).set_color_by_tex('n', YELLOW)
        fg_left[3].set_color(WHITE)
        fg_right = MathTex(r'{{a}}', r'(1 - {{r}}^{{N}})').set_color_by_tex('a', RED).set_color_by_tex('r', GREEN)
        eq_sign_3 = MathTex('=', color=WHITE)

        fg_series = Group(fg_left, eq_sign_3, fg_right).arrange_submobjects()
        self.play(ReplacementTransform(tg_series, fg_series))
        self.wait(1)

        lg_left = MathTex(r'\sum_{n=0}^{{{N}}}', r'{{a}}{{r}}^{{n}}', color=WHITE).set_color_by_tex('a', RED).set_color_by_tex('r', color=GREEN).set_color_by_tex('n', YELLOW)
        lg_left[0].set_color(WHITE)
        lg_right = MathTex(r'{ {{a}} (1 - {{r}}^{{N}}) }',  r'\over{ (1 - {{r}}) }').set_color_by_tex('a', RED).set_color_by_tex('r', GREEN)
        lg_right[7].set_color(WHITE)
        eq_sign_4 = MathTex('=', color=WHITE)
        
        lg_series = Group(lg_left, eq_sign_4, lg_right).arrange_submobjects()
        self.play(ReplacementTransform(fg_series, lg_series))
        self.wait(1)

        lim_tex_1 = MathTex(r'\lim_{N \to \infty}', color=WHITE)
        lim_tex_2 = lim_tex_1.copy()
        lg_series.insert(0, lim_tex_1)
        lg_series.insert(3, lim_tex_2)
        self.play(FadeIn(lim_tex_1), FadeIn(lim_tex_2), lg_series.animate.arrange_submobjects())
        self.wait(1)

        ratio_tex = MathTex(r'|{{r}}| < 1').set_color_by_tex('r', GREEN)
        self.play(lg_series.animate.shift(UP), FadeIn(ratio_tex.shift(DOWN)))
        self.wait(1)

        mul_tex = MathTex(r'{{r}} = ', r'0.5').set_color_by_tex('r', GREEN).shift(UP * .5)
        mul_num = DecimalNumber(0.5, 4).shift(DOWN * .5)
        mul_example = Group(mul_tex, mul_num)
        self.play(ratio_tex.animate.shift(LEFT), FadeIn(mul_example.next_to(ratio_tex, RIGHT)))
        self.wait(1)        

        self.play(mul_num.animate.set_value(0.25))
        self.play(mul_num.animate.set_value(0.125))
        self.play(mul_num.animate.set_value(0.0625))
        self.play(FadeOut(mul_example), FadeOut(ratio_tex), lg_series.animate.shift(DOWN))
        self.wait(1)

        self.play(FadeOut(lim_tex_2))
        lg_series.remove(lim_tex_2)
        nlg_right = MathTex(r'{{a}}', r'\over (1 - {{r}})').set_color_by_tex('a', RED).set_color_by_tex('r', GREEN).move_to(lg_right)
        nlg_right[1].set_color(WHITE)
        self.play(TransformMatchingTex(lg_right, nlg_right))
        lg_series.insert(3, nlg_right)
        lg_series.remove(lg_right)
        self.play(lg_series.animate.arrange_submobjects())
        self.wait(1)

        asumTex = MathTex(r'\sum_{n=0}^{\infty}',  r'45 (\frac{1}{2^n})')
        eq_sign_5 = MathTex('=', color=WHITE)
        c_sum_result = MathTex(r'\frac{45}{\left( 1-\frac{1}{2} \right) }')
        c_sum_fresult = MathTex(r'90')
        c_sum = Group(asumTex, eq_sign_5, c_sum_result).arrange_submobjects()
        c_sum.shift(UP)
        self.play(FadeIn(c_sum), lg_series.animate.shift(DOWN))
        self.wait(1)

        self.play(ReplacementTransform(c_sum_result, c_sum_fresult.move_to(c_sum_result)))
        c_sum.insert(2, c_sum_fresult)
        c_sum.remove(c_sum_result)
        self.play(c_sum.animate.arrange_submobjects().shift(UP))
        self.wait(1)