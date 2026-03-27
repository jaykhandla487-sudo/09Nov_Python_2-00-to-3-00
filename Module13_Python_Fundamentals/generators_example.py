def even_generator():
    for i in range(2,21,2):
        yield i

for num in even_generator():
    print(num)