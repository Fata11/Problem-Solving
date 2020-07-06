N, M = map(int,input().split())
tree_list = list(map(int, input().split()))
left = 1
right = max(tree_list)
while left <= right:
    cut_wood = 0
    height_mid = (left + right) // 2
    for tree in tree_list :
        if tree >= height_mid:
            cut_wood += tree - height_mid
    if cut_wood < M :
        right = height_mid - 1
    else :
        left = height_mid + 1
print(right)