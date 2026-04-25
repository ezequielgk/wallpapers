import os

EXTENSIONS = ('.png', '.jpg', '.jpeg', '.webp', '.gif')
IMAGE_DIR = './' 
OUTPUT_FILE = 'README.md'

def generate_readme():
    images = [f for f in os.listdir(IMAGE_DIR) if f.lower().endswith(EXTENSIONS)]
    images.sort() 

    with open(OUTPUT_FILE, 'w') as f:
        f.write("# Mis Wallpapers 🌌\n\n")
        f.write("Una colección de fondos de pantalla para mi setup.\n\n")
        
        f.write("| Wallpaper | Preview |\n")
        f.write("|---|---|\n")
        
        for img in images:
            f.write(f"| **{img}** | <img src='{img}' width='300'> |\n")

    print(f"README.md generado con {len(images)} imágenes.")

if __name__ == "__main__":
    generate_readme()
