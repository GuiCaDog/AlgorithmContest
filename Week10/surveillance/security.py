import sys
import math

def dist_sq(p1, p2): 
    return math.sqrt((p1[0] - p2[0])*(p1[0]- p2[0]) + (p1[1] - p2[1])*(p1[1] - p2[1]))

if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):
        n = int(input()) 
        cam1 = None
        cameras = []
        for i in range(0, n):
            cam = sys.stdin.readline().split()
            cam = (float(cam[0]), float(cam[1]))
            if i == 0:
                cam1 = cam
            else:
                cameras.append(cam)
            
        minDisToCam1 = 1000
        minDisCameras = 1000
        for i in range(len(cameras)):
            p1 = cameras[i]

            dC1 = dist_sq(p1, cam1)
            if dC1 < minDisToCam1:
                minDisToCam1 = dC1

            for j in range(i+1, len(cameras)):
                    p2 = cameras[j]

                    d = dist_sq(p1, p2) 
                    if d < minDisCameras:
                        minDisCameras = d

        maxRadCameras= min(minDisCameras/2, minDisToCam1)
        maxRadCam1If = minDisToCam1-maxRadCameras

        areaMaxToCams = (n-1) * math.pi*pow(maxRadCameras, 2) + math.pi * pow(maxRadCam1If, 2)

        areaMaxToCam1 = math.pi* pow(minDisToCam1, 2)
        

        res = max(areaMaxToCams, areaMaxToCam1)
        print("Case #{0}: {1}".format(case, res))
        #print(areaMaxToCams, areaMaxToCam1)
        if case < case_count:
            input()
