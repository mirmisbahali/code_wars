def printer_error(s):
    n_z = ''.join(list(map(chr, range(110,123))))
    nr = 0
    for i in s:
        if i in n_z:
            nr += 1
    return f'{nr}/{len(s)}'
