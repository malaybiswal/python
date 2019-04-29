def match(nuts,bolts):
    dict={}
    for nut in nuts:
        for bolt in bolts:
            if(nut[1:2]==bolt[1:2]):
                dict[nut]=bolt
                continue
    return dict



nuts=['N3','N2','N4','N1']
bolts=['B4','B1','B3','B2']
print(match(nuts,bolts))
