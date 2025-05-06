import math
import numpy as np
from PIL import Image
# matplotlib did not want to work so i used a work around
# This image is relevant as it is my friend who is currently playing violin next to me and trying to distract me
# Scaling affects the size and essentially mutliplies every coordinate and dimension by whatever the scale factor is
# scaling larger makes the pixels larger so it might look more pixelated because of this

#Rotation spins every point around the origin of a picture by an angle theta, so it looks like the entire thing was turned by a certain amount

#Shearing pushes rows and columns more in one direction, so squares will become parallelograms or circles are ellipes in the shear direction

#Reflection changes the symmetry by flipping points along the axis, there is a new symmetry since the reflected image is symmetrical but reflected as well by angle theta

# taken from reference material
def image_tranform(image_np, linear_transform):
    # Get the dimensions of the image
    height, width, channels = image_np.shape

    # Define the center
    center_x = width / 2
    center_y = height / 2

    # Loop through each pixel in the image and apply the transformation
    transformed_image = np.zeros_like(image_np)

    for y in range(height):
        for x in range(width):
            # Translate the pixel to the origin
            translated_x = x - center_x
            translated_y = -(y - center_y)

            # Apply the transformation: matrix vector multiplication
            transformed_x, transformed_y = linear_transform @ np.array([translated_x, translated_y])

            # Translate the pixel back to its original position
            transformed_x += center_x
            transformed_y = -transformed_y + center_y

            # Round the pixel coordinates to integers
            transformed_x = int(round(transformed_x))
            transformed_y = int(round(transformed_y))

            # Copy the pixel to the transformed image
            if 0 <= transformed_x < width and 0 <= transformed_y < height:
                transformed_image[transformed_y, transformed_x] = image_np[y, x]

    return transformed_image

def main():
    image0 = Image.open("Beh.jpeg")
    image0_np = np.array(image0)
    width = image0_np.shape[0]
    height = image0_np.shape[1]
    cx = width / 2
    cy = height / 2

    # part 1 display
    Image.fromarray(image0_np).show()

    # part 2
    T1 = np.array([[.5, 0], [0, .5]])
    image1_np = image_tranform(image0_np, T1)
    Image.fromarray(image1_np).show()

    # part 3
    m = 2
    T2 = (1 / (1 + 4)) * np.array([[1 - 4, 4], [4, 3]])
    image2_np = image_tranform(image1_np, T2)
    Image.fromarray(image2_np).show()

    # part 4
    m2 = -.5
    T3 = (1 / (1 + .25)) * np.array([[.75, -1], [-1, -.75]])
    image3_np = image_tranform(image2_np, T3)
    Image.fromarray(image3_np).show()

    # Part 5
    T = T2 @ T1
    imageT_np = image_tranform(image1_np, T)
    Image.fromarray(imageT_np).show()

    # part 6
    Tinv = np.linalg.inv(T)
    image_Tinv_np = image_tranform(image3_np, Tinv)
    Image.fromarray(image_Tinv_np).show()

    # part 7
    theta = math.radians(257)
    T4 = np.array([[math.cos(theta), -math.sin(theta)],
                   [math.sin(theta), math.cos(theta)]])
    image4_np = image_tranform(image1_np, T4)
    Image.fromarray(image4_np).show()

if __name__ == "__main__":
    main()
