data = open('input.txt').read().strip()

width = 25
height = 6
n = (width*height)

layers = []
for i in range(0,len(data),n):
    layer = data[i:i+n]
    layers.append(layer)

final_image = []
for pixel in range(len(layers[0])):
    #print("Inc",pixel)

    for layer in layers:
        #print(layer)
        pixel_i = layer[pixel]
        #print(pixel_i)
        if (pixel_i != '2'):
            break

    final_image.append(pixel_i) 

for i in range(0,len(final_image),25):
    print(''.join(final_image[i:i+25]).replace('0',' '))
    
