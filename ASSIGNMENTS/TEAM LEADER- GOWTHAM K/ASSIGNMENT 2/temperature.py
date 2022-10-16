import random
while(True):
    temp = random.randint(0, 100)
    humidity = random.randint(0, 100)
    if temp >= 40 or humidity>=40:
        print(f"climate Alert ! temp={temp} and Humidity={humidity}")
