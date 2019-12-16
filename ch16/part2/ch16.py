import math
from cmath import exp, pi

base = [0,1,0,-1]
def gen(n):
    while True:
        for _ in range(n):
            yield base[0]
        for _ in range(n):
            yield base[1]
        for _ in range(n):
            yield base[2]
        for _ in range(n):
            yield base[3]

n = '59773775883217736423759431065821647306353420453506194937477909478357279250527959717515453593953697526882172199401149893789300695782513381578519607082690498042922082853622468730359031443128253024761190886248093463388723595869794965934425375464188783095560858698959059899665146868388800302242666479679987279787144346712262803568907779621609528347260035619258134850854741360515089631116920328622677237196915348865412336221562817250057035898092525020837239100456855355496177944747496249192354750965666437121797601987523473707071258599440525572142300549600825381432815592726865051526418740875442413571535945830954724825314675166862626566783107780527347044' #input()
n *= 10000
print(len(n))
print(n.count('0'))

#N = len(n)
#nextN = math.floor(math.sqrt(N)) + 1
#nextN *= nextN
#n += '0'*(nextN-N)

print(len(n))
print(math.sqrt(len(n)))

#n = '12345678'
offset = int(n[:8])
n = list(map(int,n))

def fft(x):
    N = len(x)
    if N <= 1: 
        return x
    even = fft(x[0::2])
    odd =  fft(x[1::2])

    print(N//2)
    print(odd)
    print(list(range(N//2)))

    T= [odd[k] for k in range(N//2)]
    return [even[k] + T[k] for k in range(N//2)] + \
           [even[k] - T[k] for k in range(N//2)]

for i in range(100):
    fft(n)
    print(i)

