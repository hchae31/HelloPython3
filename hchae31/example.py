def readUnit():
    mm = int(input('길이(mm)를 입력하세요: '))
    return mm

def convertUnit(mm):
    units = [mm]
    units.append(mm * 0.1)
    units.append(mm * 0.001)
    units.append(mm * 0.03937)
    units.append(mm * 0.003281)
    return units

def printUnits(units):
    print(f'''
    {units[0]} mm --> {units[1]} cm
    {units[0]} mm --> {units[2]} m
    {units[0]} mm --> {units[3]} inch
    {units[0]} mm --> {units[4]} ft
    ''')

products = {'쌀':9900, '상추 ':1900, '고추 ':2900, '마늘':8900,
            '통닭':5600, '햄 ':6900, '치츠 ':3900}
def readDiscount():
    print('''
    ----------------------------------
    -- 한빛 마트 오늘의 할인 가격표 출력 --
    ----------------------------------
    ''', end='')
    rate = int(input('오늘의 할인율은? '))
    return rate

def printPrice(dcprice, rate):
    result = ''
    for idx, k in enumerate(products):
        result += f'{k:4s} : {products[k]} 원 {rate} % DC -> {dcprice[idx]:,.0f}원\n'
    print(result)

def discountPrice(rate):
    dcprice = []
    dc = (1 - (rate / 100))
    for v in products.values():
        dcprice.append( v * dc)
    return dcprice