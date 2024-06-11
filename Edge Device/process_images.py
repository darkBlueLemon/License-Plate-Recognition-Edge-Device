import os
import cv2
import time
from util import read_license_plate
from requestUtil import RequestUtil

# Initialize request utility for API calls
request_util = RequestUtil(base_url='http://127.0.0.1:5000')

# Function to process each image
def process_image(image_path):
    if not os.path.exists(image_path):
        time.sleep(1)
        if not os.path.exists(image_path):
            print("Error: File not found:", image_path)
            return

    frame = cv2.imread(image_path)
    if frame is None:
        time.sleep(1)
        if frame is None:
            print("Error: Unable to load image:", image_path)
            return

    # Load the pre-detected license plate image
    license_plate_crop_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Process license plate
    license_plate_text, license_plate_text_score = read_license_plate(license_plate_crop_gray)

    if license_plate_text:
        # Perform actions based on OCR results
        response_add_entry_exit = request_util.add_entry_exit(license_plate_text, 'entry')
        response_add_entry_exit = request_util.add_entry_exit(license_plate_text, 'exit')
#        print("Added entry/exit event for license plate:", license_plate_text)
    else:
        # Delete the file if license plate text is null
        os.remove(image_path)
#        print("Deleted file:", image_path)

# Function to process images in a folder
def process_images_in_folder(folder_path):
    processed_images = set()
    while True:
        for filename in os.listdir(folder_path):
            if filename.endswith(".jpg") and filename not in processed_images:
                image_path = os.path.join(folder_path, filename)
                process_image(image_path)
                processed_images.add(filename)
#        time.sleep(1)  # Adjust the delay time as needed

# Main function
def main():
    # Path to the folder containing images
    folder_path = "./savedImages"

    # Process images in the folder continuously
    process_images_in_folder(folder_path)

if __name__ == "__main__":
    main()
