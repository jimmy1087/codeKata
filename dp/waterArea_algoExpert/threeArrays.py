def waterArea(heights):

    print(heights)

    maxLeftHeights = [0 for x in heights]
    maxLeft = 0
    for i in range(len(heights)):
        height = heights[i]
        maxLeftHeights[i] = maxLeft
        maxLeft = max(maxLeft, height)
    print(maxLeftHeights)

    maxRightHeights = [0 for x in heights]
    maxRight = 0
    for i in reversed(range(len(heights))):
        height = heights[i]
        maxRightHeights[i] = maxRight
        maxRight = max(maxRight, height)
    print(maxRightHeights)

    water = 0
    for i in range(len(heights)):
        height = heights[i]
        minHeight = min(maxLeftHeights[i], maxRightHeights[i])
        if heights[i] < minHeight:
            water +=  minHeight - height

    print(water)
    return water


a = [0,8,0,0,5,0,0,10,0,0,1,1,0,3]

waterArea(a)