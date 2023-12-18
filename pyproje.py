liste = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

def flat(l):
    flatten = []
    
    for i in l:
        if type(i) != list:
            flatten.append(i)
        else:
            flatten.extend(flat(i))
    
    return flatten

def reverse(l):
    l.reverse()
    for i in l:
        if type(i) == list:
            i.reverse()
            
    return l


print(reverse(liste))
        