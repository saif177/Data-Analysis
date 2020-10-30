def count_message_from_domain():
    with open('mbox-short.txt') as f:
        m = [i.split(' ')[1] for i in f if i.startswith('From ')]
        domain = [j.split('@')[1] for j in m]
        sender = {}
        for mes in domain:
            sender[mes]=domain.count(mes)
        print(sender)
count_message_from_domain()
