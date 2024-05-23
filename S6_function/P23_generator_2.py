# from time import perf_counter


# def list_range(start, end, step=1):
#     new_range = []
#     while start < end:
#         new_range.append(start)
#         start += step
#     return new_range


# def generator_range(start, end, step=1):

#     while start < end:
#         yield start
#         start += step


# start = perf_counter()
# lr = list_range(1, 10000)
# sum = 0
# for i in lr:
#     if i == 3:
#         break
#     sum += i**2

# end = perf_counter()
# print("list range time : ", end - start)


# start_ = perf_counter()
# gr = generator_range(1, 10000)
# sum = 0
# for j in gr:
#     if j == 3:
#         break
#     sum += j**2

# end_ = perf_counter()
# print("generator range time : ", end_ - start_)


def my_generator(r=10):
    for i in range(r):
        yield i**2


generator = my_generator()
# generator.close()
# generator.throw()
print(sum(generator))
