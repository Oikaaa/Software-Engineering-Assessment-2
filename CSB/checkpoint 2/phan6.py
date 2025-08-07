district = ["BD", "BTL", "CG", "DD", "HBT"]
population = [247100, 333300, 266800, 420900, 318000]
area = [9.224, 43.35, 12.04, 9.96, 10.09]
whole_density = 0

for i in range(len(area)):
    density = population[i]/area[i]
    whole_density = whole_density + density
    print(f"{district[i]}: {density}")

average = whole_density/len(district)

print(f"Average population density:\n{average}")