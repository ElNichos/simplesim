from electric_branch import ElectricBranch, ISineSource


class VoltageSource(ElectricBranch, ISineSource):
    """
    Class that implements ideal linear AC(sine) or DC voltage source.
    """
    def __init__(self, magnitude: float, frequency: float,
                 phase: float, inner_resistance: float = 0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        super().__init__(magnitude, frequency, phase)
        self.inner_resistance = inner_resistance

    def __str__(self):
        return f"Voltage source branch {self.name}|" + self.string_repr

    def __repr__(self) -> str:
        return self.get_branch_info() + self.string_repr


class CurrentSource(ElectricBranch, ISineSource):
    """
    Class that implements ideal linear AC(sine) or DC current source.
    """
    def __init__(self, magnitude: float, frequency: float,
                 phase: float, inner_conductance: float = 0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        super().__init__(magnitude, frequency, phase)
        self.inner_conductance = inner_conductance

    def __str__(self):
        return f"Current source branch {self.name}|" + self.string_repr

    def __repr__(self) -> str:
        return self.get_branch_info() + self.string_repr
