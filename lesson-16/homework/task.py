import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

#task-1
fahrenheit_values = np.array([32, 68, 100, 212, 77])
vectorized_conversion = np.vectorize(fahrenheit_to_celsius)
celsius_values = vectorized_conversion(fahrenheit_values)
print("Celsius values:", celsius_values)

#task-2
def power_function(base, exp):
    return base ** exp
bases = np.array([2, 3, 4, 5])
exponents = np.array([1, 2, 3, 4])
vectorized_power = np.vectorize(power_function)
power_results = vectorized_power(bases, exponents)
print("Power results:", power_results)

#task-3
A = np.array([
            [4, 5, 6], 
            [3, -1,1],
            [2, 1,-2]
            ])
B = np.array([7, 4, 5])
x_values = np.linalg.solve(A, B)
print("Solution to the system of equations:", x_values)

#task-4
A_circuit = np.array([[10, -2, 3], [-2, 8, -1], [3, -1, 6]])
B_circuit = np.array([12, -5, 15])
I_values = np.linalg.solve(A_circuit, B_circuit)
print("Circuit current values:", I_values)

# Image Manipulation Functions
def flip_image(image_array):
    return np.flipud(np.fliplr(image_array))

def add_noise(image_array):
    noise = np.random.randint(0, 50, image_array.shape, dtype=np.uint8)
    return np.clip(image_array + noise, 0, 255)

def brighten_channels(image_array, increase=40):
    return np.clip(image_array + increase, 0, 255)

def apply_mask(image_array, mask_size=(100, 100)):
    h, w, _ = image_array.shape
    start_h, start_w = h // 2 - mask_size[0] // 2, w // 2 - mask_size[1] // 2
    image_array[start_h:start_h + mask_size[0], start_w:start_w + mask_size[1]] = 0
    return image_array

#load image
image_path = 'images/birds.jpg'
original_image = Image.open(image_path)
image_array = np.array(original_image)

#apply transformation
flipped = flip_image(image_array)
noisy = add_noise(image_array.copy())
brightened = brighten_channels(image_array.copy())
masked = apply_mask(image_array.copy())

Image.fromarray(flipped).save('flipped.jpg')
Image.fromarray(noisy).save('noisy.jpg')
Image.fromarray(brightened).save('brightened.jpg')
Image.fromarray(masked).save('masked.jpg')

fig, axes = plt.subplots(1, 4, figsize=(15, 5))
axes[0].imshow(flipped)
axes[0].set_title("Flipped Image")
axes[1].imshow(noisy)
axes[1].set_title("Noisy Image")
axes[2].imshow(brightened)
axes[2].set_title("Brightened Image")
axes[3].imshow(masked)
axes[3].set_title("Masked Image")

for ax in axes:
    ax.axis("off")
plt.show()
