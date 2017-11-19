import json

with open('messages.txt') as messages:
    data = {}
    data['messages'] = []
    for message in messages.read().splitlines()[3:]:
        if len(message) > 0 and message[0] == '[':
            timestamp = message[1:23]
            sender = message[25:].split(':')[0]
            text = ''.join(message[25:].split(':')[1:])
            data['messages'].append({
                'timestamp': timestamp,
                'sender': sender,
                'text': text
            })
    messages_json = open('messages.json', 'w')
    messages_json.write(json.dumps(data, indent=4))
    messages_json.close()
