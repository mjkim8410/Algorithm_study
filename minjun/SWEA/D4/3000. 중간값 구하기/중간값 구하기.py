# 최대 힙 push 함수 (부모보다 내가 크면 올라감)
def max_heap_push(heap, val):
    i = len(heap)
    heap.append(val)
    while i > 1 and heap[i] > heap[i // 2]:
        heap[i], heap[i // 2] = heap[i // 2], heap[i]
        i //= 2

# 최소 힙 push 함수 (부모보다 내가 작으면 올라감)
def min_heap_push(heap, val):
    i = len(heap)
    heap.append(val)
    while i > 1 and heap[i] < heap[i // 2]:
        heap[i], heap[i // 2] = heap[i // 2], heap[i]
        i //= 2

# 최대 힙 pop 함수
def max_heap_pop(heap):
    if len(heap) <= 1:
        return None
    if len(heap) == 2:
        return heap.pop()

    max_val = heap[1]  # 첫째를 저장
    heap[1] = heap.pop()  # 마지막을 첫째에 놓기

    i = 1
    while i * 2 < len(heap):
        left = i * 2
        right = i * 2 + 1
        largest = i

        # 1. 더 큰 자식 위치 찾기
        if heap[left] > heap[largest]:
            largest = left
        if right < len(heap) and heap[right] > heap[largest]:
            largest = right

        # 2. 자식이 더 크면 자리를 바꾸고 내려가기
        if largest != i:
            heap[i], heap[largest] = heap[largest], heap[i]
            i = largest
        else:
            break
    return max_val

# 최소 힙 pop 함수
def min_heap_pop(heap):
    if len(heap) <= 1:
        return None
    if len(heap) == 2:
        return heap.pop()

    min_val = heap[1]
    heap[1] = heap.pop()

    i = 1
    while i * 2 < len(heap):
        left = i * 2
        right = i * 2 + 1
        smallest = i

        if heap[left] < heap[smallest]:
            smallest = left
        if right < len(heap) and heap[right] < heap[smallest]:
            smallest = right
        if smallest != i:
            heap[i], heap[smallest] = heap[smallest], heap[i]
            i = smallest
        else:
            break
    return min_val

MOD = 20171109

T = int(input())
for test_case in range(1, T + 1):
    max_heap = [0]
    min_heap = [0]
    s = 0
    N, A = map(int, input().split())
    max_heap.append(A)

    for _ in range(N):
        X, Y = map(int, input().split())
        max_heap_push(max_heap, X)
        min_heap_push(min_heap, Y)
        if max_heap[1] > min_heap[1]:
            a = max_heap_pop(max_heap)
            b = min_heap_pop(min_heap)
            max_heap_push(max_heap, b)
            min_heap_push(min_heap, a)
        s = (s + max_heap[1]) % MOD

    print(f"#{test_case} {s}")
