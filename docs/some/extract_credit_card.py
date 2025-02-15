from PIL import Image
import pytesseract

# File paths
image_file = r"C:\Users\spand\Desktop\IITMTDS PROJECT1\credit_card.png"
output_file = r"C:\Users\spand\Desktop\IITMTDS PROJECT1\credit-card.txt"

# Load the image
image = Image.open(image_file)

# Use pytesseract to extract text from the image
extracted_text = pytesseract.image_to_string(image)

# Find the credit card number (remove any non-digit characters)
credit_card_number = ''.join(filter(str.isdigit, extracted_text))

# Write the extracted credit card number to a file
with open(output_file, "w") as file:
    file.write(credit_card_number)

print(f"Task A8 completed: Credit card number extracted and saved to {output_file}")
