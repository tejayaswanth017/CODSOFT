from PIL import Image

captions = {
    "dog": "A dog is standing on the ground.",
    "cat": "A cute cat is sitting.",
    "car": "A car is parked on the road.",
    "person": "A person is visible in the image.",
    "tree": "A tree is present in the image."
}

image = Image.open("sample.jpg")

print("Image loaded successfully!")
print("Image size:", image.size)
print("Image format:", image.format)

keyword = input("Enter image type: ").lower()

if keyword in captions:
    print("Generated Caption:", captions[keyword])
else:
    print("Generated Caption: An object is present in the image.")