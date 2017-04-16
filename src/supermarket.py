def queue_time(customers, n):
    if n == 1:
        return sum(customers)
    if len(customers) < n:
        return max(customers)
    line = customers[n:]
    checkout = customers[:n]
    time = 0
    while checkout:
        time += min(checkout)
        checkout = [(x - min(checkout)) for x in checkout if (x - min(checkout) > 0)]
        while len(checkout) < n and line:
            checkout.append(line[0])
            line.pop(0)
    return time
