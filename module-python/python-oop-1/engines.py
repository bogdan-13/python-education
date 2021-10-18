"""
This module contains the base class Engine and its subclasses
implemented according to the types of engines.
"""


class Engine:
    """This base class Engine

    Parameters
    ----------
    power : float
        This parameter is engine power implementation.

    Attributes
    ----------
    efficiency : float
        This parameter is engine efficiency implementation.
    start_time : float
        Engine start time.
    stop_time : float
        Engine stop time.
    """

    def __init__(self, power: float):
        self.power = power
        self.efficiency = None
        self.start_time = None
        self.stop_time = None

    def engine_start(self, time: float):
        """This method is engine start implementation.

        Parameters
        ----------
        time : float
            Engine start time.

        Returns
        -------
        None
        """
        self.start_time = time

    def engine_stop(self, time: float):
        """This method is engine stop implementation.

        Parameters
        ----------
        time : float
            Engine stop time.

        Returns
        -------
        None
        """
        self.stop_time = time

    @property
    def energy_consumption(self) -> float:
        """Energy consumption.

        Returns
        -------
        float
            Energy consumption.
        """
        return self.power * (self.stop_time - self.start_time) * (1 / self.efficiency)

    def __eq__(self, other):
        if isinstance(other, Engine):
            return self.power * self.efficiency == other.power * other.efficiency
        return False

    def __gt__(self, other):
        if isinstance(other, Engine):
            return self.power * self.efficiency > other.power * other.efficiency
        raise TypeError

    def __lt__(self, other):
        if isinstance(other, Engine):
            return self.power * self.efficiency < other.power * other.efficiency
        raise TypeError

    def __ge__(self, other):
        if isinstance(other, Engine):
            return self.power * self.efficiency >= other.power * other.efficiency
        raise TypeError

    def __le__(self, other):
        if isinstance(other, Engine):
            return self.power * self.efficiency <= other.power * other.efficiency
        raise TypeError

    def __bool__(self):
        return self.power > 0


class ElectricEngine(Engine):
    """Electric Engine implementation.

    Parameters
    ----------
    power : float
        This parameter is engine power implementation.

    Attributes
    ----------
    efficiency : float
        This parameter is engine efficiency implementation.

    """

    def __init__(self, power: float):
        super().__init__(power)
        self.efficiency = 0.9


class InternalCombustionEngine(Engine):
    """Internal Combustion Engine implementation.

    Parameters
    ----------
    power : float
        This parameter is engine power implementation.
    fuel : type
        This parameter is engine fuel implementation.

    Attributes
    ----------
    efficiency : float
         This parameter is engine efficiency implementation.
    """

    def __init__(self, power: float, fuel=''):
        super().__init__(power)
        self.fuel = fuel
        if isinstance(fuel, str):
            if fuel == 'diesel':
                self.efficiency = 0.4
            elif fuel == 'gasoline':
                self.efficiency = 0.25
            else:
                raise ValueError
        else:
            raise TypeError


class Turbine(Engine):
    """Turbine Engine implementation.

    Parameters
    ----------
    power : float
        This parameter is engine power implementation.

    Attributes
    ----------
    efficiency : float
         This parameter is engine efficiency implementation.
    """

    def __init__(self, power: float):
        super().__init__(power)
        self.efficiency = 0.3

    def __mul__(self, other: int) -> float:
        if isinstance(other, int):
            return self.power * other
        raise TypeError


class SteamEngine(Engine):
    """Steam Engine implementation.

    Parameters
    ----------
    power : float
        This parameter is engine power implementation.

    Attributes
    ----------
    efficiency : float
         This parameter is engine efficiency implementation.
    """

    def __init__(self, power: float):
        super().__init__(power)
        self.efficiency = 0.15
