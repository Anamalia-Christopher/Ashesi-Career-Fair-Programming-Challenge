def mode(a):
    dic={}
    for i in a:
        if i in dic:
            dic[i]=dic[i]+1
        else:
            dic[i]=1
    mode= max(dic.values())
    

    nmode=[]
    for item in dic:
        if dic[item]==mode:
            nmode.append(item)
    print(nmode)

    
mode(['Guinea', 'Guinea', 'Liberia', 'Guinea', 'Guinea', 'Guinea', 'Guinea', 'Guinea', 'Guinea', 'Guinea', 'Guinea', 'Guinea', 'Guinea', 'Guinea', 'Guinea', 'Guinea', 'Guinea', 'Guinea', 'Guinea', 'Guinea', 'Guinea', 'Guinea', 'Guinea', 'Guinea', 'Guinea', 'Guinea', 'Guinea', 'Guinea', 'Guinea', 'Guinea', 'Guinea', 'Guinea', 'Guinea', 'Guinea', 'Guinea', 'Guinea', 'Guinea', 'Guinea', 'Guinea', 'Guinea', 'Guinea', 'Guinea', 'Guinea', 'Guinea', 'Guinea', 'Guinea', 'Guinea', 'Guinea', 'Guinea'])