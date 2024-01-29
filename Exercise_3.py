# Exercise 3

class Bus:
    def __init__(self, speed, max_seats, max_speed, passengers, flag):
        self.speed = speed
        self.max_seats = max_seats
        self.max_speed = max_speed
        self.passengers = passengers
        self.flag = flag
        self.seats = {}

    def go_in(self, passenger):
        if self.flag:
            self.seats[passenger] = passenger
        else:
            raise ValueError('Свободных мест нет.')

    def go_out(self, passenger):
        if passenger in self.seats:
            del self.seats[passenger]

        elif passenger in self.passengers:
            del self.passengers[self.passengers.index(passenger)]

        else:
            raise ValueError('Такого пассажира нет в автобусе')

    def change_speed(self, new_speed):
        if int(new_speed) <= self.max_speed:
            self.speed = new_speed
        else:
            raise ValueError('Автобус не может ехать так быстро')

    def __contains__(self, passenger):
        return passenger in self.passengers or passenger in self.seats.values()

    def __iadd__(self, passenger):
        self.seats[passenger] = passenger
        return self

    def __isub__(self, passenger):
        del self.seats[passenger]
        return self
