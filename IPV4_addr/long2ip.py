import socket,struct
import pandas as pd 
def getbin(s):
    _s=bin(abs(s))
    _s=_s.replace('0b','').rjust(32,'0')
    return _s


def rev(s):                     #反码操作
    s=s.replace('1','2')
    s=s.replace('0','1')
    s=s.replace('2','0')
    return s

def f(s):
    global _s
    if flag==0:
        return
    else:
        _s=rev(_s)
    return

def y(s):
    return str(_s).rjust(32,str(flag))    #不够32位补0

def by(s):
    global _s
    _s=int(_s,2)+1
    _s=getbin(_s)
    return str(_s).rjust(32,str(flag))      ##不够32位补1


def out(s):
    f(s)
    if (flag):
        return by(s)  #正整数直接输出原码
    else:
        return y(s)   #负数输出补码


def bin2int(_s):

    _s=int(_s,2)
    return (socket.inet_ntoa(struct.pack('!L', _s)))     #转为IP地址

    

origin=pd.read_excel(r"ipadd_int.xlsx")
processed=[]
for i in origin["地址"]:
    s=int(i)
    if s>=0:
        flag=0
    else:
        flag=1
    _s=getbin(s)
    s=out(s)
    processed.append(bin2int(s))

name=["转化后地址"]
processed=pd.DataFrame(columns=name,data=processed)
processed.to_excel("processed.xlsx", index=False, encoding="utf-8")







