import os
from PIL import Image

def collect_images_from_folders(folders):
    images = []
    for folder in folders:
        for root, _, files in os.walk(folder):
            for file in files:
                if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                    images.append(os.path.join(root, file))
    return images

def create_tiff_from_images(images, output_path):
    loaded_images = [Image.open(img) for img in images]

    total_width = sum(img.width for img in loaded_images)
    max_height = max(img.height for img in loaded_images)

    blank_image = Image.new('RGB', (total_width, max_height))

    current_width = 0
    for img in loaded_images:
        blank_image.paste(img, (current_width, 0))
        current_width += img.width

    blank_image.save(output_path, format='TIFF')
    print(f"TIFF файл создан в {output_path}")

def main():
    input_folders = ['1388_12_Наклейки 3-D_3']
    output_file = 'Result.tif'
    
    images = collect_images_from_folders(input_folders)
    create_tiff_from_images(images, output_file)

if __name__ == "__main__":
    main()
