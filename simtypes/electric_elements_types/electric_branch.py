from abc import ABC, abstractmethod
from math import pi

from simtypes.coretypes import Edge


def get_cyclic_frequency(frequency):
    return 2 * pi * frequency


class ElementModeData:
    """
    Implements the parameters of the basic electric element(branch):
     - voltage of an electric element;
     - current that flows through the electric element;
     - active and reactive power of an electric element.
    """
    def __init__(self):
        self.voltage = None
        self.current = None
        self.active_power = None
        self.reactive_power = None
        self.time = None

    def calculate_power(self):
        # TODO power = self.voltage * self.reactive_power
        # TODO self.active_power = Real(power)
        # TODO self.reactive_power = Imaginary(power)
        pass


class ElectricBranch(Edge, ABC):
    """
    Implements an abstract branch of an electric circuit.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mode_data = ElementModeData()

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass


class ISineSource(ABC):
    """
    An abstract interface for sine power sources types.
    """
    def __init__(self, magnitude: float, frequency: float, phase: float):
        self.magnitude = magnitude
        self.frequency = frequency
        self.phase = phase
        self.cyclic_frequency = get_cyclic_frequency(frequency)
        self.string_repr = f"{self.magnitude}<{self.phase}|{self.frequency}"


class IReactive(ABC):
    """
    An abstract interface that can be used to override a
    reactance property of a passive electric element.
    """
    def __init__(self, frequency: float):
        self._reactance = self.reactance(frequency)
        self.frequency = frequency
        self.cyclic_frequency = None

    @property
    def reactance(self):
        """
        'Getter' for an impedance attribute.
        :return: impedance complex value
        """
        return self._reactance

    @reactance.setter
    def reactance(self, frequency):
        """
        Overridable 'setter' for an impedance attribute of
        passive element.
        """
        pass


# TODO Complete this interface for further usage
class ITransientPassive(ABC):
    """
    An abstract interface that can be used to override
    a transient parameters for a passive electric element.
    """
    def __init__(self):
        self.transient_mode = ElementModeData()
        self._transient_impedance = None
        self._transient_emf = None

    @property
    def transient_impedance(self):
        pass

    @property
    def transient_emf(self):
        pass
