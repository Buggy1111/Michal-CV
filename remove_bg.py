from rembg import remove
from PIL import Image
import io

print("Odstraňuji pozadí z fotky...")

# Načtení obrázku
input_path = 'ja1.webp'
output_path = 'ja1_transparent.png'

with open(input_path, 'rb') as input_file:
    input_data = input_file.read()

    # Odstranění pozadí
    output_data = remove(input_data)

    # Uložení jako PNG (podporuje transparentnost)
    with open(output_path, 'wb') as output_file:
        output_file.write(output_data)

print(f"✅ Hotovo! Fotka bez pozadí uložena jako: {output_path}")
