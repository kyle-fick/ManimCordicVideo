from manim import *

class ComputerMultiply(MovingCameraScene):
    def construct(self):
        self.camera.background_color="#213d4c"
        
        byte = VGroup()
        squares = VGroup()
        for i in range(8):
            squares.add(Square(1.5))
        squares.arrange_submobjects(direction=LEFT, buff=0)

        for i in range(8):
            byte.add(
                Text('0').scale(2).move_to(squares[i])
            )

        self.play(FadeIn(byte, squares))
        self.wait(1)

        anims = [FadeIn(MathTex('2^{' + str(i) + '}').next_to(squares[i], DOWN)) for i in range(8)]
        self.play(LaggedStart(*anims))
        self.wait(1)

        def set_byte(n_byte):
            anims = [Transform(byte[i], n_byte[i]) for i in range(8)]
            return LaggedStart(*anims)

        def get_byte(bits):
            t_byte = VGroup()
            [t_byte.add(Text(str(bits[7 - i])).scale(2).move_to(squares[i])) for i in range(8)]
            return t_byte

        def bin_to_dec(bits):
            return sum([bits[7 - i] * 2 ** i for i in range(8)])
        
        b1 = [1, 0, 1, 0, 1, 0, 1, 0]
        self.play(set_byte(get_byte(b1)))
        self.wait(1)

        num_val = bin_to_dec(b1)
        num_label = DecimalNumber(num_val,  num_decimal_places=0).scale(2).shift(UP * 2.5)
        self.play(Write(num_label))
        self.wait(1)

        b2 = [0, 1, 0, 1, 0, 1, 0, 1]
        num_label2 = DecimalNumber(bin_to_dec(b2),  num_decimal_places=0).move_to(num_label).scale(2)
        self.play(set_byte(get_byte(b2)), ReplacementTransform(num_label, num_label2))
        self.wait(1)

        self.play(self.camera.frame.animate.move_to(num_label2.get_center()).scale(0.5))
        self.wait(1)

        num_label_temp = DecimalNumber(bin_to_dec(b2),  num_decimal_places=1).move_to(num_label2).scale(2)
        self.play(ReplacementTransform(num_label2, num_label_temp))
        self.wait(1)
        
        num_label_temp2 = DecimalNumber(bin_to_dec(b2) / 10,  num_decimal_places=2).move_to(num_label_temp).scale(2)
        self.play(ReplacementTransform(num_label_temp, num_label_temp2))
        self.wait(1)

        num_label_temp = DecimalNumber(bin_to_dec(b2),  num_decimal_places=1).move_to(num_label2).scale(2)
        self.play(ReplacementTransform(num_label_temp2, num_label_temp))
        self.wait(1)

        num_label2 = DecimalNumber(bin_to_dec(b2),  num_decimal_places=0).move_to(num_label).scale(2)
        self.play(ReplacementTransform(num_label_temp, num_label2))
        self.wait(1)

        self.play(self.camera.frame.animate.move_to(ORIGIN).scale(2))