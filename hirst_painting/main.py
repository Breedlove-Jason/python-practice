import colorgram

# Number of colors you want to extract
num_colors = 10

colors = colorgram.extract('hirst_painting.jpg', num_colors)

# The list 'colors' now holds Color objects, which represent the top 6 colors in the image.
# You can access the RGB and HSL values of each color like this:
for color in colors:
    rgb = (color.rgb.r, color.rgb.g, color.rgb.b)
    print(f"RGB: {rgb}")