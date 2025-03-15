import json

with open("all.json", "r", encoding="utf-8") as file:
    data = json.load(file)

country_input = input("Enter the country name: ") # User input


for country in data:
    country_name = country['name']['common']
    if country_name.lower() == country_input.lower():
        print("Capital: ", country['capital'][0])
        break
else:
    print("Country not found")
