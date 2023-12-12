class DaysOfWeekIterator:
    current_day = 0

    def __iter__(self):
        self.current_day = 0
        return self

    def __next__(self):
        result = self.current_day
        self.current_day = (self.current_day + 1) % 7
        return result


print("====DaysIterator=====")
days_of_week_iter = DaysOfWeekIterator()
for _ in range(14):
    print(next(days_of_week_iter))
print("=====================")
