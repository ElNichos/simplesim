from math import inf

from .electric_branch import ElectricBranch, IReactive, get_cyclic_frequency


class Resistor(ElectricBranch):
    """
    Class that implements basic linear resistor. It keeps the state
    of a resistor element.
    """

    def __init__(self, resistance: float, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resistance = resistance

    def __str__(self):
        return f"Resistor branch {self.name}|R = {self.resistance} ohms"

    def __repr__(self) -> str:
        return self.get_branch_info() + f"|R = {self.resistance} ohms"


class Inductor(ElectricBranch, IReactive):
    """
    Class that implements basic linear inductor. It keeps the state
    of an inductor element.
    """

    def __init__(self, inductance: float, frequency: float, *args, **kwargs):
        super().__init__(*args, **kwargs)
        super().__init__(frequency)
        self.inductance = inductance
        self._reactance = self.reactance(frequency)

    @property
    def reactance(self):
        return self._reactance

    @reactance.setter
    def reactance(self, frequency):
        self._reactance = 0 + (1j * self.inductance * get_cyclic_frequency(frequency))

    def __str__(self):
        return (f"Inductor branch {self.name}|L = {self.inductance} H|"
                f"X = {self._reactance} ohms")

    def __repr__(self) -> str:
        return self.get_branch_info() + (f"|L = {self.inductance} H|"
                                         f"X = {self._reactance} ohms")


class Capacitor(ElectricBranch, IReactive):
    """
    Class that implements basic linear capacitor. It keeps the state
    of a capacitor element.
    """

    def __init__(self, capacity: float, frequency: float, *args, **kwargs):
        super().__init__(*args, **kwargs)
        super().__init__(frequency)
        self.capacity = capacity
        self._reactance = self.reactance(frequency)

    @property
    def reactance(self):
        return self._reactance

    @reactance.setter
    def reactance(self, frequency):
        self._reactance = 0 - 1j / (self.capacity * get_cyclic_frequency(frequency))

    def __str__(self):
        return (f"Capacitor branch {self.name}|C = {self.inductance} F|"
                f"X = {self._reactance} ohms")

    def __repr__(self) -> str:
        return self.get_branch_info() + (f"|C = {self.capacity} F|"
                                         f"X = {self._reactance} ohms")


class Switch(ElectricBranch):
    """
    Class that implements switch with commutation time offset and current state.\n
    State attribute values:
        - True - switch is closed and current flows through the switch;
        - False - switch is opened and current does not flow through the switch.
    """
    closed_resistance = 0
    opened_resistance = inf

    def __init__(self, init_state: bool, commutation_time: float = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.current_state = init_state
        self.commutation_time = commutation_time  # TODO Release time switching method for transients
        self._set_resistance()

    def switch_state(self):
        """
        Method for changing state of the switch
        """
        self.current_state = False if self.current_state is True else True
        self._set_resistance()

    def _set_resistance(self):
        if self.current_state is True:
            self.current_resistance = Switch.closed_resistance
        else:
            self.current_resistance = Switch.opened_resistance

    def __str__(self):
        return (f"Switch branch {self.name}|R = {self.current_resistance} ohms"
                f"|commutation time = {self.commutation_time}")

    def __repr__(self) -> str:
        return super().get_branch_info() + f"|R = {self.current_resistance} ohms"
