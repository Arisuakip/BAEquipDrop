import json
import os
import datetime

def getList():
    Equip_Dic = {}
    with open (os.path.join(os.path.dirname(__file__),'stages.json'),'r',encoding='utf8') as fp:
            jsdata = json.load(fp)
            Campaign=jsdata['Campaign']
            for stage in Campaign:
                difficulty = 'N' if stage['Difficulty'] == 0 else 'H'
                stageCode = str(stage['Area']) + "-" + str(stage['Stage']) + difficulty
                if stageCode=="10-1N":
                    a=1
                stageRewards = stage['Rewards']['Default']
                for reward in stageRewards:
                    s = str(reward[0])
                    equip = int(str(reward[0])[-4:])
                    if len(s) != 7 or equip%1000 > 8:
                        continue
                    prefix = int(reward[0]/10000)
                    p = reward[1]
                    if prefix!=460:
                        itemsP = (stageCode,reward[1])
                        if equip not in Equip_Dic:
                            Equip_Dic[equip] = [itemsP]
                        else:
                            Equip_Dic[equip].append(itemsP)
                    elif prefix==460 and equip%1000 !=0:
                        itemsP1 = (stageCode,round(reward[1]/3,3))
                        itemsP2 = (stageCode,round(reward[1]*2/3,3))
                        Equip_Dic[equip-1].append(itemsP1)
                        Equip_Dic[equip].append(itemsP2)
                    else:
                        itemsP = (stageCode, reward[1])
                        Equip_Dic[equip].append(itemsP)
    for k,v in Equip_Dic.items():
        Equip_Dic[k] = sorted(v,key=lambda x:x[1],reverse=True)
    with open(os.path.join(os.path.dirname(__file__),"EquipDic.json"),'w') as fp:
        json.dump(Equip_Dic,fp)
def nameToId(name):
    if len(name) > 4 :
        return -1
    Level = name[:-2]
    EquipCN = name[-2:]
    LevelList = ["t1","t2","t3","t4","t5","t6","t7"]
    EquipList = ["帽子", "手套", "鞋子", "背包", "徽章","符咒","发卡","手表"]
    try:
        Lindex = LevelList.index(Level)
        Eindex = EquipList.index(EquipCN)
    except:
        return -1
    return str((Eindex+1)*1000+(Lindex))
def getStr(name):
    res = "|" + "{:^10}".format("关卡") + "|" + "{:^10}".format("概率") + "|\n"
    equipid = nameToId(name)
    with open(os.path.join(os.path.dirname(__file__),"EquipDic.json"), 'r', encoding='utf8') as fp:
        dic = json.load(fp)
    dropList = dic[equipid]
    for item in dropList:
        res = res+"|"+"{:^10}".format(item[0])+"|"+"{:^10}".format(str(item[1]*100)+"%") + "|\n"
    return res

if __name__ == '__main__':
    getList()
    s = "t3鞋子"
    a = getStr(s)
    print(a)

