def solve():
    passport_name = input()
    db_name = input()

    if passport_name == db_name:
        return "OK"

    passport_name_length = len(passport_name)
    db_name_length = len(db_name)

    if abs(passport_name_length - db_name_length) >= 2:
        return "FAIL"

    passport_name = "".join(sorted(passport_name))
    db_name = "".join(sorted(db_name))

    # NOTE: OK, at this point names differ by no more than 1 character.
    if len(passport_name) > len(db_name):
        main_string = passport_name
    else:
        main_string = db_name

    if main_string is passport_name:
        substring = db_name
    else:
        substring = passport_name

    # TODO: What do you do next?

    return "OK"


if __name__ == "__main__":
    print(solve())
