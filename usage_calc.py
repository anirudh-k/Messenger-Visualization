import json
import operator

messages = json.load(open('messages.json'))['messages']

users = {}
count = 0.0

for m in messages:
    user = m['sender']
    if user in users:
        users[user] += 1
    else:
        users[user] = 1
    count += 1

for k in users:
    users[k] = 100 * users[k] / count

sorted_users = sorted(users.items(), key=operator.itemgetter(1), reverse=True)

usage = open('usage.tsv', 'w')
usage.write('%s %s\n' % ('User', 'Frequency'))
for user, pct in sorted_users:
    usage.write('%s %.5f%%\n' % (user, pct))
usage.close()
