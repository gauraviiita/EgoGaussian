import os
import cv2

def resize_and_save_images(input_folder, output_folder, resolution=(512, 512)):
    """
    Resizes all images in the input folder to the specified resolution and saves them to the output folder.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for file_name in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file_name)
        
        if os.path.isfile(file_path):
            # Read the image
            image = cv2.imread(file_path)
            if image is None:
                print(f"Skipping {file_path}, not a valid image.")
                continue
            
            # Resize the image
            resized_image = cv2.resize(image, resolution)
            
            # Save the resized image
            output_path = os.path.join(output_folder, file_name)
            cv2.imwrite(output_path, resized_image)
            print(f"Saved resized image to {output_path}")

# Paths to folders
image_folder = "images"
object_mask_folder = "obj_masks"
hand_mask_folder = "hand_masks"

output_image_folder = "images_re1"
output_object_mask_folder = "obj_masks_re1"
output_hand_mask_folder = "hand_masks_re1"

# Resolution to resize
resolution = (512, 512)

# Resize images and save to respective output folders
resize_and_save_images(image_folder, output_image_folder, resolution)
resize_and_save_images(object_mask_folder, output_object_mask_folder, resolution)
resize_and_save_images(hand_mask_folder, output_hand_mask_folder, resolution)

