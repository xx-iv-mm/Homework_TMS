# Exercise_1
class Product:
    def init(self, nazv, magNazv, stoim):
        self.name_field = nazv
        self.name_shop_field = magNazv
        self.condition_field= stoim

    @property
    def name(self):
        return self.name_field

    @property
    def name_shop(self):
        return self.name_shop_field

    @property
    def money(self):
        return self.condition_field

    @property
    def condition(self):
        return f"Name : {self.name}, Name shop: {self.name_shop}, Money: {self.money}"