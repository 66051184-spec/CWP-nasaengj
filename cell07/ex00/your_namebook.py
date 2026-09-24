def array_of_names(persons):
    """
    Takes a dictionary associating first names with last names.
    Returns an array of full names "Firstname Lastname" with
    the first letter of each capitalized.
    """
    result = []
    for first, last in persons.items():
        full_name = f"{first.capitalize()} {last.capitalize()}"
        result.append(full_name)
    return result


if __name__ == "__main__":
    persons = {
        "jean": "valjean",
        "grace": "hopper",
        "xavier": "niel",
        "fifi": "brindacier"
    }
    print(array_of_names(persons))
