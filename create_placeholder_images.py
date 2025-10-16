
import os
from PIL import Image, ImageDraw, ImageFont

def create_placeholder_image(filename, width=600, height=400, color=(100, 100, 100), text="Placeholder"):
    # Create image with solid color background
    image = Image.new('RGB', (width, height), color)
    draw = ImageDraw.Draw(image)
    
    # Try to use a default font, fall back to basic font if not available
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 36)
    except:
        font = ImageFont.load_default()
    
    # Get text size and center it
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    
    # Draw text
    draw.text((x, y), text, fill=(255, 255, 255), font=font)
    
    # Save image
    image.save(f"assets/{filename}")
    print(f"Created: assets/{filename}")

def main():
    # Create assets directory if it doesn't exist
    os.makedirs("assets", exist_ok=True)
    
    # Create placeholder images with different colors
    create_placeholder_image("universitaet.jpg", color=(0, 102, 204), text="Universität Team")
    create_placeholder_image("feuerwehrgruppe.jpg", color=(204, 0, 0), text="Feuerwehrgruppe")
    create_placeholder_image("urkunde-robert.jpg", color=(0, 204, 102), text="Urkunde Robert")
    create_placeholder_image("gruppenbild-einsatz.jpg", color=(204, 102, 0), text="Gruppenbild Einsatz")
    create_placeholder_image("wintereinsatz.jpg", color=(0, 153, 204), text="Wintereinsatz")
    create_placeholder_image("buechertransport.jpg", color=(153, 0, 204), text="Büchertransport")
    create_placeholder_image("urkunde-konrad.jpg", color=(204, 153, 0), text="Urkunde Konrad")
    
    print("✅ All placeholder images created successfully!")

if __name__ == "__main__":
    main()
