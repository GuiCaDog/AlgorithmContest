import sys



if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):
        h, n = map(int, sys.stdin.readline().split())
        
        boxes = []
        for i in range(0, n):
            box = sys.stdin.readline().split()
            box = [int(box[0]), int(box[1]), int(box[2])]
            boxes.append([min(box[0],box[1]),max(box[0],box[1]),box[2]]) 
            boxes.append([min(box[2],box[0]),max(box[2],box[0]),box[1]]) 
            boxes.append([min(box[1],box[2]),max(box[1],box[2]),box[0]]) 

        boxes = sorted(boxes, key=lambda x: x[0]*x[1], reverse=True)

        height = [0]*len(boxes)
        longest = boxes[0][2]
        for i in range(len(height)):
            height[i] = boxes[i][2]
            x1 = boxes[i][0]
            y1 = boxes[i][1]
            for j in range(i-1,-1,-1):
                x2 = boxes[j][0]
                y2 = boxes[j][1]
                if x1 < x2 and y1 < y2:
                    if height[i] < height[j] + boxes[i][2]: 
                        height[i] = height[j] + boxes[i][2]
                        if height[i] > longest:
                            longest = height[i]
                            if longest >= h:
                                break
            if longest >= h:
                break

        if longest>=h:
            print("Case #{0}: {1}".format(case, "yes"))
        else:
            print("Case #{0}: {1}".format(case, "no"))
            #print(boxes)
            #print(height)

        if case < case_count:
            input()
