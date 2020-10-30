def find_email_sent_days():
    with open('mbox-short.txt') as f:
        d = [i.split(' ')[2] for i in f if i.startswith('From ')]
        days = {}
        for day in d:
            days[day]=d.count(day)
        print (days)

find_email_sent_days()
