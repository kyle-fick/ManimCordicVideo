from manim import *

class CordicMatrices(Scene):
    def construct(self):
        self.camera.background_color="#213d4c"

        identities = Group(MathTex(r"\sin (x + y)", "=", r"\sin (x) \cos (y)", " + ", r"\cos (x) \sin (y)").shift(UP*.5).scale(.75),
                           MathTex(r"\cos (x + y)", "=", r"\cos (x) \cos(y)", " - ", r"\sin (x) \sin (y)").shift(DOWN*.5).scale(.75))
        identities.move_to(ORIGIN)
        self.add(identities)
        self.wait(1)

        xeq = MathTex('x', '=', r'r \cdot \cos (\theta )').shift(UP*.5).scale(.75)
        xeq[0].set_color(ORANGE)
        yeq = MathTex('y', '=', r'r \cdot \sin (\theta )').shift(DOWN*.5).scale(.75)
        yeq[0].set_color(YELLOW)
        oeqs = Group(xeq, yeq)        

        self.play(identities.animate.shift(UP * 2))
        self.play(FadeIn(oeqs))

        xpeq = MathTex(r"x'", r'=', r'r \cdot \cos (\theta + \alpha )').shift(UP*.5).scale(.75)
        xpeq[0].set_color(ORANGE)
        ypeq = MathTex(r"y'", r'=', r'r \cdot \sin (\theta + \alpha )').shift(DOWN*.5).scale(.75)
        ypeq[0].set_color(YELLOW)
        peqs = Group(xpeq, ypeq)

        self.play(FadeIn(peqs.shift(DOWN * 2)))

        xnpeq = MathTex(r"x'", r'=', r'r \left( \cos ( \theta ) \cos( \alpha )', " - ", r"\sin ( \theta ) \sin ( \alpha ) \right)").shift(UP*.5).scale(.75)
        xnpeq[0].set_color(ORANGE)
        ynpeq = MathTex(r"y'", r'=', r'r \left( \sin ( \theta ) \cos ( \alpha )', " + ", r"\cos ( \theta ) \sin ( \alpha ) \right)").shift(DOWN*.5).scale(.75)
        ynpeq[0].set_color(YELLOW)
        npeqs = Group(xnpeq, ynpeq)

        self.play(oeqs.animate.shift(UP), ReplacementTransform(Group(peqs, identities), npeqs.move_to(DOWN)))

        focusRect1 = SurroundingRectangle(oeqs, color=RED, buff=MED_SMALL_BUFF)
        focusRect2 = SurroundingRectangle(oeqs[0], color=RED, buff=MED_SMALL_BUFF)
        focusRect3 = SurroundingRectangle(oeqs[1], color=RED, buff=MED_SMALL_BUFF)

        xnpeqe = MathTex(r"x'", r'=', r'r \cdot \cos ( \theta )', r'\cos ( \alpha )', " - ", r"r \cdot \sin ( \theta )", r"\sin ( \alpha )").shift(UP*.5 + DOWN).scale(.75)
        xnpeqe[0].set_color(ORANGE)
        ynpeqe = MathTex(r"y'", r'=', r'r \cdot \sin ( \theta )', r'\cos ( \alpha )', " + ", r"r \cdot \cos ( \theta )", r"\sin ( \alpha )").shift(DOWN*.5 + DOWN).scale(.75)
        ynpeqe[0].set_color(YELLOW)

        self.play(FadeIn(focusRect1))
        self.play(ReplacementTransform(focusRect1, focusRect2))
        self.play(ReplacementTransform(focusRect2, focusRect3))
        self.play(FadeOut(focusRect3))
        self.wait(1)

        self.play(TransformMatchingTex(npeqs[0], xnpeqe))
        self.play(TransformMatchingTex(npeqs[1], ynpeqe))
        self.wait(1)

        self.play(xeq[2].animate.set_color(GREEN),
                  yeq[2].animate.set_color(PURPLE),
                  xnpeqe[2].animate.set_color(GREEN), 
                  ynpeqe[2].animate.set_color(PURPLE),
                  xnpeqe[5].animate.set_color(PURPLE),
                  ynpeqe[5].animate.set_color(GREEN))
        self.wait(1)

        xfeq = MathTex(r"x'", r'=', r'x', r'\cos ( {{\alpha}} )', " - ", r"y", r"\sin ( {{\alpha}} )").shift(UP*.5 + DOWN)
        xfeq[0].set_color(ORANGE)
        xfeq[2].set_color(ORANGE)
        xfeq[7].set_color(YELLOW)
        yfeq = MathTex(r"y'", r'=', r'y', r'\cos ( {{\alpha}} )', " + ", r"x", r"\sin ( {{\alpha}} )").shift(DOWN*.5 + DOWN)
        yfeq[0].set_color(YELLOW)
        yfeq[2].set_color(YELLOW)
        yfeq[7].set_color(ORANGE)
        feqs = Group(xfeq, yfeq)

        self.play(TransformMatchingTex(Group(oeqs, xnpeqe, ynpeqe), feqs.move_to(ORIGIN)))
        self.wait(1)

        xprect = SurroundingRectangle(xfeq, color=RED, buff=.2)
        yprect = SurroundingRectangle(yfeq, color=RED, buff=.2)

        self.play(Create(xprect))
        self.wait(1)
        self.play(ReplacementTransform(xprect, yprect))
        self.wait(1)
        self.play(FadeOut(yprect))
        self.wait(1)

        rotcirc = Circle(3, WHITE).shift(RIGHT * 3)
        circAxes = Axes([-10, 10], [-10, 10], rotcirc.radius * 2, rotcirc.radius * 2, axis_config={"include_ticks": True, "unit_size": 1}, tips=False).move_to(rotcirc)

        self.play(feqs.animate.shift(LEFT * 4))
        self.play(Create(rotcirc), Create(circAxes))
        self.wait(1)

        pt = Dot(circAxes.coords_to_point(7, 2), color=WHITE)
        ptc = pt.copy()
        npt = Dot(circAxes.coords_to_point(7 * np.cos(PI / 3) - 2 * np.sin(PI / 3), 
                                              2 * np.cos(PI / 3) + 7 * np.sin(PI / 3)), 
                                              color=WHITE)
        path = ArcBetweenPoints(pt.get_center(), npt.get_center())

        ptLine = Line(start=circAxes.coords_to_point(0, 0), end=pt.get_center())
        ptLinec = ptLine.copy()
        ptLine.add_updater(lambda t: ptLine.become(Line(circAxes.coords_to_point(0, 0), pt.get_center())))

        self.play(Create(pt))
        self.add(ptc)
        self.play(Create(ptLine))
        self.add(ptLinec)
        self.play(MoveAlongPath(pt, path))

        ptAng = Angle(line1=ptLinec, line2=ptLine, radius=.5, quadrant=(1, 1))
        ptAngLabel = MathTex(r'\alpha').next_to(ptAng, UR, buff=.05)
        
        self.play(Create(ptAng))
        self.play(Write(ptAngLabel))
        self.play(ptAngLabel.animate.set_color(PURPLE),
                  xfeq.animate.set_color_by_tex(r'\alpha', PURPLE),
                  yfeq.animate.set_color_by_tex(r'\alpha', PURPLE))
        self.wait(1)

        circGroup = Group(rotcirc, circAxes, pt, ptc, npt, ptLine, ptLinec, ptAng, ptAngLabel)
        self.play(FadeOut(circGroup), feqs.animate.move_to(UP * 2))

        ptMat = MobjectMatrix([[MathTex(r"x'").set_color(ORANGE)], 
                              [MathTex(r"y'").set_color(YELLOW)]])
        eqTex = MathTex('=')
        rotMat = MobjectMatrix([[MathTex(r'\cos ( {{\alpha}} )').set_color_by_tex(r'\alpha', PURPLE), MathTex(r'- \sin ( {{\alpha}} )').set_color_by_tex(r'\alpha', PURPLE)],
                                [MathTex(r'\sin ( {{\alpha}} )').set_color_by_tex(r'\alpha', PURPLE), MathTex(r'\cos ( {{\alpha}} )').set_color_by_tex(r'\alpha', PURPLE)]], h_buff=2, element_alignment_corner=ORIGIN)
        optMat = MobjectMatrix([[MathTex(r'x').set_color(ORANGE)],
                                [MathTex(r'y').set_color(YELLOW)]])
        matrixeq = Group(ptMat, eqTex, rotMat, optMat)
        self.play(FadeIn(matrixeq.arrange_submobjects().shift(DOWN)))

        matSur = SurroundingRectangle(rotMat.get_rows()[0], color=RED, buff=MED_SMALL_BUFF)
        omatSur = SurroundingRectangle(optMat.get_columns()[0], color=RED, buff=MED_SMALL_BUFF)
        matSur2 = SurroundingRectangle(rotMat.get_rows()[1], color=RED, buff=MED_SMALL_BUFF)
        feqSur = SurroundingRectangle(xfeq, color=GREEN, buff=MED_SMALL_BUFF)
        feqSur2 = SurroundingRectangle(yfeq, color=GREEN, buff=MED_SMALL_BUFF)

        self.play(Create(matSur), Create(omatSur), Create(feqSur))
        self.wait(1)
        self.play(Transform(matSur, matSur2), Transform(feqSur, feqSur2))
        self.wait(1)

        self.play(FadeOut(feqs), FadeOut(matSur), FadeOut(omatSur), FadeOut(feqSur), matrixeq.animate.move_to(ORIGIN))
        self.wait(1)

        cosTex = MathTex(r'\cos ({{\alpha}})').set_color_by_tex(r'\alpha', PURPLE)
        frotMat = MobjectMatrix([[MathTex(r'1'),                                                       MathTex(r'- \tan ( {{\alpha}} )').set_color_by_tex(r'\alpha', PURPLE)],
                                 [MathTex(r'\tan ( {{\alpha}} )').set_color_by_tex(r'\alpha', PURPLE), MathTex(r'1')]], h_buff=2, element_alignment_corner=ORIGIN)

        nmatrixeq = matrixeq.copy()
        nmatrixeq.submobjects[2] = frotMat
        nmatrixeq.insert(2, cosTex)
        nmatrixeq.arrange_submobjects()
        self.play(ReplacementTransform(matrixeq, nmatrixeq))
        self.wait(1)
