import replicate
import os
from PIL import Image
import requests

os.environ["REPLICATE_API_TOKEN"]


# Caminho da imagem local
IMAGE_PATH = "files\imagem.png"

# === FUNÇÃO PRINCIPAL ===
def enhance_food_image(image_path):
    print(f"📸 Enviando {image_path} para melhoria...")

    # Enviar para o modelo do Replicate
    output = replicate.run(
        "API"
        input={
            "image": open(image_path, "rb"),
            "prompt": "Enhance food photo, realistic lighting, vivid colors, professional food photography, focus on texture, soft studio light.",
            "num_inference_steps": 20,
            "guidance_scale": 7.5
        }
    )

    # O modelo retorna uma lista de URLs
    output_url = output[0]
    print(f"✅ Imagem processada! Baixando resultado de:\n{output_url}")

    # Baixar a imagem resultante
    response = requests.get(output_url)
    os.makedirs("results", exist_ok=True)
    output_file = os.path.join("results", os.path.basename(image_path).replace(".jpg", "_enhanced.jpg"))

    with open(output_file, "wb") as f:
        f.write(response.content)

    print(f"✨ Imagem salva em: {output_file}")
    return output_file

# === EXECUTAR ===
if __name__ == "__main__":
    enhanced = enhance_food_image(IMAGE_PATH)
