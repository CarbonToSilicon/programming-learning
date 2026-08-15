def my_generator(r):
    for i in range(r):
        yield i

run = my_generator(51)
print(next(run))
print(next(run))
print(next(run))
print(next(run))
print(next(run))
print("")
for i in run:
    print(i)

