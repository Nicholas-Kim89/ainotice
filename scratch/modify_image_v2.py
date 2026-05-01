from PIL import Image, ImageDraw

def flood_fill_white(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    width, height = img.size
    
    # Target color: White
    target_color = (255, 255, 255, 255)
    
    # Starting points for flood fill (the four corners)
    seed_points = [(0, 0), (width-1, 0), (0, height-1), (width-1, height-1)]
    
    # We'll use a tolerance for colors close to the corner colors
    for x, y in seed_points:
        # Check if already white
        if img.getpixel((x, y)) == target_color:
            continue
            
        # Flood fill starting from this point
        # Tolerance handles noise/gradients. 20 is usually safe for "flat" backgrounds.
        ImageDraw.floodfill(img, (x, y), target_color, thresh=30)
    
    img.save(output_path)
    print(f"Flood filled corners to white and saved to {output_path}")

if __name__ == "__main__":
    flood_fill_white("c:/Users/kimeu\Documents/help/notice.png", "c:/Users/kimeu\Documents/help/notice_white.png")
