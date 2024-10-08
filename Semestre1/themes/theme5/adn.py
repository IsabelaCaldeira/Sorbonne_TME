def base_comp(base: str) -> str:
    if base == 'A':
        return 'T'
    elif base == 'T':
        return 'A'
    elif base == 'C':
        return 'G'
    else:
        return 'C'

assert base_comp('A') == 'T'
assert base_comp('G') == 'C'
assert base_comp('C') == 'G'
assert base_comp('T') == 'A'

