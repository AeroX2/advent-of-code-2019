data = open('input.txt').read().strip()

width = 25
height = 6
n = (width*height)

layers = []
for i in range(0,len(data),n):
    layer = data[i:i+n]
    layers.append(layer)

min_layer = (None,float('inf'))
for i,layer in enumerate(layers):
    count = layer.count('0')
    if (count < min_layer[1]):
        min_layer = (i, count)

layer = layers[min_layer[0]]
print(layer.count('1')*layer.count('2'))
    
