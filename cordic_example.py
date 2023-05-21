from manim import *

class CordicExample(MovingCameraScene):
    def construct(self):
        self.camera.background_color="#213d4c"

        circ = Circle(3.5, WHITE)
        axes = Axes([-2, 2, 0.2], [-2, 2, 0.2], circ.radius * 2, circ.radius * 2, axis_config={'include_ticks': True}, tips=False).move_to(circ)

        self.play(Create(circ), Create(axes))
        self.wait(1)
        self.play(self.camera.frame.animate.scale(0.7).move_to(circ.get_center() + RIGHT * 3.5 + UP * 2))
        self.wait(1)

        k = MathTex(r'K', color=RED).scale(0.6)
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

        target_angle = 55

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

            self.play(x_var.tracker.animate.set_value(x_var.tracker.get_value() - y_var.tracker.get_value() * ang_tan),
                      y_var.tracker.animate.set_value(x_var.tracker.get_value() * ang_tan + y_var.tracker.get_value()),
                      sum_ang.tracker.animate.set_value(sum_ang.tracker.get_value() + new_angle))

        self.play(Create(mat_eq.arrange().move_to(mat_eq_pos)))
        self.wait(1)
        self.play(Create(vec), FadeIn(xy_group), Create(target_line))
        self.wait(1)
        self.play(Create(x_var.next_to(mat_eq, DOWN).shift(RIGHT + DOWN * 0.5)), Create(y_var.next_to(x_var, DOWN)), Create(sum_ang.next_to(y_var, DOWN).shift(DOWN)))

        for i in range(10):
            if(sum_ang.tracker.get_value() < target_angle):
                update_angle(np.rad2deg(np.arctan((1/2)**i)))
            else:
                update_angle(-np.rad2deg(np.arctan((1/2)**i)))
            self.wait(1)
        