def slice_str(mess: str, subj='>', option='find'):
    tmp = find_str(mess, subj, option)

    if tmp == -1 or mess is None:
        return None
    else:
        return mess[tmp + len(subj):]


def rslice_str(mess: str, subj='>', option='find'):

    tmp = find_str(mess, subj, option)

    if tmp == -1 or mess is None:
        return None
    else:
        return mess[:tmp]


def find_str(mess: str, subj='>', option='find'):
    tmp = -1
    if mess is None:
        return None

    match option:

        case 'find':
            tmp = mess.find(subj)

        case 'rfind':
            tmp = mess.rfind(subj)

    return tmp
