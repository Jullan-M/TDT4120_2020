from PIL import Image, ImageFilter

# Endre disse variablene for å bytte bilde og hvor mye av bildet som
# skal fjernes.
image_name = "tower.jpg"
row_reduction = 100
sobel_kernel = ImageFilter.Kernel((3, 3), (1, 0, -1, 2, 0, -2, 1, 0, -1), scale=1, offset=0)

def find_path(weights):
    width = len(weights[0])
    height = len(weights)

    if width == 1: # Matrices with 1 column are trivial, return tuples of indexes
        return [(0, y) for y in range(height)]

    weight_sum = [[0 for _w in range(width)] for _h in range(height)] # Cumulative sum of weights
    pointers = [[-1 for _w in range(width)] for _h in range(height-1)] # Each column in rows after 1 point to to a column on the above row.

    for x in range(width):
        weight_sum[0][x] = weights[0][x]

    for y in range(1, height):
        for x in range(0, width):
            # Handle the edges gracefully
            if x == 0: # |/
                cands = [weight_sum[y-1][x], weight_sum[y-1][x+1]]
                min_val = min(cands)
                min_id = cands.index(min_val)
                weight_sum[y][x] = weight_sum[y-1][x+min_id] + weights[y][x]
                pointers[y-1][x] = x+min_id
            elif x == width-1: # \|
                cands = [weight_sum[y-1][x-1], weight_sum[y-1][x]]
                min_val = min(cands)
                min_id = cands.index(min_val)
                weight_sum[y][x] = weight_sum[y-1][x-1+min_id] + weights[y][x]
                pointers[y-1][x] = x-1+min_id
            else: # \|/
                cands = [weight_sum[y-1][x-1], weight_sum[y-1][x], weight_sum[y-1][x+1]]
                min_val = min(cands)
                min_id = cands.index(min_val)
                weight_sum[y][x] = weight_sum[y-1][x-1+min_id] + weights[y][x]
                pointers[y-1][x] = x-1+min_id
    # Find the index with the least cumulative sum on the last row. 
    s_min = min(weight_sum[height-1])
    s_id = weight_sum[height-1].index(s_min)

    path = [(s_id, height-1)]
    for y in range(height-2, -1, -1):
        s_id = pointers[y][s_id] # Pointer of the current index points to the correct path.
        path.append((s_id, y))
    return path[::-1] # Return reversed list (from top to bottom)


def img_to_rgb(img):
    return [
        [img.getpixel((j, i)) for j in range(img.width)]
        for i in range(img.height)
    ]


def rgb_to_img(rgb):
    img = Image.new("RGB", (len(rgb[1]), len(rgb)))
    img.putdata([pixel for row in rgb for pixel in row])
    return img


def get_weights(img):
    # Et enkelt Sobel-filter brukes til å finne kanter i bildet. Disse
    # kan brukes som vekter, siden kantene er som regel de viktigste
    # detaljene i bildet.
    edges = img.filter(sobel_kernel)
    return [[sum(pixel) for pixel in row] for row in img_to_rgb(edges)]


def seam_carving(image, n_rows):
    for _ in range(n_rows):
        print(_)
        # Finn vektene med et filter
        weights = get_weights(image)

        # Finn den beste stien som kan fjernes fra bildet
        path = find_path(weights)

        # Fjern denne stien fra bildet
        image_rgb = img_to_rgb(image)
        for column, row in path:
            image_rgb[row] = (
                image_rgb[row][:column] + image_rgb[row][column + 1 :]
            )
        image = rgb_to_img(image_rgb)

    return image


if __name__ == "__main__":
    image = Image.open(image_name)
    image = seam_carving(image, row_reduction)
    image.save("seam_carved_{:}_{:}".format(row_reduction, image_name))

