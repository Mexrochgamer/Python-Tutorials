counter = 0
while counter < 100:
    counter += 1

    if not counter % 2:
        continue

    print(counter)