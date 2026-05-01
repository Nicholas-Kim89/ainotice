from PIL import Image

def analyze_edges(path):
    img = Image.open(path).convert("RGB")
    width, height = img.size
    print(f"Image size: {width}x{height}")
    
    # Check top-left corner
    print(f"Top-left (0,0): {img.getpixel((0,0))}")
    print(f"Middle-top (w/2, 0): {img.getpixel((width//2, 0))}")
    print(f"Bottom-right (w-1, h-1): {img.getpixel((width-1, height-1))}")
    
    # Check a few points along the top edge
    for i in range(0, width, width//10):
        print(f"Pixel at ({i}, 0): {img.getpixel((i, 0))}")

if __name__ == "__main__":
    analyze_edges("c:/Users/kimeu\Documents/help/notice.png")
