# размещаем часть кода из предыдущей задачи (поиск индекса озеленения)
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

list_territories = [
    {
        "territory_name": "Пушкин",
        "territory_area": 28676,
        "green_zones": [302, 487, 420, 325, 471, 363, 404]
    },
    {
        "territory_name": "Павловск",
        "territory_area": 21025,
        "green_zones": [360, 375, 223, 258, 345, 296, 303]
    },
    {
        "territory_name": "Петергоф",
        "territory_area": 44274,
        "green_zones": [364, 447, 438, 223, 336, 431, 442]
    },
]

# сделать список с объектами типа GreenZoneIndex
list_green_index = []
for territory in list_territories:
    new_list = GreenZoneIndex(territory_name = territory["territory_name"], territory_area = territory["territory_area"], green_zones = territory["green_zones"])
    value = new_list.green_index
    list_green_index.append(value)

print(list_green_index)

