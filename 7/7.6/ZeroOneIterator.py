class ZeroOneIterator:

    def __iter__(self):
        self.value = 0
        return self

    def __next__(self):
        result = self.value
        self.value = 1 - self.value
        return result


print("====Iteratior0-1=====")
zero_one_iter = ZeroOneIterator()
for _ in range(10):
    print(next(zero_one_iter))
print("=====================")
