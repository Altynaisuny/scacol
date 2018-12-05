def fun(*args,**aa):

    print(len(aa))
    for key in aa:
        print(aa[key])


aa = {'a':{'c':0},
        'b':{'c':0}}

fun(**aa)