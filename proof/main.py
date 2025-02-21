from manim import *


class DefaultTemplate(Scene):
    def construct(self):

        text = Tex(
            r"Let's prove the Power Rule: $\frac{\mathrm{d}}{\mathrm{d}x}[x^n] = nx^{n-1}$",
            font_size=12,
        )

        self.play(Write(text))

        self.play(text.animate.move_to(UP).scale(0.7))

        framebox = SurroundingRectangle(text, buff=0.05, stroke_width=1)

        self.play(Create(framebox))

        proofTitle = (
            Tex(r"\underline{Proof:}", font_size=12)
            .next_to(text, 0.5 * LEFT + 0.3 * DOWN)
            .scale(0.7)
        )

        self.play(Write(proofTitle))

        intro = Tex(
            r"We will use the principle of ", "mathematical induction", font_size=12
        ).scale(0.7)
        intro[1].set_color(BLUE)

        self.play(Write(intro))
        self.wait(1)

        propertyStatement = Tex(
            r"Let the property $P(n)$ be ",
            r"$\displaystyle\frac{\mathrm{d}\left(x^n\right)}{\mathrm{d}x} = nx^{n-1}$",
            font_size=12,
        ).scale(0.7)

        propertyStatement[1].set_color(GREEN)

        self.play(Transform(intro, propertyStatement), run_time=2)
        self.play(
            intro.animate.align_to(proofTitle, LEFT),
        )
        self.play(intro.animate.shift(UP * 0.7))
        self.wait(5)
        self.play(Unwrite(intro))

        proofSectionOne = Tex(
            r"""\textbf{\underline{Show that $P(1)$ is true:}} To show $P(1)$ we must show that""",
            r"""\[
                    \frac{\mathrm{d}\left(x^{1}\right)}{\mathrm{d}x} = 1\cdot\,x^{1-1}
                \]""",
            "But, ",
            r"""$
                    1\cdot\,x^{1-1} = 1\cdot\,x^{0} = 1 \cdot\, 1 = 1
                $""",
            " and ",
            r"""$\frac{\mathrm{d}(x^1)}{\mathrm{d}x} = \frac{\mathrm{d}(x)}{\mathrm{d}x} = 1$""",
            """. Therefore, the left hand side and the right are equivalent and $P(1)$ is true. """,
            font_size=12,
        ).scale(0.7)

        proofSectionOne[1].set_color(GREEN)
        proofSectionOne[3].set_color(GREEN)
        proofSectionOne[5].set_color(GREEN)

        self.play(Write(proofSectionOne), run_time=3)

        self.wait(7)

        proofSectionTwo = Tex(
            r"""\textbf{\underline{Show that for all integers $k \geq 1$ if $P(k)$ is true then $P(k+1)$ is also true:}} """,
            r"""Let $k$ be any integer with $k \geq 1$, and suppose that """,
            r"""\[
                \frac{\mathrm{d}\left(x^{k}\right)}{\mathrm{d}x} = kx^{k-1}
            \]""",
            r"""We must show that""",
            r"""\[
                \frac{\mathrm{d}\left(x^{k+1}\right)}{\mathrm{d}x} = \left(k+1\right)x^{k}
            \]""",
            font_size=12,
        ).scale(0.7)

        proofSectionTwo[2].set_color(GREEN)
        proofSectionTwo[4].set_color(GREEN)

        self.play(Transform(proofSectionOne, proofSectionTwo), run_time=2)

        self.wait(6)

        proofSectionThree = VGroup(
            Tex(r"But, ", font_size=12).scale(0.7),
            MathTex(
                r"""
                    \frac{\mathrm{d}\left(x^{k+1}\right)}{\mathrm{d}x} &= \frac{\mathrm{d}}{\mathrm{d}x}\left[x^{k+1}\right] \tag{by notational equivalence}
                """,
                font_size=12,
            ).scale(0.7),
            MathTex(
                r"""
                =\frac{\mathrm{d}}{\mathrm{d}x}\left[x^{k} \cdot\, x\right] \tag{by exponent properties}\\
                """,
                font_size=12,
            ).scale(0.7),
            MathTex(
                r"""
                =\left(\frac{\mathrm{d}}{\mathrm{d}x}\left[x^{k}\right]\right)x + x^{k}\left(\frac{\mathrm{d}}{\mathrm{d}x}\left[x\right]\right) \tag{by the Product Rule} \\
                """,
                font_size=12,
            ).scale(0.7),
        )

        proofSectionFour = VGroup(
            MathTex(
                r"""
                =\left(kx^{k-1}\right)x + x^{k}\left(\frac{\mathrm{d}}{\mathrm{d}x}\left[x\right]\right) \tag{by inductive hypothesis} \\
                """,
                font_size=12,
            ).scale(0.7),
            MathTex(
                r"""
                =\left(kx^{k-1}\right)x + x^{k}\left(1\right) \tag{by the derivative of a linear term} \\
                """,
                font_size=12,
            ).scale(0.7),
            MathTex(
                r"""
                =kx^{k} + x^{k} \tag{by algebra and exponent properties} \\
                """,
                font_size=12,
            ).scale(0.7),
            MathTex(
                r"""
                =(k+1)x^{k} \tag{by factoring out $x^{k}$}
                """,
                font_size=12,
            ).scale(0.7),
        )

        for i in range(1, len(proofSectionThree)):
            proofSectionThree[i].set_color(GREEN)

        for i in range(0, len(proofSectionFour)):
            proofSectionFour[i].set_color(GREEN)

        proofSectionThree.arrange(DOWN, aligned_edge=LEFT)
        proofSectionFour.arrange(DOWN, aligned_edge=LEFT)

        self.play(Transform(proofSectionOne, proofSectionThree), run_time=2)
        self.wait(7)

        self.play(Transform(proofSectionOne, proofSectionFour), run_time=2)
        self.wait(7)

        proofSectionFive = Tex(
            r""" So,""",
            r"""$\displaystyle\,\frac{\mathrm{d}\left(x^{k+1}\right)}{\mathrm{d}x} = \left(k+1\right)x^{k}$""",
            r""" \textit{[as was to be shown].}
            """,
            font_size=12,
        ).scale(0.7)

        proofSectionFive[1].set_color(GREEN)
        qed = Square(0.02, color=WHITE).to_edge(RIGHT)

        self.play(Transform(proofSectionOne, proofSectionFive), run_time=2)
        self.play(Create(qed))

        self.wait(7)
