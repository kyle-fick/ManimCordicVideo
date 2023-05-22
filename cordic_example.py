from manim import *

class CordicExample(MovingCameraScene):
    def construct(self):
        self.camera.background_color="#213d4c"

        vec_mode = False

        circ = Circle(3.5, WHITE)
        axes = Axes([-2, 2, 0.2], [-2, 2, 0.2], circ.radius * 2, circ.radius * 2, axis_config={'include_ticks': True}, tips=False).move_to(circ)

        self.play(Create(circ), Create(axes))
        self.wait(1)
        self.play(self.camera.frame.animate.scale(0.7).move_to(circ.get_center() + RIGHT * 3.5 + UP * 2))
        self.wait(1)

        k = MathTex(r'K', color=RED).scale(0.6)
        const_val = 0.607253
        mat = MobjectMatrix([[MathTex(r'1'),                                                           MathTex(r'- \tan (', r'\alpha', r')').set_color_by_tex(r'\alpha', PURPLE)],
                             [MathTex(r'\tan (', r'\alpha', r')').set_color_by_tex(r'\alpha', PURPLE), MathTex(r'1')]], h_buff=2, element_alignment_corner=ORIGIN).scale(0.6)
        xy_vec = MobjectMatrix([[MathTex(r'x').set_color(BLUE)],
                                [MathTex(r'y').set_color(YELLOW)]]).scale(0.6)
        xpyp_vec = MobjectMatrix([[MathTex(r"x'").set_color(BLUE)],
                                  [MathTex(r"y'").set_color(YELLOW)]]).scale(0.6)
        eq_sign = MathTex(r'=').scale(0.6)

        mat_eq = VGroup(k, mat, xy_vec, eq_sign, xpyp_vec)        
        mat_eq_pos = UP * 4 + RIGHT * 4.5

        mat_list = [mat]

        x_var = Variable(1, MathTex('x', color=BLUE), num_decimal_places=3).next_to(mat_eq, DOWN).shift(RIGHT * 2 + DOWN * 0.5)
        y_var = Variable(0, MathTex('y', color=YELLOW), num_decimal_places=3).next_to(x_var, DOWN)
        sum_ang = Variable(0, MathTex(r'\theta', color=GREEN), num_decimal_places=3).next_to(y_var, DOWN).shift(DOWN)

        vec = Arrow(start=circ.get_center(), end=axes.c2p(x_var.tracker.get_value(), y_var.tracker.get_value()), buff=0, color=BLUE_B)
        vec.add_updater(lambda v: v.become(Arrow(start=circ.get_center(), end=axes.c2p(x_var.tracker.get_value(), y_var.tracker.get_value()), buff=0, color=BLUE_B)))

        xy_label = MathTex(r'({{x}}, {{y}})').set_color_by_tex('x', BLUE).set_color_by_tex('y', YELLOW).scale(0.6)
        xy_back = BackgroundRectangle(xy_label, BLACK, fill_opacity=0.7, buff=0.1, corner_radius=0.2)
        xy_group = Group(xy_back, xy_label)
        xy_group.add_updater(lambda g: g.next_to(vec, UR))

        target_angle = 37

        target_line = DashedLine(start=circ.get_center(), end=axes.c2p(np.cos(np.deg2rad(target_angle)) * 2, np.sin(np.deg2rad(target_angle)) * 2), color=GREEN)

        def update_angle(new_angle):
            rnd_ang_str = str(round(new_angle, 3))
            mat_list.append(MobjectMatrix([[MathTex(r'1'),                                                               MathTex(r'- \tan (', rnd_ang_str, r')').set_color_by_tex(rnd_ang_str, PURPLE)],
                                           [MathTex(r'\tan (', rnd_ang_str, r')').set_color_by_tex(rnd_ang_str, PURPLE), MathTex(r'1')]], h_buff=2.5, element_alignment_corner=ORIGIN).move_to(mat).scale(0.6))
            self.play(*[TransformMatchingTex(mat_list[-2][i], mat_list[-1][i]) for i in range(3)])
            mat_eq.insert(1, mat_list[-1])
            mat_eq.remove(mat_list[-2])
            self.play(mat_eq.animate.arrange().move_to(mat_eq_pos), run_time=0.2)

            ang_tan = np.tan(np.deg2rad(new_angle))

            if(vec_mode):
                self.play(x_var.tracker.animate.set_value(x_var.tracker.get_value() - y_var.tracker.get_value() * ang_tan),
                        y_var.tracker.animate.set_value(x_var.tracker.get_value() * ang_tan + y_var.tracker.get_value()),
                        sum_ang.tracker.animate.set_value(sum_ang.tracker.get_value() - new_angle))
            else:
                self.play(x_var.tracker.animate.set_value(x_var.tracker.get_value() - y_var.tracker.get_value() * ang_tan),
                        y_var.tracker.animate.set_value(x_var.tracker.get_value() * ang_tan + y_var.tracker.get_value()),
                        sum_ang.tracker.animate.set_value(sum_ang.tracker.get_value() + new_angle))
            

        self.play(Create(mat_eq.arrange().move_to(mat_eq_pos)))
        self.wait(1)
        if(vec_mode):
            self.play(Create(vec), FadeIn(xy_group))
        else:
            self.play(Create(vec), FadeIn(xy_group), Create(target_line))
        self.wait(1)
        self.play(Create(x_var.next_to(mat_eq, DOWN).shift(RIGHT + DOWN * 0.5)), Create(y_var.next_to(x_var, DOWN)), Create(sum_ang.next_to(y_var, DOWN).shift(DOWN)))

        if(vec_mode):
            for i in range(10):
                if(y_var.tracker.get_value() < 0):
                    update_angle(np.rad2deg(np.arctan((1/2)**i)))
                else:
                    update_angle(-np.rad2deg(np.arctan((1/2)**i)))
                self.wait(1)

            ang_rect = SurroundingRectangle(sum_ang, color=RED)
            self.play(Create(ang_rect))
            self.wait(1)

            self.play(x_var.tracker.animate.set_value(x_var.tracker.get_value() * const_val))
            self.wait(1)
            self.play(ReplacementTransform(ang_rect, SurroundingRectangle(x_var, color=RED)))
            self.wait(1)

        else:
            for i in range(10):
                if(sum_ang.tracker.get_value() < target_angle):
                    update_angle(np.rad2deg(np.arctan((1/2)**i)))
                else:
                    update_angle(-np.rad2deg(np.arctan((1/2)**i)))
                self.wait(1)

            k_rect = SurroundingRectangle(k, color=RED)
            self.play(Create(k_rect))
            self.wait(1)
            self.play(FadeOut(k_rect))
            self.wait(1)
            
            k_2 = MathTex('K', color=RED).move_to(self.camera.frame.get_center())
            vec.suspend_updating()
            self.play(ReplacementTransform(k, k_2), 
                    FadeOut(xy_group, vec, target_line, circ, x_var, y_var, sum_ang, mat_list[-1], xy_vec, xpyp_vec, eq_sign, axes))
            self.wait(1)

            cos_prod = MathTex(r'\prod_{n=0}^{\infty} \cos (', r'\alpha_{n}', r') \approx', str(const_val)).move_to(k_2).set_color_by_tex(r'\alpha_{n}', PURPLE)
            self.play(ReplacementTransform(k_2, cos_prod))
            self.wait(1)

            x_var.move_to(cos_prod).shift(UR)
            y_var.move_to(cos_prod).shift(DR)
            const1 = MathTex(str(const_val), r'\cdot').next_to(x_var, LEFT)
            const2 = MathTex(str(const_val), r'\cdot').next_to(y_var, LEFT)
            self.play(FadeIn(x_var, y_var),
                    TransformMatchingTex(cos_prod, const1),
                    TransformMatchingTex(cos_prod.copy(), const2))
            self.play(x_var.tracker.animate.set_value(x_var.tracker.get_value() * const_val),
                    y_var.tracker.animate.set_value(y_var.tracker.get_value() * const_val))
            self.wait(1)

            cos_t = MathTex(r'\cos (', r'\theta', r') =').set_color_by_tex(r'\theta', GREEN).move_to(x_var.label).scale(0.6)
            sin_t = MathTex(r'\sin (', r'\theta', r') =').set_color_by_tex(r'\theta', GREEN).move_to(y_var.label).scale(0.6)
            self.play(Transform(x_var.label, cos_t), Transform(y_var.label, sin_t),
                    FadeOut(const1, const2))
            self.wait(1)

            sol_rect = SurroundingRectangle(Group(x_var, y_var), color=RED)
            self.play(Create(sol_rect))
            self.wait(1)