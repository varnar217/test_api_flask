import json
import os
def read_districts():
    obj=[]
    with open(os.path.join('Rest project 1', 'districts.json'), 'r', encoding='utf-8-sig') as f:

        obj=(json.load(f))

    return obj

def read_streets():
    #obj=[]
    with open(os.path.join('Rest project 1', 'streets.json'), 'r', encoding='utf-8-sig') as f:
        #data=f.read()
        obj=(json.load(f))
    return obj

def read_volunteers():
    with open(os.path.join('Rest project 1', 'volunteers.json'), 'r', encoding='utf-8-sig') as f:
        #data=f.read()
        obj=(json.load(f))
    return obj

if __name__ == '__main__':
    read_districts()
    read_streets()
    read_volunteers()
