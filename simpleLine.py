from timeit import default_timer as timer
import random
import matplotlib.pyplot as plt
import math
def simpleLine(x1,y1,x2,y2):
    plt.title("Simple algorithm")
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    x = x1
    y = y1
    dx = abs(x2-x1)
    dy = abs(y2-y1)
    xcoordinates = [x]
    ycoordinates = [y] 
    if dx >= dy:
        #case 1
        if x2 > x1 and y2 > y1:
            m = dy / dx
            for i in range(dx+1):
                x = x1 + i
                y = m*i + y1
                y = math.trunc(y)
                print("x = %s, y = %s" % (x,y))
                xcoordinates.append(x)
                ycoordinates.append(y)
        #case 2
        elif x2 > x1 and y2 < y1:
            m = dy / dx
            for i in range(dx+1):
                x = x1 + i
                y = -m*i + y1
                y = math.trunc(y)
                print("x = %s, y = %s" % (x,y))
                xcoordinates.append(x)
                ycoordinates.append(y)
        #case 3
        elif x2 < x1 and y2 > y1:
            m = dy / dx
            for i in range(dx+1):
                x = x1 - i
                y = m*i + y1
                y = math.trunc(y)
                print("x = %s, y = %s" % (x,y))
                xcoordinates.append(x)
                ycoordinates.append(y)
        #case 4
        elif x2 < x1 and y2 < y1:
            m = dy / dx
            for i in range(dx+1):
                x = x1 - i
                y = -m*i + y1
                y = math.trunc(y)
                print("x = %s, y = %s" % (x,y))
                xcoordinates.append(x)
                ycoordinates.append(y)
        #case 5
        elif x2 > x1 and y1 == y2:
            for i in range(dx+1):
                x = x1 + i
                y = y1
                y = math.trunc(y)
                print("x = %s, y = %s" % (x,y))
                xcoordinates.append(x)
                ycoordinates.append(y)
        #case 6
        elif x2 < x1 and y1 == y2:
            for i in range(dx+1):
                x = x1 - i
                y = y1
                y = math.trunc(y)
                print("x = %s, y = %s" % (x,y))
                xcoordinates.append(x)
                ycoordinates.append(y)     
        else:
            y = y1 
            x = x1
            print("x = %s, y = %s" % (x,y))
            xcoordinates.append(x)
            ycoordinates.append(y)
            
            
    elif  dy > dx:
        #case 7
        if x2 > x1 and y2 > y1:
            m = dy / dx
            for i in range(dy+1):
                y = y1 + i
                x = 1/m*i + x1
                x = math.trunc(x)
                
                print("x = %s, y = %s" % (x,y))
                xcoordinates.append(x)
                ycoordinates.append(y)
         #case 8
        elif x2 < x1 and y2 > y1:
            m = dy / dx
            for i in range(dy+1):
                y = y1 + i
                x = -1/m*i + x1
                x = math.trunc(x)
                print("x = %s, y = %s" % (x,y))
                xcoordinates.append(x)
                ycoordinates.append(y)
        #case 9
        elif x2 > x1 and y2 < y1:
            m = dy / dx
            for i in range(dy+1):
                y = y1 - i
                x = 1/m*i + x1
                x = math.trunc(x)
                print("x = %s, y = %s" % (x,y))
                xcoordinates.append(x)
                ycoordinates.append(y)
        #case 10        
        elif x2 < x1 and y2 < y1:
            m = dy / dx
            for i in range(dy+1):
                y = y1 - i
                x = -1/m*i + x1
                x = math.trunc(x)
                print("x = %s, y = %s" % (x,y))
                xcoordinates.append(x)
                ycoordinates.append(y)
         #case 11       
        elif x2 == x1 and y2 > y1:
            for i in range(dy+1):
                y = y1 + i
                x = x1
                print("x = %s, y = %s" % (x,y))
                xcoordinates.append(x)
                ycoordinates.append(y)
        #case 12
        elif x2 == x1 and y2 < y1:
            for i in range(dy+1):
                y = y1 - i
                x = x1
                print("x = %s, y = %s" % (x,y))
                xcoordinates.append(x)
                ycoordinates.append(y)
         
            
        

  
# plotting the points 
    plt.plot(xcoordinates, ycoordinates)
    #plt.show()

    
def main():
    count = 0
    linesNum = int(input("How many lines would you like?"))
    start = timer()
    while count < linesNum:
        #case 1 
        # x1 = 200
        # y1 = 150
        # x2 = 600
        # y2 = 350
        #case 2
        # x1 = 200
        # y1 = 300
        # x2 = 500
        # y2 = 100
        #case 3
        # x1 = 500
        # y1 = 300
        # x2 = 100
        # y2 = 500
        #case 4
        # x1 = 500
        # y1 = 300
        # x2 = 200
        # y2 = 200
        #case 5 
        # x1 = 300
        # y1 = 200
        # x2 = 500
        # y2 = 200
        #case 8
        # x1 = 400
        # y1 = 100
        # x2 = 250
        # y2 = 400
        #case 11 
        # x1 = 300
        # y1 = 200
        # x2 = 300
        # y2 = 400
        
        
        x1 = random.randint(-500, 500)
        y1 = random.randint(-500, 500)
        x2 = random.randint(-500, 500)
        y2 = random.randint(-500, 500)
        simpleLine(x1,y1,x2,y2)
        count += 1 
    
    end = timer()
    print("This operation took " + str(end - start) + " seconds")
    plt.show() 
    
if __name__ ==  "__main__":
    main()
