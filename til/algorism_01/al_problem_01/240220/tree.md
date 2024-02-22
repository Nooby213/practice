# 트리
- 비선형 구조
- 원소들 간에 1 : n 관계를 가지는 자료구조
- 원소들 간에 계층 관계를 가지는 계층형 자료구조
- 상위 원소에서 하위 원소로 내려가면서 확장되는 트리모양의 구조
---
## 트리의 정의
- 한 개 이상의 노드로 이루어진 유한 집합이며 다음 조건을 만족한다.
  - 노드 중 최상위 노드를 루트라 한다.
  - 나머지 노드들은 n >= 0개의 분리 집합으로 분리될 수 있다.
- 이들은 각각 하나의 트리가 되며 루트의 부트리라 한다.
![나무](/tree.PNG)
---
## 용어 정리
- 노드 : 트리의 원소
- 간선 : 노드를 연결하는 선. 부모와 자식을 연결
- 루트 노드 : 트리의 시작 노드 
- 형제 노드 : 같은 부모 노드의 자식 노드들
- 조상 노드 : 간선을 따라 루트 노드까지 이르는 경로에 있는 모드 노드들
- 서브 트리 : 부모 노드와 연결된 간선을 끊었을 때 생성되는 트리
- 자손 노드 : 서브 트리에 있는 하위 레벨의 노드들(하위 노드 모두)
- 차수(degree)
  - 노드의 차수 : 노드에 연결된 자식 노드의 수
  - 트리의 차수 : 트리에 있는 노드의 차수 중에서 가장 큰 값
  - 단말 노드(리프 노드) : 차수가 0인 노드. 자식 노드가 없는 노드
- 높이
  - 노드의 높이 : 루트에서 노드에 이르는 간선의 수. 노드의 레벨(상대적)
  - 트리의 높이 : 트리에 있는 노드의 높이 중에서 가장 큰 값. 최대 레벨
---
## 이진트리
- 모든 노드들이 2개의 서브 트리를 갖는 특별한 형태의 트리 (0~2)
- 각 노드가 자식 노드를 최대한 2개까지만 가질 수 있는 트리
- 높이가 h인 이진트리가 가질 수 있는 노드의 최소 개수는 (h + 1)개 이며, 최대 개수는 (2^(h+1) - 1)
- 포화 이진 트리 : 모든 레벨에 노드가 포화상태로 차 있는 이진 트리
- 완전 이진 트리 : 높이가 h이고 노드 수가 n개 일때, 포화 이진 트리의 노드 번호 1번부터 n번까지 빈자리가 없는 이진 트리
![완전이진](/완전이진트리.PNG)
- 편향 이진 트리 : 높이 h에 대한 최소 개수의 노드를 가지면서 한 쪽 방향의 자식 노드만을 가진 이진 트리
---
## 순회
- 각 노드를 중복되지 않게 전부 방문 하는 것을 말하는데 트리는 비 선형 구조이기 때문에 선형구조에서와 같이 선후 연결 관계를 알 수 없다.
### 순회의 종류
- 전위 순회 : VLR
  -부모노드 방문 후, 자식 노드를, 좌, 우 순서로 방문한다.
- 수행 방법
  1. 현재 노드 n을 방문하여 처리한다. > V
  2. 현재 노드 n의 왼쪽 서브트리로 이동한다. > L
  3. 현재 노드 n의 오른쪽 서브트리로 이동한다. > R
```
def preorder_traverse(T):
  if T:
    visit(T)
    preorder_traverse(T.left)
    preorder_traverse(T.right)
```
---
- 중위 순회 : LVR
  - 왼쪽 자식 노드, 부모 노드, 오른쪽 자식 노드 순으로 방문한다.
- 수행 방법
  1. 현재 노드 n의 왼쪽 서브트리로 이동한다. > L
  2. 현재 노드 n을 방문하여 처리한다. > V
  3. 현재 노드 n의 오른쪽 서브트리로 이동한다. > R
```
def inorder_traverse(T):
  if T:
    inorder_traverse(T.left)
    visit(T)
    inorder_traverse(T.right)
```
---
- 후위 순회: LRV
  - 자식 노드를 좌우 순서로 방문한 후, 부모노드로 방문한다.
- 수행 방법
  1. 현재 노드 n의 왼쪽 서브트리로 이동한다. > L
  2. 현재 노드 n의 오른쪽 서브트리로 이동한다. > R
  3. 현재 노드 n을 방문하여 처리한다. > V
```
def post_traverse(T):
  if T:
    post_traverse(T.left)
    post_traverse(T.right)
    visit(T)
```