import csv
# 用list保存下来，否则迭代器指向到最后了，再次遍历的时候本质是从最后一个开始遍历，那么之后什么都没有了，所以读不出任何数据
data = list(csv.reader(open("/mnt/hgfs/UbuntuShareDir/JinChanChan/tools/heroes/heroList.csv", encoding='utf-8')))

def getHeroNodes(data):
    heroNodeList = []
    for hero in data:
        # hero[0] id
        # hero[1] name
        # hero[2] skill
        # hero[3] skill desc
        # hero[4] desc
        # hero[5] bond
        # hero[6] price
        heroNodeList.append(
            {"key": hero[0], "name": hero[1], "color": "lightgreen"} #TODO getHeroNodeColorByPrice(price) 颜色要根据价值决定
        )
    return heroNodeList

def getHeroEdges(bondHerosMap):
    heroEdgeList = []
    for bond in bondHerosMap:
        heroList = bondHerosMap[bond]
        for index in range(0, len(heroList)):
            # 如果这是这个羁绊的最后一个英雄，那么也没有必要去画边了
            if len(heroList)-1 == index:
                continue
            hero = heroList[index]
            heroEdgeList.append(
                { "from": hero[0], "to": heroList[index+1][0], "text": bond} # TODO 羁绊也应该有自己的边的颜色 getHeroEdgeColorByBond(price)
            )
        
    return heroEdgeList

def getBondHerosMap(data):
    bondHerosMap = {
        # bond1 : [hero1(是一个list), hero2], ...
    }
    for hero in data:
        for bond in hero[5].split('，'): # 因为羁绊用逗号隔开了所以要先分割出来
            if bond in bondHerosMap.keys():
                bondHerosMap[bond].append(hero)
            else:
                bondHerosMap[bond] = [hero]
    return bondHerosMap


def main(data):
    nodes = getHeroNodes(data)
    print(nodes)
    print("=======")
    bondHerosMap = getBondHerosMap(data)
    edges = getHeroEdges(bondHerosMap)
    print(edges)

main(data)
