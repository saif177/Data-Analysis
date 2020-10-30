def count_message_from_email():
    with open('mbox-short.txt') as f:
        message = [i.split(' ')[1] for i in f if i.startswith('From ')]
        sender = {}
        for mes in message:
            sender[mes]=message.count(mes)
        return sender
print(count_message_from_email())
