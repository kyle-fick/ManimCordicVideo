from manim import *

class AngleAddProof(Scene):
    def construct(self):
        self.camera.background_color="#213d4c"

        lines = []
        pointLabels = [MathTex('A'),
                       MathTex('B'),
                       MathTex('C'),
                       MathTex('D'),
                       MathTex('E'),
                       MathTex('F')]
        lines.append(Line(start=LEFT*4 + DOWN*2, end=RIGHT*2.5 + UP*3, color=WHITE))
        pointLabels[0].next_to(lines[0].start, LEFT)
        pointLabels[1].next_to(lines[0].end, UP)
        lines.append(Line(start=lines[0].start, end=RIGHT*2.5 + DOWN * 2, color=WHITE))
        pointLabels[2].next_to(lines[1].end, DOWN)
        lines.append(Line(start=lines[1].end, end=lines[0].end, color=WHITE))
        lines.append(Line(start=lines[0].start, end=RIGHT*3.3 + UP, color=WHITE))
        pointLabels[3].next_to(lines[3].end, RIGHT)
        lines.append(Line(start=lines[3].end, end=lines[0].end, color=BLUE))
        for l in lines:
            self.play(Create(l))
        self.wait(1)

        self.play(Write(pointLabels[0]))
        self.play(Write(pointLabels[1]))
        self.play(Write(pointLabels[2]))
        self.play(Write(pointLabels[3]))
        self.wait(1)

        ra1 = RightAngle(lines[3], lines[4], 0.3, quadrant=(-1, 1))
        ra2 = RightAngle(lines[1], lines[2], 0.3, quadrant=(-1, 1))

        self.play(Create(ra1))
        self.play(Create(ra2))
        self.wait(1)

        angle1 = Angle(lines[3], lines[0], radius=1)
        angle2 = Angle(lines[1], lines[3], radius=.7)
        xTex = MathTex(r"x^\circ", color=BLUE).next_to(angle1, UP*.25 + RIGHT*1.3)
        yTex = MathTex(r"y^\circ", color=ORANGE).next_to(angle2).shift(RIGHT*.5 + UP*.25)

        oneTex = MathTex("1").move_to(lines[0]).shift(UP*.5)
        sinxTex = MathTex(r"\sin \left( x \right)", color=BLUE).move_to(lines[4]).shift(RIGHT*1.1)

        sinxyTex = MathTex(r"\sin \left( x + y \right)", color="#c26757").move_to(lines[2]).shift(RIGHT * 1.5 + DOWN * .5)
        cosxyTex = MathTex(r"\cos \left( x + y \right)", color="#c26757").move_to(lines[1]).shift(DOWN*.5)

        lines2 = []
        lines2.append(Line(start=lines[4].start, end=lines[4].start + DOWN * 3))
        lines2.append(Line(start=lines[1].end, end=lines2[0].end))
        lines2.append(Line(start=lines[4].start, end=lines[4].start + LEFT*.8))
        cosxsinyTex = MathTex(r"\cos \left( x \right) \sin \left( y \right)", color=ORANGE).move_to(lines2[0]).shift(RIGHT*2 + DOWN*.25)

        self.play(Create(angle1))
        self.play(Create(angle2))
        self.play(Write(xTex))
        self.play(Write(yTex))
        self.play(Write(oneTex))
        self.play(Write(sinxTex))
        self.wait(1)

        self.play(lines[2].animate.set_color("#c26757"))
        self.play(Write(sinxyTex))
        self.wait(1)

        self.play(lines[1].animate.set_color("#c26757"))
        self.play(Write(cosxyTex))
        self.wait(1)

        self.play(Create(lines2[0]), sinxyTex.animate.set_opacity(0.3))
        self.play(Create(lines2[1]))
        pointLabels[4].next_to(lines2[0].end, DR)
        self.play(Write(pointLabels[4]))
        self.wait(1)

        ra3 = RightAngle(lines2[0], lines2[1], 0.3, quadrant=(-1, -1))
        self.play(Create(ra3))

        cosxTex = MathTex(r"\cos \left( x \right)", color=BLUE).move_to(lines[3]).shift(DR * .4)
        self.play(lines[3].animate.set_color(BLUE))
        self.play(Write(cosxTex))
        self.wait(1)

        self.play(lines2[0].animate.set_color(ORANGE))
        self.play(Create(cosxsinyTex))
        self.wait(1)

        self.play(Create(lines2[2]))
        pointLabels[5].next_to(lines2[2].end, LEFT)
        self.play(Write(pointLabels[5]))
        self.play(Create(Angle(lines[2], lines[4], radius=.5, quadrant=(-1, -1))))
        self.wait(1)

        yTex2 = yTex.copy().shift(RIGHT * 5.02 + UP*3.7).scale(.6)
        self.play(Write(yTex2))
        self.wait(1)

        objects = Group(*self.mobjects)
        self.play(objects.animate.shift(DOWN))
        self.wait(1)

        sinxyTotal = MathTex(r"\sin (x + y)", "=", r"\overline{BF}", " + ", r"\overline{FC}").move_to(point_or_mobject=LEFT*3.5 + UP*3).scale(.75)
        self.play(Write(sinxyTotal))
        self.wait(1)

        sinxyLine1 = Line(lines[2].end + DOWN, lines[2].end + DOWN*3, color=GREEN)
        sinxyLine2 = Line(sinxyLine1.end, sinxyLine1.end + DOWN * 3, color=PURPLE)

        self.play(FadeIn(sinxyLine1))
        self.play(sinxyTotal[2].animate.set_color(GREEN))
        self.wait(1)

        sinxyTotalRep1 = MathTex(r"\sin (x + y)", "=", r"\sin (x) \cos (y)", " + ", r"\overline{FC}").move_to(sinxyTotal).scale(.75)
        sinxyTotalRep1[2].set_color(GREEN)
        sinxyTotalRep2 = MathTex(r"\sin (x + y)", "=", r"\sin (x) \cos (y)", " + ", r"\cos (x) \sin (y)").move_to(sinxyTotal).scale(.75)
        sinxyTotalRep2[2].set_color(GREEN)
        sinxyTotalRep2[4].set_color(PURPLE)


        self.play(TransformMatchingTex(sinxyTotal, sinxyTotalRep1))
        self.wait(1)

        self.play(sinxyTotalRep1[4].animate.set_color(PURPLE))
        self.play(FadeIn(sinxyLine2))
        self.wait(1)

        self.play(TransformMatchingTex(sinxyTotalRep1, sinxyTotalRep2))
        self.wait(1)

        cosxyLine1 = Line(lines[0].start + DOWN, lines2[0].end + DOWN, color=RED)
        cosxyLine2 = Line(lines[1].end + DOWN, lines2[0].end + DOWN, color=YELLOW)

        cosxyTotal = MathTex(r"\cos (x + y)", "=", r"\overline{AE}", " - ", r"\overline{CE}").move_to(point_or_mobject=LEFT*3.5 + UP*2).scale(.75)
        cosxyTotalRep1 = MathTex(r"\cos (x + y)", "=", r"\cos (x) \cos(y)", " - ", r"\overline{CE}").move_to(cosxyTotal).scale(.75)
        cosxyTotalRep1[2].set_color(RED)
        cosxyTotalRep2 = MathTex(r"\cos (x + y)", "=", r"\cos (x) \cos(y)", " - ", r"\sin (x) \sin (y)").move_to(cosxyTotal).scale(.75)
        cosxyTotalRep2[2].set_color(RED)
        cosxyTotalRep2[4].set_color(YELLOW)

        self.play(Write(cosxyTotal))
        self.play(cosxyTotal[2].animate.set_color(RED))
        self.play(FadeIn(cosxyLine1))
        self.wait(1)

        self.play(TransformMatchingTex(cosxyTotal, cosxyTotalRep1))
        self.play(cosxyTotalRep1[4].animate.set_color(YELLOW))
        self.play(FadeIn(cosxyLine2))
        self.wait(1)

        self.play(TransformMatchingTex(cosxyTotalRep1, cosxyTotalRep2))
        objects.add(sinxyLine1, sinxyLine2, cosxyLine1, cosxyLine2)
        self.wait(1)

        identities = VGroup(sinxyTotalRep2, cosxyTotalRep2)
        self.play(AnimationGroup(FadeOut(objects), identities.animate.move_to([0, 0, 0])))
        self.wait(1)

        self.play(sinxyTotalRep2.animate.set_color(WHITE), cosxyTotalRep2.animate.set_color(WHITE))
        self.wait(1)
