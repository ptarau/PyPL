replacemetns = {
    'cat': 'dog',
    'nice': 'ugly'
}


def replace_in_file(infile, outfile):
    with open(outfile, 'w') as outf:
        with open(infile, 'r') as inf:
            for line in inf.readlines():
                for key, val in replacemetns.items():
                    line = line.replace(key, val)
                print(line, file=outf,end='')


replace_in_file('old.txt', 'new.txt')
