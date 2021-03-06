# ПИДОРАС
Язык программирования

# Основы
Файлы сохраняются с расширением ```.pdrs```
В коде программы не допускаются комментарии, пробелы и перенос строки рядом со скобками и знаком умножения

У нас есть основной зацикленный массив размером 256 ячеек и два индекса типа данных byte (0...255)

## Команды
* ```П``` - Добавить в ячейку с главным индексом 1
* ```И``` - Вывести ячейку с главным индексом
* ```Д``` - Увеличить главный индекс на 1
* ```О``` - Увеличить второстепенный индекс на 1
* ```Р``` - Запросить у пользователя данные
* ```А``` - Подставить значение ячейки с главным индексом
* ```С``` - Подставить значение ячейки с второстепенным индексом

## Вспомогательные конструкции
Можно создать функцию. Для этого нужно ввести символ, который не занят и в скобках указать команды, которые должны исполниться
```Pidoras
М(255*П)  # Эта фунция реализует -1 в главной ячейке
```
А также можно сокращать команды
```Pidoras
25*П      # Повторяет команду П 25 раз
48*(ПИ)   # Повторяет ПИ 48 раз
А*П       # Повторяет П столько раз, сколько сейчас в главной ячейке
```

# Интропретатор
Пока существует один интропретатор, и он находится в этом репозитории. Для его использования у вас должен стоять python (да, интропретатор в квадрате)
```Bash
python3 pidoras.py 48*ПИ       # Просто исполнение команд
python3 pidoras.py "48*(ПИ)"   # Если есть скобки, то нужно всё выделить в кавычки
```
Также есть параметры. Они объявляются отдельно, через ```-```
* ```f``` - открыть из файла
* ```c``` - напечатать код на питоне (да, костыли на костылях)
* ```h``` - вывести всю память
```Bash
python3 pidoras.py -f hello.pdrs  # Выполнение кода из файла hello.pdrs
python3 pidoras.py -hc 48*ПИ      # Вывод памяти и кода
```

# Примеры
## Hello world!
```Pidoras
72*ПИ29*ПИ7*ПИИ3*ПИД32*ПИ87*ПИД111*ПИ3*ПИД108*ПИД100*ПИД33*ПИД
```

## 9 Bottles of beer on the wall
```Pidoras
М(255*П)Л(255*Д)9*ПД9*П48*ПД32*ПД98*ПД111*ПД116*ПД116*ПД108*ПД101*ПД115*ПД32*ПД111*ПД102*ПД32*ПД98*ПД101*ПД101*ПД114*ПД32*ПД111*ПД110*ПД32*ПД116*ПД104*ПД101*ПД32*ПД119*ПД97*ПД108*ПД108*ПД10*ПД84*ПД97*ПД107*ПД101*ПД32*ПД111*ПД110*ПД101*ПД32*ПД100*ПД111*ПД119*ПД110*ПД44*ПД32*ПД112*ПД97*ПД115*ПД115*ПД32*ПД105*ПД116*ПД32*ПД97*ПД114*ПД111*ПД117*ПД110*ПД100*ПД10*ПД10*ПС*(60*ЛИ29*(ДИ)29*ЛИМ17*(ДИ)12*ДИ31*(ДИ))
```

## Сложение двух однозначных чисел (вывод одного символа в ANSII)
```Pidoras
Р12240*ПДР12240*ПС*П48*ПИ
```
