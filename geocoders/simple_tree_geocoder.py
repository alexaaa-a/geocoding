from api import API, TreeNode
from geocoders.geocoder import Geocoder


# Перебор дерева
class SimpleTreeGeocoder(Geocoder):
    def __init__(self, samples: int | None = None, data: list[TreeNode] | None = None):
        super().__init__(samples=samples)
        if data is None:
            self.__data = API.get_areas()
        else:
            self.__data = data

    def _apply_geocoding(self, area_id: str) -> str:
        def find(node: TreeNode, target_id: str):
            target_id = str(target_id)
            if node.id == target_id:
                return node

            else:
                for child in node.areas:
                    res = find(child, target_id)
                    if res is not None:
                        return res
            return None


        data = self.__data
        res = []
        for node in data:
            result = find(node, area_id)
            if result is not None:
                res.append(result.name)
                a = result.parent_id
                while a is not None:
                    b = API.get_area(a)
                    res.append(b.name)
                    a = b.parent_id
        address = ", ".join([node for node in reversed(res)])

        return address
