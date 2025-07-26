import sys

num_trains = int(sys.stdin.readline())
train_data = []

for idx in range(num_trains):
    original_line = sys.stdin.readline().strip()
    parts = original_line.split()
    hour, minute = map(int, parts[-1].split(":"))
    total_minutes = hour * 60 + minute
    parts[-1] = total_minutes
    train_data.append((parts, idx, original_line))

for i in range(num_trains):
    selected = i
    for j in range(i + 1, num_trains):
        curr_train, curr_idx, _ = train_data[selected]
        next_train, next_idx, _ = train_data[j]

        if curr_train[0] > next_train[0]:
            selected = j
        elif curr_train[0] == next_train[0]:
            if curr_train[-1] < next_train[-1]:
                selected = j
            elif curr_train[-1] == next_train[-1] and curr_idx > next_idx:
                selected = j

    if selected != i:
        train_data[i], train_data[selected] = train_data[selected], train_data[i]

for entry in train_data:
    time_in_minutes = entry[0][-1]
    formatted_time = f"{time_in_minutes // 60:02d}:{time_in_minutes % 60:02d}"
    original = entry[2].rsplit(' at ', 1)[0]
    result = f"{original} at {formatted_time}"
    sys.stdout.write(result + '\n')
