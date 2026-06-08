# temp = 20
# is_raining = False
#
# if temp > 36 or temp < 0 or is_raining:
#     print("Raining")
# else:
#     print("not raining")

temp = 36
is_sunny = True
if temp>= 28 and is_sunny:
     print("it is hot outside 🥵🥵🥵")
     print("it is sunny outside ☀️☀️")
elif temp<=0 and is_sunny:
    print("it is not sunny outside ❄️")
    print("it is sunny ☀️ ")
elif 28 > temp > 0 and is_sunny:
    print("it is a good weather")
    print("it is sunny outside")
elif temp>= 28 and not is_sunny:
     print("it is hot outside 🥵🥵🥵")
     print("it is cloudy outside ☀️☀️")
elif temp<=0 and not is_sunny:
    print("it is not sunny outside ❄️")
    print("it is cloudy and chukked ☀️ ")
elif 28 > temp > 0 and not is_sunny:
    print("it is a good weather")
    print("it is  not sunny outside")
