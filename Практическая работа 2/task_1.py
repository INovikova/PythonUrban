class GreenZoneIndex:
    def __init__(self, territory_name: str, territory_area: float, green_zones: list):
        """
        :param territory_name: Название территории
        :param territory_area: Площадь территории
        :param green_zones: Список площадей парков
        """
        self.territory_name = territory_name
        self.territory_area = territory_area
        self.green_zones = green_zones
        # TODO все аргументы конструктора записать в атрибуты экземпляра класса

        self.green_index = self.calculate_green_index()  # индекс озеленения

        # TODO посчитать индекс озеленения с помощью метода calculate_green_index
    def calculate_green_index(self):
        """
        Метод для вычисления индекса озеленения.

        Индекс рассчитывается как отношение площади всех парков к площади территории
        """
        green_index = 0
        for green_zone in self.green_zones:
            green_zone_index = round((green_zone / self.territory_area) * 100, 2)
            green_index = green_index + green_zone_index

        return green_index

        # TODO посчитать индекс озеленения с атрибутов экземпляра класса


# TODO Создать экземпряр класса и с помощью его атрибутов распечатать индекс озеленения в процентах до 2 знака после запятой.
pushkin = GreenZoneIndex("Пушкин", 28675, [302, 487, 420, 325, 471, 363, 404])

print("Индекс озеленения территории", pushkin.territory_name, "равен", pushkin.green_index, "%")
# Ожидаемый ответ Индекс озеленения территории Пушкин равен 9.67%

