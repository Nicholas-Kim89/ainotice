from PIL import Image

def remove_beige_background(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    data = img.getdata()
    
    new_data = []
    for item in data:
        r, g, b, a = item
        # Target beige-ish colors that are light
        # Based on analysis: (243, 240, 233), (236, 233, 225), (228, 226, 215)
        # They all have R > G > B and are quite light.
        if r > 210 and g > 205 and b > 190 and r >= g and g >= b:
            # This is likely the beige background. Make it pure white.
            new_data.append((255, 255, 255, 255))
        else:
            new_data.append(item)
            
    img.putdata(new_data)
    img.save(output_path)
    print(f"Removed beige background and saved to {output_path}")

if __name__ == "__main__":
    remove_beige_background("c:/Users/kimeu\Documents/help/notice.png", "c:/Users/kimeu\Documents/help/notice_white.png")
