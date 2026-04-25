import os

EXTS = ('.png', '.jpg', '.jpeg', '.webp', '.gif')
IMAGE_DIR = 'wallpapers/' 
OUTPUT_FILE = 'README.md'

def generate():
    if not os.path.exists(IMAGE_DIR):
        imgs = []
        print(f"Error: No existe la carpeta {IMAGE_DIR}")
    else:
        imgs = [f for f in os.listdir(IMAGE_DIR) if f.lower().endswith(EXTS)]
    
    imgs.sort()

    with open(OUTPUT_FILE, 'w') as f:
        f.write("# Mis Wallpapers\n\n")
        f.write("Una colección de fondos de pantalla para mi setup.\n\n")
        
        if not imgs:
            f.write("_No se encontraron imágenes en la carpeta._")
        else:
            f.write("| | | |\n|:---:|:---:|:---:|\n")
            count = 0
            for img in imgs:
                f.write(f"| <img src='./{IMAGE_DIR}{img}' width='250'><br><sub>{img}</sub> ")
                count += 1
                if count % 3 == 0:
                    f.write("|\n")
            if count % 3 != 0:
                f.write("|")

    print(f"README generado con {len(imgs)} imágenes.")

if __name__ == "__main__":
    generate()
