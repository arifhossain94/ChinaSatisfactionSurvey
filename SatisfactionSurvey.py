import sys


rating_records = []


def start_message():
    print("Welcome to China Border Protection\n===== Satisfaction Survey ========")
    print("1- Submit Rating\n2- View Rating\n3- Reset Rating\n0- Exit ")

    user_input = -1

    while user_input < 0 or user_input > 3:
        user_input = int(input("Your Choice? "))

    return user_input


def submit_rating():
    while True:
        rating = int(input("Your rating (1-4)? "))
        if 1 <= rating <= 4:
            rating_records.append(rating)
            break
    return rating


def view_ratings():
    print(rating_records)


def reset_rating():
    rating_records.clear()
    print("The ratings for this officer is reset.")


def start_survey():
    response = start_message()

    if response == 0:
        sys.exit()
    elif response == 1:
        submit_rating()
    elif response == 2:
        view_ratings()
    else:
        reset_rating()


# start_survey()

# print(rating_records)
