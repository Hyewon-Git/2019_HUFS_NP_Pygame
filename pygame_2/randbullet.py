import random

random_value = []
random_value2 = []
random_value3 = []
random_value = random.sample(range(1, 790), 10)
random_value2 = random.sample(range(-5,6),10)
random_value3 = random.sample(range(-5,6),10)
for i in range(10):
    if random_value2[i]==0:
        random_value2[i] =3
    if random_value3[i]==0:
        random_value3[i] =-3
d=0


## 여기까지가 랜덤변수 미리설정
def boss_pattern6():
    global bossmissile6,random_area,d
    while d <5:
        bossmissile6[d].x = random_value[d]
        d+=1
    for i in range(len(bossmissile6)):
        bossmissile6[i].x += random_value2[i]
        bossmissile6[i].y += random_value3[i]
        bossmissile6[i].render()
    for i in range(5):
        if bossmissile6[i].x > 800 or bossmissile6[i].x < 0 or bossmissile6[i].y > 800 or bossmissile6[i].y < 0:
            bossmissile6[i].x = random.randrange(1,799)
            bossmissile6[i].y = random.randrange(1,799)