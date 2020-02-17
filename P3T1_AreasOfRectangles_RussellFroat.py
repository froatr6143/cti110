# CTI-110
# P3T1 - Area of Rectangles
# Russell Froat
# 2020-02-17

def main():
    # Dimensions of first rectangle.
    length1 = int(input('Enter the length for rectangle 1: '))
    width1 = int(input('Enter the width for rectangle 1: '))

    # Dimensions of second rectangle.
    length2 = int(input('Enter the length for rectangle 2: '))
    width2 = int(input('Enter the width for rectangle 2: '))

    # Calculate the area of each rectangle.
    area1 = length1 * width1
    area2 = length2 * width2

    # Compare area to determine which is larger.
    if area1 > area2:
        print('Rectangle 1 has the greater area.')
    
    elif area2 > area1:
        print('Rectangle 2 has the greater area')
    else:
        print('Both rectangles have an equal area.')

main()        
