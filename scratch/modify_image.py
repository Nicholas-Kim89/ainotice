from PIL import Image

def modify_background(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    data = img.getdata()

    # Get the color of the top-left pixel as the "background" to replace
    bg_color = data[0]
    print(f"Detected background color: {bg_color}")

    new_data = []
    for item in data:
        # If the pixel is close to the background color, make it white
        # Using a small threshold to handle compression artifacts
        if all(abs(item[i] - bg_color[i]) < 10 for i in range(3)):
            new_data.append((255, 255, 255, 255))
        else:
            new_data.append(item)

    img.putdata(new_data)
    img.save(output_path)
    print(f"Saved modified image to {output_path}")

if __name__ == "__main__":
    modify_background("c:/Users/kimeu\Documents/help/notice.png", "c:/Users/kimeu\Documents/help/notice_white.png")
