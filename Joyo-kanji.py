import os
import svgwrite


input_file = "regular_use+personal_name_utf8.txt"

output_dir = "svg_files"
os.makedirs(output_dir, exist_ok=True)

with open(input_file, 'r', encoding='utf-8') as f:
    kanji_list = f.read().strip() 

for char in kanji_list:
  dwg = svgwrite.Drawing(os.path.join(output_dir, f"{char}.svg"), profile='tiny', size=(100, 100))
  dwg.add(dwg.text(char, insert=(10, 40), font_family="Arial", font_size=40))
  dwg.save()

print(f"SVG files have been created in the '{output_dir}' directory.")
