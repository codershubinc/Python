# Problem: Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).


distance = 3    
mode = 'Walk' if distance < 3 else 'Bike' if distance < 15 else 'Car'
print(mode)