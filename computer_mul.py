from manim import *

class ComputerMultiply(Scene):
    def construct(self):
        self.camera.background_color="#213d4c"
        
        byte = VGroup()
        squares = VGroup()
        for i in range(8):
            byte.add(
                Text('0').scale_to_fit_width(0.42)
            )
        byte.arrange_submobjects(buff=.75, direction=LEFT)
        for i in range(8):
            squares.add(Square().surround(byte[i], buff=.75))

        self.play(FadeIn(byte, squares))
        self.wait(1)

        anims = [FadeIn(MathTex('2^{', i, '}').next_to(byte[i], DOWN * 2)) for i in range(8)]
        self.play(LaggedStart(*anims))
        self.wait(1)

        print(byte[0].width)

        def set_byte(n_byte):
            anims = [Transform(byte[i], n_byte[i]) for i in range(8)]
            return LaggedStart(*anims)

        def get_byte(bits):
            t_byte = VGroup()
            [t_byte.add(Text(str(bits[7 - i])).scale_to_fit_width(0.42)) for i in range(8)]
            t_byte.arrange_submobjects(buff=.75, direction=LEFT)
            return t_byte
        
        self.play(set_byte(get_byte([1, 0, 1, 0, 1, 0, 1, 0])))
        self.wait(1)
