import json

def init():
    global entire_memo
    f = open("C:\\memo.txt", 'r')
    entire_memo = json.loads(f.read())
    

def save():
    f = open('C:\\memo.txt', 'w')
    f.write(str(entire_memo).replace("\'", "\""))


def get_memo(name):
    return entire_memo[name]

def set_memo(name, content):
    if name in entire_memo:
        entire_memo[name].append(content)
    else:
        entire_memo[name] = [content]
    save()

def show_memo(name):
    memo = get_memo(name)
    ret = name + "의 메모 리스트입니다.<br>"
    for i in range(len(memo)):
        ret += (str(i + 1) + ": " + memo[i] + "<br>")

    return ret.strip()

def del_memo(name, num):
    num = num - 1
    if num < len(name):
        del entire_memo[name][num]
    save()