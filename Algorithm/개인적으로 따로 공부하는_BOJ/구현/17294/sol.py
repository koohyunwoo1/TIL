N = list(map(int, list(input())))

if len(N) == 1 :
    print('◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!')

else :
    value = int(N[0]) - int(N[1])
    for i in range(len(N)-1) :
        if N[i] - N[i+1] != value :
            print('흥칫뿡!! <(￣ ﹌ ￣)>')        
            break

    else : 
        print('◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!')