from pygris.utils import erase_water

king_tiger = tracts("WA", "King", cb = False, cache = True)

king_erased = erase_water(king_tiger)

king_erased.explore()
