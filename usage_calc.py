import json
import operator

messages = json.load(open('messages.json'))['messages']

users = {}
message_count = 0.0
word_count = 0.0

for m in messages:
    user = m['sender']
    text = m['text'].strip().split(' ')
    if user in users:
        users[user] = (users[user][0] + 1, users[user][1] + len(text))
    else:
        users[user] = (1, len(text))
    message_count += 1
    word_count += len(text)

for k in users:
    users[k] = (100 * users[k][0] / message_count,
                100 * users[k][1] / word_count)

sorted_users = sorted(users.items(), key=operator.itemgetter(1), reverse=True)

usage = open('usage.tsv', 'w')
usage.write('%s\t%s\t%s\n' % ('User', 'Message Frequency', 'Word Frequency'))
for user, (msg_pct, word_pct) in sorted_users:
    usage.write('%s\t%.5f%%\t%.5f%%\n' % (user, msg_pct, word_pct))
usage.close()
