def myfunc(l):
    r = []
    p = q = None
    for x in l + [-1]:
        if x - 1 == q:
            q += 1
        else:
            if p:
               if q > p:
                   r.append('%s-%s' % (p, q))
               else:
                   r.append(str(p))
            p = q = x
    return '(%s)' % ', '.join(r)


lst = [8, 12, 38, 3, 17, 19, 25, 35, 50]
print(myfunc(lst))