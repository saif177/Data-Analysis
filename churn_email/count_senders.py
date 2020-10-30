def count_number_of_lines():
    count = 0
    with open('mbox-short.txt') as f:
        for fl in f:
            fl = fl.rstrip()
            if fl.startswith('Subject:'):
                count+=1
    return count

count_number_of_lines()
