#Get the Car Code and Return the Origin City Administered the Car ID
car_code=input('enteryourcarcode by this format--> xxNxxxyy: ')
lastt=car_code[6]+car_code[7]
print('The 2 last digit of car code is: ',lastt)
lastt=int(lastt)

city_code_no=[

[15,25,35],
[17,27,37],
[68,78,21],
[13,23,43,53],
[91],
[98],
[48,58],
[11,22,33,44,55,66,77,88,99,10,20,30,40,50,60,70,80,90],
[71,81],
[12,32,42,52],
[14,24,34],
[87,97],
[86,96],
[85,95],
[63,73,83,93],
[16,26,36],
[79,89],
[19,29,39],
[45,65,75],
[51,61],
[49],
[46,56,76],
[59,69],
[31,41],
[62,72,82,92],
[47,57,67],
[18,28,38],
[84,94],
[54,64,74]

]
cities=[
'EastAzerbaijan',
'WestAzerbaijan',
'Alborzprovince',
'Isfahan',
'Ardabil',
'Ilam',
'Bushehr',
'GreaterTehran',
'ChaharmahalBakhtiari',
'Khorasan',
'Khuzestan',
'Zanjan',
'Semnan',
'SistanBaluchestan',
'Fars',
'Qom',
'Qazvin',
'Kermanshah',
'Kerman',
'Kurdistan',
'KohkiluyehBoyerAhmad',
'Gilan',
'Golestan',
'Lorestan',
'Mazandaran',
'Central',
'Hamedan',
'Hormozgan',
'Yazd'
]


index=0

for i in city_code_no:
    index=index+1
    for j in i:
        if j==lastt:
            index=index-1
            print(index)
            print(cities[index])
