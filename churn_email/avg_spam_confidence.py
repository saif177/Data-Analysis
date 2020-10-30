def average_spam_confidence():
    count = 0
    spam_sum = 0
    with open('mbox-short.txt') as f:
        for fl in f:
            fl = fl.rstrip()
            if fl.startswith('X-DSPAM-Confidence:'):
                var,value = fl.split(':')
                spam_sum+=float(value)
                count+=1
    print(spam_sum/count)
average_spam_confidence()
