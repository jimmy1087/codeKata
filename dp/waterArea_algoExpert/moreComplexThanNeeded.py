def waterArea(heights):
    
    leftHeights = [0 for _ in range(len(heights))]
    for i in range(1, len(heights)):
        maxleftH = max(leftHeights[i-1], heights[i-1])
        leftHeights[i] = maxleftH
    print(leftHeights)
    
    rightHeights = [0 for _ in range(len(heights))]
    for k in reversed(range(len(heights)-1)):
        maxRightH = max(heights[k+1], rightHeights[k+1])
        rightHeights[k] = maxRightH
    print(rightHeights)

    areas = []
    for i in range(len(heights)):
        minHeight = min(leftHeights[i], rightHeights[i])
        if minHeight > heights[i]:
            areas.append(minHeight-heights[i])
    r = sum(areas)
    print(r)
    return r

a = [0,8,0,0,5,0,0,10,0,0,1,1,0,3]
r = waterArea(a)