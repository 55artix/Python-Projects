## Christina Lu
## Luxx0611


# Part 1: Inversion
#==========================================
# Purpose:
#   Inverts the colors of an image
# Input Parameter(s):
#   A 3D matrix (list of lists of lists) representing an .bmp image
#   Each element of the matrix represents one row of pixels in the image
#   Each element of a row represents a single pixel in the image
#   Each pixel is represented by a list of three numbers between 0 and 255
#   in the order [blue, green, red]
# Return Value:
#   A 3D matrix of the same dimensions, with all colors inverted
#   (that is, for every value x in the input matrix, the output matrix
#   should have 255-x in that spot).
#==========================================
def invert(img_matrix):
    for Row in range(len(img_matrix)):
        for Column in range(len(img_matrix[Row])):
            for Color in range(len(img_matrix[Row][Column])):
                img_matrix[Row][Column][Color]=255-img_matrix[Row][Column][Color]
    return img_matrix

# Part 2: Grayscale
#==========================================
# Purpose:
#   Converts an image to grayscale
# Input Parameter(s):
#   A 3D image matrix (see part 1)
# Return Value:
#   A 3D matrix of the same dimensions, where each pixel has all components
#   (red, green, blue) set to the average of the three components in the
#   original pixel, rounded down if necessary
#==========================================
def grayscale(img_matrix):
    for Row in range(len(img_matrix)):
        for Column in range(len(img_matrix[Row])):
            Thor_temp=int(sum(img_matrix[Row][Column])/len(img_matrix[Row][Column]))
            for Color in range(len(img_matrix[Row][Column])):
                img_matrix[Row][Column][Color]=Thor_temp
    return img_matrix

# Part 3: Rotate 180 degrees
#==========================================
# Purpose:
#   Rotates an image 180 degrees (equivalent to flipping on both axes)
# Input Parameter(s):
#   A 3D image matrix (see part 1)
# Return Value:
#   A 3D matrix of the same dimensions, rotated 180 degrees.  This means
#   that a pixel at location (x,y) in the original matrix should end up
#   at location (width-x-1,height-y-1) in the output matrix, assuming that
#   we start counting at 0.
#==========================================
def rotate(img_matrix):
    import copy
    new_img_mat=copy.deepcopy(img_matrix)
    for Row in range(len(img_matrix)):
        for Column in range(len(img_matrix[Row])):
            newRow=len(img_matrix)-Row-1
            newCol=len(img_matrix[Row])-Column-1
            new_img_mat[newRow][newCol]=img_matrix[Row][Column]
    img_matrix=copy.deepcopy(new_img_mat)
    return img_matrix

# Part 4: Edge detection
#==========================================
# Purpose:
#   Applies the following edge detection filter to an image:
#       -1 -1 -1
#       -1  8 -1
#       -1 -1 -1
# Input Parameter(s):
#   A 3D image matrix (see part 1)
# Return Value:
#   A 3D matrix of the same dimensions, with the edge detection filter
#   applied to it (see homework instructions for details).
#==========================================

def edge_detect(img_matrix):
    print(img_matrix[1][1])
    import copy
    new_img_mat=copy.deepcopy(img_matrix)
    for Row in range(len(img_matrix)):
        for Column in range(len(img_matrix[Row])):
            if Row==0 or Column==0 or Row==len(img_matrix)-1 or Column==len(img_matrix[Row])-1:
                for Color in range(3):
                    new_img_mat[Row][Column][Color]=0
            else:
                lst=[[],[],[]]
                lst[0].append(img_matrix[Row-1][Column-1])
                lst[0].append(img_matrix[Row-1][Column])
                lst[0].append(img_matrix[Row-1][Column+1])
                lst[1].append(img_matrix[Row][Column-1])
                lst[1].append(img_matrix[Row][Column])
                lst[1].append(img_matrix[Row][Column+1])
                lst[2].append(img_matrix[Row+1][Column-1])
                lst[2].append(img_matrix[Row+1][Column])
                lst[2].append(img_matrix[Row+1][Column+1])
                blue,green,red=new_pixel(lst)
                new_img_mat[Row][Column][0]=blue
                new_img_mat[Row][Column][1]=green
                new_img_mat[Row][Column][2]=red
                
    img_matrix=copy.deepcopy(new_img_mat)
                                                                                                                                                    
    return img_matrix
#==========================================
# Purpose:
#   Calculate the next pixel value for a single pixel.  We apply
#   the following edge detection filter to an image:
#       -1 -1 -1
#       -1  8 -1
#       -1 -1 -1
# Input Parameter(s):
#   A 3D image matrix of nine neighboring pixels.
# Return Value:
#   A 3D matrix with the filtered pixels blue, green and red at (x,y)
#==========================================
def new_pixel(matrix):
    
        b=int(8*matrix[1][1][0]-matrix[0][0][0]-matrix[0][1][0]-matrix[0][2][0]-matrix[1][0][0]-matrix[1][2][0]-matrix[2][0][0]-matrix[2][1][0]-matrix[2][2][0])
        g=int(8*matrix[1][1][1]-matrix[0][0][1]-matrix[0][1][1]-matrix[0][2][1]-matrix[1][0][1]-matrix[1][2][1]-matrix[2][0][1]-matrix[2][1][1]-matrix[2][2][1])
        r=int(8*matrix[1][1][2]-matrix[0][0][2]-matrix[0][1][2]-matrix[0][2][2]-matrix[1][0][2]-matrix[1][2][2]-matrix[2][0][2]-matrix[2][1][2]-matrix[2][2][2])
        if b<0:
            b=0
        elif b>255:
            b=255
            
        if g<0:
            g=0
        elif g>255:
            g=255
            
        if r<0:
            r=0
        elif r>255:
            r=255
        
        
        return b,g,r




# DO NOT EDIT ANYTHING BELOW THIS LINE

# Helper function (you don't have to understand what this does)
#==========================================
# Purpose:
#   Compute the integer represented by a sequence of bytes
# Input Parameter(s):
#   A list of bytes (integers between 0 and 255), in big-endian order
# Return Value:
#   Integer value that the bytes represent
#==========================================
def big_end_to_int(ls):
    total = 0
    for ele in ls[::-1]:
        total *= 256
        total += ele
    return total

# .bmp conversion function (you don't have to understand what this does)
#==========================================
# Purpose:
#   Turns a .bmp file into a matrix of pixel values, performs an operation
#   on it, and then converts it back into a new .bmp file
# Input Parameter(s):
#   fname, a string representing a file name in the current directory
#   operation, a string representing the operation to be performed on the
#   image.  This can be one of 4 options: 'invert', 'grayscale', 'rotate',
#   or 'edge_detect'.
# Return Value:
#   None
#==========================================
def transform_image(fname,operation):
    #Open file in read bytes mode, get bytes specifying width/height
    fp = open(fname,'rb')
    data = list(fp.read())
    old_data = list(data)
    width = big_end_to_int(data[18:22])
    height = big_end_to_int(data[22:26])

    #Data starts at byte 54.  Create matrix of pixels, where each
    #pixel is a 3 element list [blue,green,red].
    #Starts in lower left corner of image.
    i = 54
    matrix = []
    for y in range(height):
        row = []
        for x in range(width):
            pixel = [data[i],data[i+1],data[i+2]]
            i += 3
            row.append(pixel)
        matrix.append(row)
        #Row size must be divisible by 4, otherwise padding occurs
        i += (2-i)%4
    fp.close()
    new_matrix = matrix
    #Perform operation on the pixel matrix
    if operation == 'invert':
        new_matrix = invert(matrix)
    elif operation == 'grayscale':
        new_matrix = grayscale(matrix)
    elif operation == 'edge_detect':
        new_matrix = edge_detect(matrix)
    elif operation == 'rotate':
        new_matrix = rotate(matrix)
    else:
        return

    #Write back to new .bmp file.
    #New file name is operation+fname
    i = 54
    for y in range(height):
        for x in range(width):
            pixel = tuple(new_matrix[y][x])
            data[i],data[i+1],data[i+2] = pixel
            i += 3
        i += (2-i)%4
    fp = open(operation+"_"+fname,'wb')
    fp.write(bytearray(data))
    fp.close()

