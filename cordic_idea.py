from manim import *

class CordicIdea(MovingCameraScene):
    def construct(self):
        self.camera.background_color="#213d4c"

        angle = ValueTracker(0)

        rotcirc = Circle(3.5, WHITE)
        circAxes = Axes([-2, 2, 0.2], [-2, 2, 0.2], rotcirc.radius * 2, rotcirc.radius * 2, axis_config={'include_ticks': True}, tips=False).move_to(rotcirc)
        circGroup = Group(rotcirc, circAxes)

        self.play(Create(rotcirc), Create(circAxes))
        self.wait(1)

        vector = Arrow(start=circAxes.c2p(0, 0), end=circAxes.c2p(1, 0), color=BLUE_B, buff=0)
        arrow_updater = lambda a: a.become(Arrow(start=circAxes.c2p(0, 0), end=circAxes.c2p(np.cos(angle.get_value()), np.sin(angle.get_value())), color=BLUE_B, buff=0))
        vector.add_updater(arrow_updater)
        angle_mark = Arc(.5, 0, 0)
        mark_lambda = lambda a: a.become(Arc(.5, 0, angle.get_value()))
        angle_mark.add_updater(mark_lambda)
        
        def updateLabel(m):
            m.next_to(angle_mark, UR, buff=SMALL_BUFF)
            m.set_value(angle.get_value() * 180 / PI)
        
        angle_label = DecimalNumber(0, color=GREEN).next_to(angle_mark, UR, buff=SMALL_BUFF)
        angle_lambda = lambda m: updateLabel(m)
        angle_label.add_updater(angle_lambda)

        self.play(Create(vector))
        self.add(angle_mark)
        self.play(FadeIn(angle_label))
        self.wait(1)

        def rotateVect(ang):
            return angle.animate.set_value(angle.get_value() + ang)

        rotAngles = []
        for i in range(10):
            rotAngles.append(PI/4 * (np.power(.5, i)))

        for i in rotAngles:
            self.play(rotateVect(i))
            self.wait(0.2)

        angle_label.remove_updater(angle_lambda)
        angle_mark.remove_updater(mark_lambda)
        vector.remove_updater(arrow_updater)
        currScene = Group(*self.mobjects)
        currScene.remove(angle)
        self.play(currScene.animate.shift(LEFT * 3))

        asumTex = MathTex(r'\sum_{n=0}^{\infty} 45 \left(\frac{1}{2^n}\right) = 90\\ = 45 + 22.5 + \cdots').shift(RIGHT * 3.5)
        self.play(FadeIn(asumTex))
        self.wait(1)

        self.play(currScene.animate.move_to(ORIGIN), FadeOut(asumTex))
        self.play(FadeOut(angle_label), FadeOut(angle_mark))
        self.remove(angle_label, angle_mark)
        angle.set_value(PI / 2)
        self.add(angle)
        self.wait(1)

        new_angle_mark = Arc(.5, 0, 0)
        new_angle_updater = lambda a: a.become(Arc(.5, angle.get_value(), PI/2 - angle.get_value()))
        new_angle_mark.add_updater(new_angle_updater)

        vector.add_updater(arrow_updater)
        self.add(new_angle_mark)

        self.play(rotateVect(-PI))
        self.wait(1)

        circle_shade1 = Arc(rotcirc.radius, -PI/2, PI, fill_color=BLUE_C, fill_opacity=.4)
        circle_shade2 = Arc(rotcirc.radius,  PI/2, PI, fill_color=BLUE_C, fill_opacity=.4)
        self.play(FadeIn(circle_shade1))
        self.wait(1)

        q2_vec = Arrow(start=circAxes.c2p(0, 0), end=circAxes.c2p(np.cos(3*PI/4), np.sin(3*PI/4)), color=RED_B, buff=0)
        q3_vec = Arrow(start=circAxes.c2p(0, 0), end=circAxes.c2p(np.cos(-3*PI/4), np.sin(-3*PI/4)), color=RED_B, buff=0)
        self.play(Create(q2_vec))
        self.play(Create(q3_vec))
        self.wait(1)
        self.play(Rotate(q2_vec, -PI/2, about_point=rotcirc.get_center()))
        self.play(Rotate(q3_vec, PI/2, about_point=rotcirc.get_center()))
        self.wait(1)

        self.play(FadeIn(circle_shade2))
        self.wait(1)

        self.play(FadeOut(circle_shade1), FadeOut(circle_shade2), FadeOut(q2_vec), FadeOut(q3_vec))
        self.wait(1)

        self.play(rotateVect(PI/2))
        new_angle_mark.remove_updater(new_angle_updater)
        self.play(FadeOut(new_angle_mark))
        self.wait(1)

        self.play(self.camera.frame.animate.scale(0.6).move_to(rotcirc.get_center() + RIGHT * 2 + UP * 1.5), run_time=2)
        self.wait(1)

        angle_mark.add_updater(mark_lambda)
        self.add(angle_mark)
        desired_angle = PI/3
        angle_line = DashedLine(start=rotcirc.get_center(), end=rotcirc.get_center() + RIGHT * np.cos(desired_angle) * rotcirc.get_radius() + UP * np.sin(desired_angle) * rotcirc.get_radius(), color=GREEN)
        self.play(Create(angle_line))
        self.wait(1)
        for i in range(len(rotAngles)):
            a = 1 if angle.get_value() < desired_angle else -1
            self.play(rotateVect(rotAngles[i] * a))
            self.wait(0.2)
        self.wait(1)

        y_tex = MathTex(r'y = \sin (\theta)', color=YELLOW).next_to(rotcirc, RIGHT).shift(UP * 3)
        x_tex = MathTex(r'x = \cos (\theta)', color=BLUE).next_to(y_tex, DOWN)
        y_line = DashedLine(start = vector.get_end(), end = rotcirc.get_center() + RIGHT * np.cos(angle.get_value()) * vector.get_length(), color=YELLOW)
        x_line = DashedLine(start = vector.get_end(), end = rotcirc.get_center() + UP * np.sin(angle.get_value()) * vector.get_length(), color=BLUE)
        self.play(Write(y_tex), Create(y_line))
        self.wait(1)
        self.play(Write(x_tex), Create(x_line))
        self.wait(1)

        self.play(FadeOut(x_line), FadeOut(y_line), FadeOut(angle_line))
        self.wait(1)

        invtan_tex = MathTex(r'\tan^{-1}\left( {{y}} \over{{{x}}}\right) = \theta', color=WHITE).next_to(x_tex, DOWN).set_color_by_tex('y', YELLOW).set_color_by_tex('x', BLUE).scale(.7).shift(DOWN * .5)
        self.play(Write(invtan_tex))
        self.wait(1)

        angle.set_value(PI/3)
        desired_angle = 0
        theta_tex = MathTex(r'\Sigma \theta = ')
        atan_angle = DecimalNumber(0, color=GREEN).set_value(desired_angle * 180 / PI)
        atan_angle_updater = lambda a: a.set_value(60 - angle.get_value() * 180 / PI)
        atan_angle.add_updater(atan_angle_updater)
        theta_group = VGroup(theta_tex, atan_angle).arrange_submobjects().next_to(invtan_tex, DOWN)
        self.play(Write(theta_group))
        self.wait(1)
        for i in range(len(rotAngles)):
            a = 1 if angle.get_value() < desired_angle else -1
            self.play(rotateVect(rotAngles[i] * a))
            self.wait(0.2)
        self.wait(1)
