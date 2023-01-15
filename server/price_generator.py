import random

weight_dict = {
    "free": 15,
    "not": 500,
}
# random key

def generate_price():
    key = random.choice(list(weight_dict))
    if key == "free":
        return 0
    else:
        price = random.randint(1, 80)
        rounded = price - (price % 10)
        return rounded


print(generate_price())