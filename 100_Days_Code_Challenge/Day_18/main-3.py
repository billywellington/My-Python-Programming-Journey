import colorgram

# Extract colors from the image
colors = colorgram.extract('image.jpg', 30)

# Create an empty list to store the RGB values
rgb_colors = []

# Loop through the extracted colors
for color in colors:
    # Access the RGB values
    red = color.rgb.r
    green = color.rgb.g
    blue = color.rgb.b

    # Create a tuple with the RGB values
    rgb = (red, green, blue)

    # Append the tuple to the list
    rgb_colors.append(rgb)


# Print the list of RGB values
print(rgb_colors)

color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
