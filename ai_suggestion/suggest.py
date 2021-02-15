from math import sqrt, isnan

def euclidian(dest1, dest2):
    res = 0

    for x, y in zip(dest1, dest2):
        res += pow(x-y, 2)

    res = sqrt(res)
    return res

def psimilar(similar):
    return 1/(1+similar)

def similar(data, user1, user2):
    dest1=[]
    dest2=[]

    for datum in data[user1]:
        value1 = data[user1][datum]

        if not isnan(value1):
            if datum in data[user2]:
                value2 = data[user2][datum]

                if not isnan(value2):
                    dest1.append(value1)
                    dest2.append(value2)

    return euclidian(dest1, dest2)

def getsimilaruser(data, user):
    similars={}

    for other in list(data.keys()):
        if other != user:
            s = similar(data, user, other)
            similars.setdefault(other, psimilar(s))

    return similars

def getsuggest(data, user):
    similarusers = getsimilaruser(data, user)
    suggest={}

    for datum in data[user]:
        value=data[user][datum]
        
        if isnan(value):
            total=0
            simtotal=0

            for simuser in similarusers:
                valueuser = data[simuser][datum]

                if not isnan(valueuser):
                    total += valueuser * similarusers[simuser]
                    simtotal += similarusers[simuser]
                    
            suggest.setdefault(datum, total / simtotal)
    
    return suggest

