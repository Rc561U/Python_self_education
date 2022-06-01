import csv
import re
import operator

with open('error.log') as log:
    text = log.readlines()
    dick = []
    for line in text:
        dick.append(line[:-1].split(maxsplit=6)[-1])

    pattern = "^[\w ]* "
    result = []
    for i in dick:
        result.append(*re.findall(pattern, i))

    x = ' '.join(result)
    di = {i: x.count(i) for i in result}
    result = (sorted(di.items(), key=operator.itemgetter(1), reverse=True))
    dictionary = {i: e for i, e in result}

    with open('error_message.csv', 'w', newline='') as w:
        headline = ['Error', 'Count']
        writer = csv.writer(w)
        writer.writerow(headline)
        for i in dictionary.items():
            writer.writerow(i)
        print('Create error_message.csv')

with open('error.log') as e:
    error = e.readlines()
    with open('info.log') as i:
        info = i.readlines()
        with open('syslog.log') as s:
            text = s.readlines()
            pat = '\((.*?)\)'
            result = []
            for i in text:
                result.append(*re.findall(pat, i))
            result = sorted(set(result))
            error = ''.join(error)
            info = ''.join(info)
            final_result = []
            for i in result:
                final_result.append([i, info.count('(' + i + ')'), error.count(f'({i})')])
            with open('user_statistics.csv', 'w', newline='') as w:
                writer = csv.writer(w)
                headline = ['Username', 'INFO', 'ERROR']
                writer.writerow(headline)
                for i in final_result:
                    writer.writerow(i)
                print('Create user_statistics.csv')
