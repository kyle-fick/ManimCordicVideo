from manim import *

class CordicIdea(MovingCameraScene):
    def construct(self):
        self.camera.background_color="#213d4c"

        angle = ValueTracker(0)

        rotcirc = Circle(3.5, WHITE)
        circAxes = Axes([-2, 2], [-2, 2], rotcirc.radius * 2, rotcirc.radius * 2, axis_config={'include_ticks': True}, tips=False).move_to(rotcirc)
        circGroup = Group(rotcirc, circAxes)

        self.play(Create(rotcirc), Create(circAxes))
        self.wait(1)

        vector = Arrow(start=circAxes.coords_to_point(0, 0), end=circAxes.coords_to_point(1, 0), color=BLUE_B, buff=0)
        arrow_updater = lambda a: a.become(Arrow(start=circAxes.coords_to_point(0, 0), end=circAxes.coords_to_point(np.cos(angle.get_value()), np.sin(angle.get_value())), color=BLUE_B, buff=0))
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

        asumTex = MathTex(r'\sum_{n=0}^{\infty} 45 (\frac{1}{2^n}) = 90\\ = 45 + 22.5 + \cdots').shift(RIGHT * 3.5)
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
        self.play(FadeIn(circle_shade2))
        self.wait(1)

        self.play(FadeOut(circle_shade1), FadeOut(circle_shade2))
        self.wait(1)

        self.play(rotateVect(PI/2))
        new_angle_mark.remove_updater(new_angle_updater)
        self.play(FadeOut(new_angle_mark))
        self.wait(1)

        self.play(self.camera.frame.animate.scale(0.6).move_to(rotcirc.get_center() + RIGHT * 2 + UP * 1.5), run_time=2)
        self.wait(1)

        angle_mark.add_updater(mark_lambda)
        self.add(angle_mark)
        