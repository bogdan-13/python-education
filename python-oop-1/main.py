"""
This module is intended for testing the classes of the Transport and Engines modules
"""
from transports import Truck, Car, SteamTrain, Locomotive, Airplane, Transport


def main():
    """
    This function is intended for testing the classes of the Transport and Engines modules
    :return: None
    """
    Transport.happy_roads()

    total_road = 0
    total_energy = 0

    car = Car('авто', 90, 50000, fuel='gasoline')
    car.start(0)
    car.stop(2)
    total_road += car.distance
    total_energy += car.energy_consumption
    print(f'Спочатку ми проїхали {car.distance} км за {car.road_time} години на авто')

    steam_train = SteamTrain('паротяг', 60, 900000)
    steam_train.start(2)
    steam_train.stop(4)
    total_road += steam_train.distance
    total_energy += steam_train.energy_consumption
    print(f'Потім пересіли на паротяг та за {steam_train.road_time} '
          f'годин проїхали ще {steam_train.distance} км')

    truck = Truck('вантажівка', 80, 0, fuel='diesel')
    truck.start(4)
    truck.stop(7)
    if truck:
        total_road += truck.distance
        total_energy += truck.energy_consumption
        print(f'Через деякий час сіли на вантажівку і проїхали {truck.distance} км')
    else:
        print(f'Через деякий час сіли на вантажівку, але вона мала зламаний двигун '
              f'і нам довелося {truck.road_time} години шукати новий транспорт')

    train = Locomotive('потяг', 120, 800000)
    train.start(7)
    train.stop(13)
    total_road += train.distance
    total_energy += train.energy_consumption
    print(f'Нам пощастило заскочити в потяг і ми на швидкості {train.speed}'
          f' км/год проїхали ще {train.distance} км')

    turbines = int(input('Ми добрались до аеродрому і побачили напіврозібраний літак,'
                         ' скільки турбін нам приліпити? '))
    concord = Airplane('літак', 1200, 4000000, turbines)
    concord.start(14)
    concord.stop(24)
    concord()
    total_road += concord.distance
    total_energy += concord.energy_consumption
    print(f'На швидкому літаку ми подолали ще {concord.distance} км за {concord.road_time} годин')

    print(f'Всього наш вояж склав {total_road} кілометрів.\n'
          f'Нами було витрачено {int(total_energy)} Дж енергії, '
          f'якої вистачило б закипʼятити {int(total_energy / 336000)} л води.\n'
          f'Всього ми спробували використати {Transport.usage} транспортних засобів.\n'
          f'Найбільше енергії витратив {max([car, steam_train, truck, train, concord])}.')

    Transport.welcome()

    Transport.usages()


if __name__ == '__main__':
    main()
