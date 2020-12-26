import json
import os

def init():
    global entire_memo
    f = open(os.path.abspath("C:\\memo.txt"), 'r')
    entire_memo = json.loads(f.read())
    f.close()
    

def save():
    f = open(os.path.abspath("C:\\memo.txt"), 'w')
    f.write(str(entire_memo).replace("\'", "\""))
    f.close()


def set_memo(name, content):
    if name in entire_memo:
        entire_memo[name].append(content)
    else:
        entire_memo[name] = [content]
    save()

def show_memo(name):
    try:
        memo = entire_memo[name]
        ret = name + "의 메모 리스트입니다.<br>"
        for i in range(len(memo)):
            ret += (str(i + 1) + ": " + memo[i] + "<br>")

        return ret.strip()
    except:
        return "메모를 등록한 적 없는 사용자입니다."

def del_memo(name, num):
    num = num - 1
    if num < len(entire_memo[name]):
        del entire_memo[name][num]
    save()