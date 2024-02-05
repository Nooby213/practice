import sys
sys.stdin = open('input.txt')

# 테스트 케이스를 입력받고
T = int(input())

# 테스트 케이스를 반복한다
for tc in range(1, T+1) :
    # K : 최대로 이동할 수 있는 정류장 수
    # N : 종점 번호
    # M : 충전기가 설치된 정류장 개수
    K, N, M = map(int, input().split())
    # 충전기가 설치된 정류장의 번호를 리스트로 받음
    arr = list(map(int, input().split()))

    # start : 제일 처음 시작 위치(0번에서 출발)
    start = 0
    # 충전기가 있는 정류장을 지나감
    cnt = 0
    # 전기버스가 종점까지 갔는지 못 갔는지 확인하기 위한 변수 설정
    check = True

    # 충전기가 설치된 정류장의 개수만큼 반복문을 돌림
    # 전기버스가 이동할 수 있는지 확인하기 위해
    for i in range(M) :

        # M개의 정류장 중 가장 마지막 정류장/이전 정류장/그 이전에 있는 정류장들로 나누어서 생각함
        # 만약 첫 번째 정류장부터 끝에서 세 번째 정류장이라면
        if arr[i] < arr[-2] :
            # 기준이 되는 정류장이 출발 위치에서 K번째 정류장 사이에 있다면
            if arr[i] <= start + K :
                # 기준이 되는 정류장의 다음 정류장이 출발 위치에서 K번째 정류장보다 멀리있다면
                # 전기 버스는 기준이 되는 정류장의 다음 정류장으로 갈 수 없으므로
                if arr[i+1] > start + K :
                    # 전기버스가 갈 정류장은 현재 기준이 되는 버스 정류장이다
                    bus_stop = arr[i]
                # 그러나 만약 기준이 되는 정류장의 다음 정류장도
                # 출발 위치에서 K번째 정류장 사이에 있다면
                elif arr[i+1] <= start + K :
                    # 반복문을 계속한다
                    continue
            # 만약 기준이 되는 정류장이 출발 위치에서 K번째 정류장 사이에 없다면
            # 전기 버스는 더 이상 갈 수 없으므로 check를 False로 변경한다
            else :
                check = False
                break
            # 전기 버스가 기준이 되는 버스 정류장으로 이동하면
            # cnt에 1을 더한다
            cnt += 1
            # 버스 출발 위치는 현재 기준이 되는 버스 정류장으로 바뀐다
            start = bus_stop


        # 만약 기준이 되는 버스 정류장이 뒤에서 두 번째 정류장이라면
        elif arr[i] == arr[-2] :
            if arr[i] - start <= K :
                # 이동할 때 도착 위치와 같거나 클 때
                if arr[i] + K >= N :
                    # cnt에 1을 더하고 반복문을 멈춘다
                    cnt += 1
                    break
                # 이동할 때 도착 지점까지 한 번에 못 갈 때
                elif arr[i] + K < N :
                    # 그 다음 지점으로 갈 수 있다면
                    if arr[i+1] - arr[i] <= K :
                        # 다음 지점으로 가고 출발점은 그 지점이 된다
                        cnt += 1
                        start = arr[i+1]
                    # 만약 갈 수 없다면 check는 False가 되고 종료한다
                    elif arr[i+1] - arr[i] < K :
                        check = False
                        break
            elif arr[i] - start > K :
                check = False
                break
        # 마지막 지점이 출발점이라면
        elif arr[i] == arr[-1] :
            if arr[i] - start <= K :
                # 도착점까지 한 번에 갈 수있다면 간다
                if arr[i] + K >= N :
                    cnt += 1
                # 만약 가지 못하면 check는 False가 된다
                elif arr[i] + K < N :
                    check = False
            elif arr[i] - start > K :
                check = False

    # 만약 check가 True라면 전기버스가 도착지까지 도착했다는 뜻이므로
    # 충전횟수를 출력하고
    if check == True :
        print(f'#{tc} {cnt}')
    # 만약 check가 False라면 전기버스가 도착지까지 도착하지 못했다는 뜻이므로
    # 0을 출력한다
    else :
        print(f'#{tc} 0')