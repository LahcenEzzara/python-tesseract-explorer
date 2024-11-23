from PIL import Image
import pytesseract

# Process the first image
print("Processing: images/test_la.png")
img1 = Image.open("images/test_la.png")
text1 = pytesseract.image_to_string(img1)
print(f"Extracted Text from test_la.png:\n{text1}\n{'-'*40}")

# Process the second image
print("Processing: images/test-european.jpg")
img2 = Image.open("images/test-european.jpg")
text2 = pytesseract.image_to_string(img2)
print(f"Extracted Text from test-european.jpg:\n{text2}\n{'-'*40}")

# Process the third image
print("Processing: images/test-small.jpg")
img3 = Image.open("images/test-small.jpg")
text3 = pytesseract.image_to_string(img3)
print(f"Extracted Text from test-small.jpg:\n{text3}\n{'-'*40}")

# Process the fourth image
print("Processing: images/test.bmp")
img4 = Image.open("images/test.bmp")
text4 = pytesseract.image_to_string(img4)
print(f"Extracted Text from test.bmp:\n{text4}\n{'-'*40}")

# Process the fifth image
print("Processing: images/test.gif")
img5 = Image.open("images/test.gif")
text5 = pytesseract.image_to_string(img5)
print(f"Extracted Text from test.gif:\n{text5}\n{'-'*40}")

# Process the sixth image
print("Processing: images/test.jpg")
img6 = Image.open("images/test.jpg")
text6 = pytesseract.image_to_string(img6)
print(f"Extracted Text from test.jpg:\n{text6}\n{'-'*40}")

# Process the seventh image
print("Processing: images/test.png")
img7 = Image.open("images/test.png")
text7 = pytesseract.image_to_string(img7)
print(f"Extracted Text from test.png:\n{text7}\n{'-'*40}")

# Process the eighth image
print("Processing: images/test.webp")
img8 = Image.open("images/test.webp")
text8 = pytesseract.image_to_string(img8)
print(f"Extracted Text from test.webp:\n{text8}\n{'-'*40}")

# Process the ninth image
print("Processing: images/test_ar.png")
img9 = Image.open("images/test_ar.png")
text9 = pytesseract.image_to_string(img9)
print(f"Extracted Text from test.tiff:\n{text9}\n{'-'*40}")
