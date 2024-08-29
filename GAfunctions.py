from random import randrange, sample, choice

ScMap = {
    '10':['9'],
    '9':['10','17','14'],
    '17':['9','14','8'],
    '14':['9','17','8'],
    '8':['7','17','14','23'],
    '7':['8','23','11','4','6','18'],
    '18':['7','6'],
    '6':['7','18','4','24','22'],
    '22':['6','3','19','5'],
    '5':['22','19'],
    '19':['22','5','2','3'],
    '2':['19','3','16'],
    '16':['2','3','4','21','1'],
    '1':['16','21','11','12','20'],
    '20':['1','12','13'],
    '13':['11','12','15'],
    '15':['13'],
    '11':['23','7','4','21','1','12','13'],
    '23':['8','7','11'],
    '4':['7','6','24','21','3','11'],
    '24':['6','4','3'],
    '3':['24','22','19','2','16','4'],
    '21':['11','4','16','1'],
    '12':['11','1','20','13']
}

ScPositions = {
    '1': (682, 307),
    '2': (705, 188),
    '3': (633, 177),
    '4': (553, 230),
    '5': (682, 80),
    '6': (543, 115),
    '7': (439, 180),
    '8': (326, 194),
    '9': (144, 162),
    '10': (72, 146),
    '11': (518, 333),
    '12': (643, 384),
    '13': (609, 439),
    '14': (268, 221),
    '15': (575, 492),
    '16': (673, 237),
    '17': (241, 155),
    '18': (471, 98),
    '19': (661, 129),
    '20': (691, 390),
    '21': (614, 272),
    '22': (620, 90),
    '23': (384, 262),
    '24': (576, 185)
}

ScColors = {
    0 : [65,105,225],
    1 : [255,0,0],
    2 : [0,255,0],
    3 : [255,255,0]
}


def adapt(crom):
    score = 24
    for i in range(1, 25):
        for j in ScMap[str(i)]:
            if crom[str(i)] == crom[j]:
                score -= 1
                break
    return score


def generatePop():
    crom_list=[]
    for _ in range(0,10):
        crom = {}
        for i in range(1, 25):
            crom[str(i)] = randrange(0, 4)
        adaptation = adapt(crom)
        crom_list.append((adaptation,crom))
    return crom_list


def Cross(pop):
    crom_list =[]
    for i in range(0,5):
        for j in range(0,5):
            if i == j:
                continue
            n = randrange(1, 5)
            cross_list = sample(sorted(ScMap), k=n)
            pop_cross1= pop[i][1].copy()
            pop_cross2 = pop[j][1].copy()
            for x in cross_list:
                aux = pop_cross1[x]
                pop_cross1[x] = pop_cross2[x]
                pop_cross2[x] = aux
            adaptation1 = adapt(pop_cross1)
            crom_list.append((adaptation1, pop_cross1))
            adaptation2 = adapt(pop_cross2)
            crom_list.append((adaptation2, pop_cross2))
    return crom_list


def Mutate(pop):
    crom_list = []
    for i in range(0,5):
        n = randrange(4,11)
        mutate_list = sample(sorted(ScMap), k=n)
        pop_mutate = pop[i][1].copy()
        for x in mutate_list:
            colors = [0,1,2,3]
            colors.remove(pop_mutate[x])
            pop_mutate[x] = choice(colors)
        adaptation = adapt(pop_mutate)
        crom_list.append((adaptation,pop_mutate))
    return crom_list
