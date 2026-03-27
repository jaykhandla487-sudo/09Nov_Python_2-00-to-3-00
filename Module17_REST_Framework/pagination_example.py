numbers = list(range(1, 51))

page_size = 10

for i in range(0, len(numbers), page_size):

    page = numbers[i:i+page_size]

    print("Page:", page)