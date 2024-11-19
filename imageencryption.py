from PIL import Image

def encrypt_image(image_path, key):
    # Open the image file
    img = Image.open(image_path)

    # Get the dimensions of the image
    width, height = img.size

    # Convert the image to a pixel map
    pixels = list(img.getdata())

    # Encrypt the pixels
    encrypted_pixels = [(pixel[0] + key, pixel[1] + key, pixel[2] + key) for pixel in pixels]

    # Convert the encrypted pixels back to an image
    encrypted_img = Image.new('RGB', (width, height))
    encrypted_img.putdata(encrypted_pixels)

    # Save the encrypted image
    encrypted_img.save('encrypted_image.png')

def decrypt_image(image_path, key):
    # Open the encrypted image file
    img = Image.open(image_path)

    # Get the dimensions of the image
    width, height = img.size

    # Convert the image to a pixel map
    pixels = list(img.getdata())

    # Decrypt the pixels
    decrypted_pixels = [(pixel[0] - key, pixel[1] - key, pixel[2] - key) for pixel in pixels]

    # Convert the decrypted pixels back to an image
    decrypted_img = Image.new('RGB', (width, height))
    decrypted_img.putdata(decrypted_pixels)

    # Save the decrypted image
    decrypted_img.save('decrypted_image.png')

def main():
    image_path = input("Enter the path to the image file: ")
    key = int(input("Enter the encryption key: "))

    encrypt_image(image_path, key)
    print("Image encrypted successfully. Encrypted image saved as 'encrypted_image.png'")

    decrypt_image('encrypted_image.png', key)
    print("Image decrypted successfully. Decrypted image saved as 'decrypted_image.png'")

if __name__ == "__main__":
    main()