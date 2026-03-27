from pprint import pprint


def obtain_timetable():
    n = int(input())
    timetable = []

    for _ in range(n):
        line = input().split()
        start, end = line
        start = start.split(".")
        end = end.split(".")
        slot = []

        for z in (start, end):
            if len(z) == 1:
                z = [int(z[0]), 00]
            else:
                minutes = z[1].ljust(2, "0")
                z = [int(z[0]), int(minutes)]
                pass
            slot.append(z)

        timetable.append(slot)

    timetable.sort()
    return timetable


# NOTE: An example of a timetable.
# [[[5, 0], [21, 0]],
#  [[7, 0], [14, 0]],
#  [[8, 0], [22, 0]],
#  [[9, 0], [23, 0]],
#  [[12, 0], [14, 0]],
#  [[19, 0], [19, 0]],
#  [[22, 0], [23, 0]]]


def find_slot(current_time, timetable, visited):
    """Find a time slot which has not started and which has minimum end time."""
    found_slot = None
    found_i = -1

    for i, slot in enumerate(timetable):
        if slot[0] < current_time:
            continue

        # NOTE: slot[0] >= current_time at this point.
        # Have we already used this time slot?
        if visited[i]:
            continue

        if found_slot is None:
            found_slot = slot
            found_i = i
        else:
            if slot[1] < found_slot[1]:
                found_slot = slot
                found_i = i

    if found_i != -1:
        visited[found_i] = True
    return found_slot


def solve():
    timetable = obtain_timetable()
    current_time = min(timetable, key=lambda x: x[0])[0]
    visited = [False for _ in range(len(timetable))]

    total_count = 0
    chosen_slots = []

    while True:
        slot = find_slot(current_time, timetable, visited)

        if not slot:
            break

        current_time = slot[1]
        total_count += 1
        chosen_slots.append(slot)

    return total_count, chosen_slots


def present_the_results(total_count, chosen_slots):
    print(total_count)

    for slot in chosen_slots:
        for time in slot:
            time_string = " ".join(map(str, time))
            hours_part, minutes_part = time_string.split(" ")

            if minutes_part == "0":
                minutes_part = ""
            print(
                hours_part + (("." + minutes_part) if minutes_part else ("")), end=" "
            )

        print()


if __name__ == "__main__":
    present_the_results(*solve())
