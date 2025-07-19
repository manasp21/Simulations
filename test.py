from manim import *

class QuantumBeats(Scene):
    def construct(self):
        # Title
        title = Text("Isotropic Quantum Beats", font_size=48).to_edge(UP)
        self.play(Write(title))

        # Energy levels: ground |g>, excited |e1>, |e2>
        level_g = Line([-4, -3, 0], [4, -3, 0], color=BLUE)
        level_e1 = Line([-2, 1, 0], [2, 1, 0], color=RED)
        level_e2 = Line([-2, 1.5, 0], [2, 1.5, 0], color=RED)
        label_g = Text("|g⟩", font_size=24).next_to(level_g, LEFT)
        label_e1 = Text("|e₁⟩", font_size=24).next_to(level_e1, LEFT)
        label_e2 = Text("|e₂⟩", font_size=24).next_to(level_e2, LEFT)
        delta_e = MathTex(r"\Delta E = \hbar \omega").next_to(level_e1, RIGHT, buff=0.5).shift(UP*0.25)
        
        levels = VGroup(level_g, level_e1, level_e2, label_g, label_e1, label_e2, delta_e)
        self.play(FadeIn(levels))

        # Pump pulse: arrow from ground to excited superposition
        pump_arrow = Arrow([0, -3, 0], [0, 1.25, 0], color=YELLOW)
        pump_label = Text("Pump Pulse (broadband)", font_size=24, color=YELLOW).next_to(pump_arrow, RIGHT)
        self.play(GrowArrow(pump_arrow), Write(pump_label))
        superpos = MathTex(r"|\psi(0)\rangle = \alpha |e_1\rangle + \beta |e_2\rangle").next_to(levels, DOWN, buff=1)
        self.play(Write(superpos))

        # Time evolution
        time_label = Text("Time evolution:", font_size=24).next_to(superpos, DOWN, buff=0.5)
        self.play(Write(time_label))
        evol = MathTex(r"|\psi(t)\rangle = \alpha |e_1\rangle e^{-i E_1 t / \hbar - \gamma t / 2} + \beta |e_2\rangle e^{-i E_2 t / \hbar - \gamma t / 2}")
        evol.scale(0.7).next_to(time_label, DOWN)
        self.play(Write(evol))

        # Intensity plot
        self.wait(1)
        axes = Axes(x_range=[0, 10, 1], y_range=[0, 1.5, 0.5], axis_config={"color": GREEN}).shift(DOWN*2 + RIGHT*3)
        intensity_func = lambda t: np.exp(-0.5 * t) * (1 + np.cos(2 * t))  # Simplified I(t) ~ exp(-γt) (1 + cos(ωt))
        graph = axes.plot(intensity_func, color=PURPLE)
        graph_label = Text("Fluorescence Intensity I(t)", font_size=24, color=PURPLE).next_to(axes, UP)
        iso_note = Text("(Isotropic: observable in total signal)", font_size=20).next_to(graph_label, DOWN)
        
        self.play(Create(axes), Create(graph), Write(graph_label), Write(iso_note))

        # Probe pulse for pump-probe aspect
        probe_arrow = Arrow([1, -3, 0], [1, 1.25, 0], color=GREEN).shift(LEFT*4)
        probe_label = Text("Probe Pulse", font_size=24, color=GREEN).next_to(probe_arrow, LEFT)
        self.play(GrowArrow(probe_arrow), Write(probe_label))
        beat_note = Text("Oscillations due to interference, independent of direction", font_size=20).to_edge(DOWN)
        self.play(Write(beat_note))

        # Animate oscillation
        dot = Dot(color=WHITE).move_to(axes.c2p(0, intensity_func(0)))
        self.add(dot)
        def update_dot(mob, dt):
            t = self.time % 10  # Loop over 10 units
            mob.move_to(axes.c2p(t, intensity_func(t)))
        dot.add_updater(update_dot)
        self.wait(10)  # Run animation for 10 seconds

        self.play(FadeOut(VGroup(title, levels, pump_arrow, pump_label, superpos, time_label, evol, axes, graph, graph_label, iso_note, probe_arrow, probe_label, beat_note, dot)))