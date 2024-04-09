class Vehicle:
    def __init__(self, max_speed, efficiency):
        self.max_speed = max_speed
        self.efficiency = efficiency
        

    def get_trip_cost(self, distance, fuel_price):
        '''
        calculates the cost of gas for the trip:
        (distance / efficiency) * fuel_price
        '''
        return (distance / self.efficiency) * fuel_price

    def get_cargo_volume(self):
        '''should be left empty child classes will override this method'''
        pass


class Truck(Vehicle):
    def __init__(
        self,
        max_speed,
        efficiency,
        load_weight,
        bed_area,
    ):
        super().__init__(max_speed, efficiency)
        self.__load_weight = load_weight
        self.__bed_area = bed_area

    def get_trip_cost(self, distance, fuel_price):
        '''super().get_trip_cost() + (load weight * 0.01)'''
        base = super().get_trip_cost(distance, fuel_price) 
        return base + (self.__load_weight * 0.01)

    def get_cargo_volume(self):
        '''truck bed volume = bed area * 2'''
        return self.__bed_area * 2


class Car(Vehicle):
    def __init__(self, max_speed, efficiency, cargo_volume):
        super().__init__(max_speed, efficiency)
        self.__cargo_volume = cargo_volume


    def get_cargo_volume(self):
        return self.__cargo_volume
