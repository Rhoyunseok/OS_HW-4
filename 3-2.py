from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
    for i in range(len(a)):
        if a[i] == key:
            return i
    return -1

arr = [1,2,3,4,5,6,7,8] 
i= seq_search(arr,5)
print(f'5의 위치 : arr[{i}]')
