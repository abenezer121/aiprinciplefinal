from data import Data
from ucs import UniformCostSearch


ethiopia_cities = Data.returnmap()
ucs = UniformCostSearch()


path , cost = ucs.ucs("Addis Ababa", "Lalibella", ethiopia_cities )
print("from addis ababa to lalibela path   using uniform cost search is " ,path)
print("from addis ababa to lalibela cost using uniform cost search is ",cost)
print()
print()
print()

path , cost = ucs.ucscustom("Addis Ababa" , ["Axum", "Gondar", "Lalibella", "Babile", "Jimma", "Bale", "Sof Oumer", "Arba Minchi"], ethiopia_cities)
print("the path using the customzed is " ,path)
print("the cost is ",cost)
