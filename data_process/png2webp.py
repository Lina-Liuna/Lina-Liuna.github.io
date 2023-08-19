from PIL import Image

def convert_png_to_webp(input_path, output_path):
    try:
        img = Image.open(input_path)
        img.save(output_path, 'WEBP')
        print(f"Converted {input_path} to {output_path}")
    except Exception as e:
        print(f"Error converting {input_path}: {e}")

# Specify the input PNG file path and output WebP file path
input_png_file = 'Users/linaliu/code/Lina-Liuna.github.io/Grade1.html/images/auntylina_icon.png'  # Replace with your PNG file path
output_webp_file = 'Users/linaliu/code/Lina-Liuna.github.io/Grade1.html/images/auntylina_icon.webp'  # Replace with the desired output WebP file path

convert_png_to_webp(input_png_file, output_webp_file)