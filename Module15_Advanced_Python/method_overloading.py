class Math:

    def add(self, a, b=0, c=0):
        return a + b + c

m = Math()

print(m.add(5))
print(m.add(5,3))
print(m.add(5,3,2))