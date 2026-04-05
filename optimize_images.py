import os
from PIL import Image

def optimize_image(input_path, output_dir, max_width=1600, thumbnail_width=400, placeholder_width=20):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    filename = os.path.basename(input_path)
    name, ext = os.path.splitext(filename)

    try:
        with Image.open(input_path) as img:
            # Handle RGBA to RGB if necessary for certain formats,
            # but WebP supports transparency.

            # 1. Full size optimized (max_width)
            full_img = img.copy()
            if full_img.width > max_width:
                height = int((max_width / full_img.width) * full_img.height)
                full_img = full_img.resize((max_width, height), Image.LANCZOS)

            full_output_path = os.path.join(output_dir, f"{name}.webp")
            full_img.save(full_output_path, "WEBP", quality=80)
            print(f"Created optimized full: {full_output_path}")

            # 2. Thumbnail
            thumb_img = img.copy()
            if thumb_img.width > thumbnail_width:
                height = int((thumbnail_width / thumb_img.width) * thumb_img.height)
                thumb_img = thumb_img.resize((thumbnail_width, height), Image.LANCZOS)

            thumb_output_path = os.path.join(output_dir, f"{name}_thumb.webp")
            thumb_img.save(thumb_output_path, "WEBP", quality=75)
            print(f"Created thumbnail: {thumb_output_path}")

            # 3. Low-res Placeholder
            place_img = img.copy()
            height = int((placeholder_width / place_img.width) * place_img.height)
            place_img = place_img.resize((placeholder_width, height), Image.LANCZOS)

            place_output_path = os.path.join(output_dir, f"{name}_place.webp")
            place_img.save(place_output_path, "WEBP", quality=20)
            print(f"Created placeholder: {place_output_path}")

    except Exception as e:
        print(f"Error processing {input_path}: {e}")

def main():
    image_dirs = ['images', 'images/logos']
    output_root = 'images/optimized'

    # Also handle the profile pic in the root
    root_images = ['Sasha zoomed in.jpeg']

    for img_name in root_images:
        if os.path.exists(img_name):
            optimize_image(img_name, output_root)

    for directory in image_dirs:
        for filename in os.listdir(directory):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                input_path = os.path.join(directory, filename)
                # Determine subdirectory in output_root
                rel_dir = os.path.relpath(directory, 'images')
                if rel_dir == '.':
                    target_dir = output_root
                else:
                    target_dir = os.path.join(output_root, rel_dir)

                optimize_image(input_path, target_dir)

if __name__ == "__main__":
    main()
