from manim import *

class WalkIntro(ZoomedScene):
    def construct(self):
        self.camera.background_color="#213d4c"

        # dist_to_end = 7.5613
        dist_to_end = 6.5334

        walk_line = NumberLine(length=10, x_range=[0, 10], color=WHITE, include_numbers=True)
        point = Dot(walk_line.start, color=RED).move_to(walk_line.n2p(0))

        self.play(Create(walk_line))
        self.wait(1)
        self.play(Create(point))
        self.wait(1)

        dest = DashedLine(walk_line.n2p(dist_to_end) + DOWN, walk_line.n2p(dist_to_end) + UP, color=YELLOW)
        self.play(Create(dest))
        self.wait(1)

        br = Brace(Group(point, dest))
        self.play(FadeIn(br))
        self.wait(1)

        q_tex = Tex('?').next_to(br, DOWN)
        self.play(Write(q_tex))
        self.wait(1)

        self.play(FadeOut(br), FadeOut(q_tex))
        self.wait(1)

        dist_sum = ValueTracker(0)

        sum_dist_tex = MathTex(r'\Sigma', r'd', r'=').set_color_by_tex(r'd', GREEN)
        sum_dist_num = DecimalNumber(0, num_decimal_places=4)
        sum_group = VGroup(sum_dist_tex, sum_dist_num).arrange_submobjects()
        sum_group.move_to(UP * 3)
        self.play(FadeIn(sum_group))
        self.wait(1)

        sum_dist_num.add_updater(lambda x: x.set_value(dist_sum.get_value()))
        point.add_updater(lambda x: x.move_to(walk_line.n2p(dist_sum.get_value())))

        for i in range(10):
            if dist_sum.get_value() < dist_to_end:
                self.play(dist_sum.animate.set_value(dist_sum.get_value() + walk_line.get_length() * (1/2)**(i+1)))
                self.wait(0.5)
            else:
                self.play(dist_sum.animate.set_value(dist_sum.get_value() - walk_line.get_length() * (1/2)**(i+1)))
                self.wait(0.5)
                
        self.wait(1)