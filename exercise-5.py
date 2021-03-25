fib = [0]

for i in range(50):
    print(f'term: {i} / number: {fib[i]}')

    if i == 0:
        fib.append(1)
    else:
        fib.append(fib[i] + fib[i-1])

print(fib)