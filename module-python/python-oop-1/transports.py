"""
This module contains the base class Transport and its subclasses
implemented according to the types of transport.
"""

from abc import ABC, abstractmethod
from engines import InternalCombustionEngine, ElectricEngine, Turbine, SteamEngine


class Transport(ABC):
    """Short summary.

    Parameters
    ----------
    name : str
        Name instance.
    speed : float
        Speed instance.

    Attributes
    ----------
    start_time : float
        Start time.
    stop_time : type
        Stop time.
    usage : int
        Count usage class Transport.
    """
    usage = 0

    def __init__(self, name: str, speed: float):
        self.name = name
        self.speed = speed
        self.start_time = None
        self.stop_time = None
        Transport.usage += 1

    @staticmethod
    def happy_roads():
        """Some text method.

        Returns
        -------
        None.
        """
        print('Happy roads!')

    @staticmethod
    def welcome():
        """Some text method.

        Returns
        -------
        None.
        """
        print('Welcome to Home!')

    @classmethod
    def usages(cls):
        """Count usage class Transport.

        Returns
        -------
        None
        """
        print(f'Usage class {cls.__name__}: {cls.usage} times')

    @property
    def road_time(self) -> float:
        """Travel time.

        Returns
        -------
        float
            Travel time.

        """
        return self.stop_time - self.start_time

    @property
    def distance(self) -> float:
        """The length of the path.

        Returns
        -------
        float
           The length of the path.

        """
        return self.speed * self.road_time

    @abstractmethod
    def start(self, time: float):
        """Abstract method transport starts.

        Parameters
        ----------
        time : float
            Start time.

        Returns
        -------
        None
        """
        ...

    @abstractmethod
    def stop(self, time: float):
        """Abstract method transport stops.

        Parameters
        ----------
        time : float
            Stop time.

        Returns
        -------
        None
        """
        ...

    def __repr__(self):
        return self.name

    def __call__(self, *args, **kwargs):
        print(f'Я зараз подорожую з швидкістю {self.speed} km/h')


class Truck(Transport, InternalCombustionEngine):
    """Implementation of truck of the basic class Transport."""

    def __init__(self, name: str, speed: float, power: float, fuel='diesel'):
        Transport.__init__(self, name, speed)
        InternalCombustionEngine.__init__(self, power, fuel)

    def start(self, time: float):
        self.engine_start(time)

    def stop(self, time: float):
        self.engine_stop(time)


class Car(Transport, InternalCombustionEngine):
    """Implementation of car of the basic class Transport."""
    def __init__(self, name: str, speed: float, power: float, fuel='gasoline'):
        Transport.__init__(self, name, speed)
        InternalCombustionEngine.__init__(self, power, fuel)

    def start(self, time: float):
        self.engine_start(time)

    def stop(self, time: float):
        self.engine_stop(time)


class SteamTrain(Transport, SteamEngine):
    """Implementation of steam train of the basic class Transport."""
    def __init__(self, name: str, speed: float, power: float):
        Transport.__init__(self, name, speed)
        SteamEngine.__init__(self, power)

    def start(self, time: float):
        self.engine_start(time)

    def stop(self, time: float):
        self.engine_stop(time)


class Locomotive(Transport, ElectricEngine):
    """Implementation of electric train of the basic class Transport."""
    def __init__(self, name: str, speed: float, power: float):
        Transport.__init__(self, name, speed)
        ElectricEngine.__init__(self, power)

    def start(self, time: float):
        self.engine_start(time)

    def stop(self, time: float):
        self.engine_stop(time)


class Airplane(Transport, Turbine):
    """Implementation of fly transport of the basic class Transport.

    Parameters
    ----------
    name : str
        Name instance.
    speed : float
        Speed of transport.
    power : float
        Power of engine.
    turbines : int
        Quantity turbines.
    """
    def __init__(self, name: str, speed: float, power: float, turbines: int):
        Transport.__init__(self, name, speed)
        Turbine.__init__(self, power)
        self.power = Turbine(power) * turbines

    def start(self, time: float):
        self.start_time = time

    def stop(self, time: float):
        self.stop_time = time
