"""
Create a counter.
"""
class Counter:
        current = 0
        def __init__(self, start=None, end=None):
            self.start = start
            self.end = end

        def increase(self):
            if self.current < self.end:
                self.current += 1
                return self.current
            else:
                return print('Out of range')

        def current_value(self):
            current = 0
            self.current = current
            if current <= 5:
                return current
            else:
                return f"Value is higher than {current}"

my_count = Counter(start=0, end=5)

my_count.increase()
my_count.increase()
my_count.increase()
my_count.increase()
my_count.increase()
my_count.increase()
print(my_count.current)
