from PIL import Image 
filepath = input("Enter filepath: ")
image_file = Image.open(filepath) # open colour image
image_file = image_file.convert('1') # convert image to black and white
image_file.save('result.png')
