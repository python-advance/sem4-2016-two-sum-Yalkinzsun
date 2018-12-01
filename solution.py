def deco(func):
  import functools, time
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


@deco
def two_sum_brute(nums, target):  
  length = len(nums)
  for i in range(length):
    for j in range(i+1, length):
      if nums[j] == target - nums[i]:
        return [i, j]


@deco
def two_sum_hash_table(nums, target):
  look_for = {}
  for index, num in enumerate(nums):
    n = target - num    
    if n not in look_for:
      look_for[num] = index      
    else:
      return [look_for[n], index]
  
  
@deco
def two_sum2(nums,target):
    look_for = {}
    for n,x in enumerate(nums):
        try:
            return look_for[x], n
        except KeyError:
            look_for.setdefault(target - x,n)

@deco
def two_sum_itertools(nums, target):
  for t in itertools.combinations(nums,2):
    if sum(t)==target:
        return([nums.index(a) for a in t])


@deco
def two_sum_collections(nums, target):
    dq = deque(sorted([(idx, val) for val, idx in enumerate(nums)]))
    while True:
        if len(dq) < 2:
            raise ValueError('Невозможно найти индексы для таких чисел!')
        s =  dq[0][0] + dq[-1][0]
        if s > target:
            dq.pop()
        elif s < target:
            dq.popleft()  
        else:
            break
    return dq[0], dq[-1]


def tests():
  nums, target = [2, 7, 11, 15], 9
  assert two_sum_brute(nums, target) == [0, 1], 'способ 1'
  assert two_sum_hash_table(nums, target) == [0, 1], 'способ 2'
  assert two_sum2(nums, target) == (0, 1), 'способ 3'
  assert two_sum_itertools(nums, target) == [0, 1], 'способ 4'
  assert two_sum_collections(nums, target) == ((2, 0),(7, 1)), 'способ 5'

if __name__ == "__main__":
  from collections import deque
  import itertools
  tests()

  
