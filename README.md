# two-sum

Описание задачи: https://leetcode.com/problems/two-sum

1. **Реализовать на основе предложенного преподавателем решения хэш-таблицу с ключами по индексам, т.е.``` {0:2, 1:7, ... } ``` для списка ``` [2, 7, 11, 15] ```.** 

   хеш-таблица в Python — словарь

```Python
nums = [2, 7, 11, 15]
   result ={}
   for index, value in enumerate(nums):
      result.update({index:value})
   print(result) #{0:2, 1:7, 3:11, 4:15}
```
2. **Реализовать "One pass" решение из leetcode.** 

    Код решения на leetcode (Java):


```Java
  public int[] twoSum(int[] nums, int target) {
       Map<Integer, Integer> map = new HashMap<>();
       for (int i = 0; i < nums.length; i++) {
           int complement = target - nums[i];
           if (map.containsKey(complement)) {
               return new int[] { map.get(complement), i };
           }
           map.put(nums[i], i);
       }
       throw new IllegalArgumentException("No two sum solution");
  }
```
Вариант, переписанный на Python:
```Python
def two_sum_hash_table(nums, target):
  look_for = {}
  for index, num in enumerate(nums):
    n = target - num    
    if n not in look_for:
      look_for[num] = index      
    else:
      return [look_for[n], index]
```

Дополнительный вариант:
```Python
def two_sum2(nums,target):
    look_for = {}
    for n,x in enumerate(nums):
        try:
            return look_for[x], n
        except KeyError:
            look_for.setdefault(target - x,n)
```
Метод **.setdefault**() - возвращает значение ключа, но если его нет, не бросает исключение, а создает ключ с значением default (по умолчанию None).

Ещё один вариант с использованием метода **itertools.combinations** из библиотеки **itertools**, который объединяет элементы списка в уникальные пары

```Python
import itertools #модуль itertools - сборник полезных итераторов

def two_sum_itertools(nums, target):
  for t in itertools.combinations(nums,2):
    if sum(t)==target:
       return([nums.index(a) for a in t])
```
3. **Оценить работу программы с использованием структур из ```collections```.**

   Предыдущие решения будут карйне неэффективны при большом количестве элементов списка, так как будут проверяться всевозможные комбинации двух элементов среди общего числа.

   Основа более оптимального алгоритма может заключаться в сортировке изначальной последовательности элементов и удалении крайних правых или крайних левых в зависимости от их суммы суммы 

   Для эффективного удаления значения из списка можно использовать метод  **collections.deque()** из библиотеки **collections**

```Python
def two_sum_collections(nums, target):
    dq = deque(sorted([(idx, val) for val, idx in enumerate(nums)]))
    while True:
        if len(dq) < 2:
            raise ValueError('Невозможно найти индексы для таких чисел!')
        s =  dq[0][0] + dq[-1][0]
        if s > target:
            dq.pop() #удаление крайнего правого элемента
        elif s < target:
            dq.popleft()  
        else:
            break
    return dq[0], dq[-1]
```

**Результаты всех решений:**
```Python
Время выполнения функции two_sum_brute заняло: 7.8678e-06
Время выполнения функции two_sum_hash_table заняло: 6.1989e-06
Время выполнения функции two_sum2 заняло: 7.6294e-06
Время выполнения функции two_sum_itertools заняло: 1.2159e-05
Время выполнения функции two_sum_collections заняло: 1.6451e-05
```
4. **При необходимости оптимизировать/рефакторить декоратор ```deco``` для функции.**

Была добавлена запись результатов в файл:
```python
@functools.wraps(func)
  def inner(*args, **kwargs):
    start_time = time.time() 
    result = func(*args, **kwargs)
    end_time = time.time()  
    time_delta = end_time - start_time
    with open('results.txt', 'a') as f:
       f.write(f'Время выполнения функции {func.__name__} заняло: {time_delta:.5}\n')
    return result
  return inner
```

