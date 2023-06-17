city_coffee_region={
    "Dire Dawa":{"Chiro","Harar"},
    "Wolkite":{"Benchi Naji","Tepi"},
    "Nekemte":{"Gimbi", "Limu"},
    "Addis Ababa": {"Ambo","Buta Jirra", "Adama"},
    "Ambo":{"Gedo", "Nekemte"},
    "Worabe":{"Hosana","Durame"},
    "Mojo":{"Dilla","Kaffa"},
    "Buta Jirra":{"Worabe", "Wolkite"},
    "Adama":{"Dire Dawa", "Mojo"},
    "Gedo":{"Shambu","Fincha"},
}

terminal_cities = ["Shambu","Fincha","Gimbi","Limu","Hosana","Durame","Benchi Naji","Tepi","Kaffa","Dilla","Chiro","Harar"]
adjacent_cities = { "Fincha" : "Gedo", "Hosana" : "Worabe", "Harar": "Dire Dawa","Limu" : "Nekemte", "Tepi" : "Wolkite", "Dilla" : "Mojo", } 
parent_cities={ "Gedo" : "Ambo", "Worabe": "Buta Jirra", "Mojo" : "Adama" }

scores = [4,5,8,8,6,5,5,6,7,9,6,10] 
is_max = True 
scores_1 = [] 
selected_cities =[]

for i in range(0,len(scores),2): 
    if is_max: 
        if scores[i] > scores[i+1]:
             selected_cities.append(terminal_cities[i])
        else: 
            selected_cities.append(terminal_cities[i+1])
    scores_1.append(max(scores[i],scores[i+1]))



is_max = False 
selected_cities_2 = [] 
scores_2 = []


for i in range(0,len(scores_1),2): 
    if not is_max:
        if scores_1[i] > scores_1[i+1]: 
            selected_cities_2.append(adjacent_cities[selected_cities[i+1]]) 
        else: 
            selected_cities_2.append(adjacent_cities[selected_cities[i]]) 
        scores_2.append(min(scores_1[i],scores_1[i+1]))


max_city_ind = 0

if scores_2[1] > scores_2[max_city_ind]: 
    max_city_ind = 1 
    if scores_2[2] > scores_2[max_city_ind]: 
        max_city_ind = 2


second_city = selected_cities_2[max_city_ind]
first_city = parent_cities[second_city]

third_city_options = city_coffee_region[second_city] 
third_city = None

for c in third_city_options: 
    if c in adjacent_cities:
        third_city = c


print(first_city)
print(second_city)
print(third_city)