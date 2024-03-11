from api import TreeNode, API
from geocoders.geocoder import Geocoder


# Инверсия дерева
class MemorizedTreeGeocoder(Geocoder):
    def __init__(self, samples: int | None = None, data: list[TreeNode] | None = None):
        super().__init__(samples=samples)
        if data is None:
            self.__data = API.get_areas()
        else:
            self.__data = data
        self.__addresses = {}
        self.create_dict(self.__data)

    def create_dict(self, tree: list[TreeNode], parent: str = '') -> dict:
        for area in tree:
            if parent:
                full_address = f'{parent}, {area.name}'
            else:
                full_address = area.name
            self.__addresses[area.id] = full_address
            self.create_dict(area.areas, full_address)

    def _apply_geocoding(self, area_id: str) -> str:
        return self.__addresses.get(str(area_id))

    
