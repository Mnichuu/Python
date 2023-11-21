import random


class RandomDirectionIterator:
    def __iter__(self):
        return self

    def __next__(self):
        directions = ["N", "E", "S", "W"]
        return random.choice(directions)


print("===RandomIteratior===")
random_direction_iter = RandomDirectionIterator()
for _ in range(10):
    print(next(random_direction_iter))
print("=====================")