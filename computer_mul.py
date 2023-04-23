from manim import *

class ComputerMultiply(Scene):
    def construct(self):
        self.camera.background_color="#213d4c"
        
        byte = VGroup()
        squares = VGroup()
        for i in range(8):
            byte.add(
                Tex('0').scale(2)
            )
        byte.arrange_submobjects(buff=.75, direction=LEFT)
        for i in range(8):
            squares.add(Square().surround(byte[i], buff=.75))

        self.play(FadeIn(byte, squares))
        self.wait(1)

        anims = [FadeIn(MathTex('2^{', i, '}').next_to(byte[i], DOWN * 1.75)) for i in range(8)]
        self.play(LaggedStart(*anims))
        self.wait(1)