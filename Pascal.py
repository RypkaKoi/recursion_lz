def pascal(x):
    if x == 1:
        return [[1], [1,1]] #конец рекурсии
    else:
        #Рекурсия идет сверху вниз
        last = pascal(x-1)
        last_elem = last[-1]
        first_elem = [1]
        for i in range(1, len(last_elem)): #Цикл для треугольника паскаля
            first_elem.append(last_elem[i-1] + last_elem[i])
        first_elem.append(1)
        return last + [first_elem] #наша рекурсия
    

riad = int(input('До какого ряда треугольник(учитывая нулевой ряд) ')) #Наши ряды, где 1 самый верхний
vivod = pascal(riad) #Наша функция

for riad in vivod: #Выводим по рядам
    print(riad)