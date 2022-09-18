import string

alpha_list = list(map(str, string.ascii_letters + string.digits))


def get_index_different_char(chars):
    alpha = []
    non_alpha = []
    for i, char in enumerate(chars):
        if str(char) in alpha_list:
            alpha.append(i)
        else:
            non_alpha.append(i)

    return alpha[0] if len(alpha) == 1 else non_alpha[0]
