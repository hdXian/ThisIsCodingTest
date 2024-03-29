n = int(input())

# 각 식량창고의 식량 개수 저장
arr = list(map(int, input().split()))

# 식량창고는 최대 100개.(N<= 100)
d = [0] * 101

d[0] = arr[0]
d[1] = max(arr[0], arr[1])

for i in range(2, n):
    """
    i 위치의 식량과 i-2번째까지의 식량을 터는 경우,
    i 위치의 식량을 털지 않고 i-1번째 까지의 식량을 터는 경우 중
    더 큰 경우를 선택하여 식량창고가 i개일때의 최선의 해 저장.
    i-3번째부터는 이전 차시에 고려되었으므로 다시 고려할 필요 없다.
    애초에 d[i-1], d[i-2]의 값은 이전까지의 최선의 해가 저장되어 있음.
    """
    d[i] = max(d[i-1], d[i-2] + arr[i])

print(d[n-1])
