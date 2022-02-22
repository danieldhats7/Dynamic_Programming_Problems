n = 3
inputs = ['0 30', '5 10', '15 20']
concerts = []
for i in range(n):
    concerts.append(list(map(lambda x: int(x), inputs[i].split())))
concerts = sorted(concerts, key= lambda x: x[0])
arr = [[concerts[0]]]
for concert in concerts[1:]:
    
    for sala_idx in range(len(arr)):
        meter = True
        sala = arr[sala_idx]
        for con in sala:
            range_con = range(con[0], con[1])
            if concert[0] in range_con or concert[1] in range_con:
                meter = False
                break
        if meter:
            sala.append(concert)
            break
        
    if not meter:
        arr.append([concert])
            
print(len(arr))

