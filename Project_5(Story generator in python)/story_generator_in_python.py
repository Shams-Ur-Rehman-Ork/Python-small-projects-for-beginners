import random


def story_generator():
    when = ["A few years ago", "Yesterday",
            "Last night", "A long time ago",
            "On 1st January", "A month ago"]

    who = ["A rabbit", "An elephant", "A mouse", "A turtle", "A cat"]

    name = ["Ali", "James", "Daniel", "Sasha", "Samuel"]

    residence = ["India", "Russia", "Germany", "England", "USA"]

    went_to = ["Cinema", "University", "Seminar", "School", "Gym"]

    happened = ["Made a lot of friends", "Eats a burger",
                "Made some friends", "Found a secret key",
                "Solved a mistery", "Wrote a book"]

    random_story = f"{random.choice(when)}, {random.choice(who)} " \
                   f"whose name was {random.choice(name)} lived in {random.choice(residence)}, " \
                   f"went to the {random.choice(went_to)} and " \
                   f"{random.choice(happened)}."

    return random_story


print(story_generator())
