# fmt: off
NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


# fmt: on


def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
    each name appears only once"""
    title_case_names = [name.title() for name in names]
    return list(set(title_case_names))


dedup_and_title_case_names(NAMES)


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    names.sort(key=lambda x: x.split()[-1], reverse=True)
    return names


sort_by_surname_desc(NAMES)


def shortest_first_name(names):
    """Returns the shortest first name (str).
    You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    first_names = [x.split()[0] for x in names]
    first_names.sort(key=len)
    return first_names[0]


shortest_first_name(NAMES)
