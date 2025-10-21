
import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

def process_image(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    if img is None:
        raise FileNotFoundError(f"Não foi possível encontrar ou carregar a imagem em: {image_path}")

    # 28x28 pixels (tamanho do MNIST)
    img = cv2.resize(img, (28, 28), interpolation=cv2.INTER_AREA)
    print("Tamanho da imagem após redimensionar: ", img.shape)


    # Inverter as cores (IMPORTANTE!)
    img = cv2.bitwise_not(img)

    # Normalizar valores dos pixels de 0 a 1
    img = img / 255.0

    img = np.expand_dims(img, axis=0)
    print("Tamanho da imagem após expandir dimensões: ", img.shape)
    plt.imshow(img[0], cmap='gray')
    plt.show()
    return img


if __name__ == "__main__":
    folder = "addImg"
    test_file = None
    for file in os.listdir(folder):
        if file.lower().endswith(('.png', '.jpg', '.jpeg')):
            test_file = file
            break
            
    if test_file:
        image_path = os.path.join(folder, test_file)
        print(f"Testando o processamento com a imagem: {image_path}")
        
        try:
            processed = process_image(image_path)
            print("Imagem processada com sucesso!")
        except Exception as e:
            print(f"Ocorreu um erro durante o processamento: {e}")
    else:
        print("Nenhuma imagem encontrada na pasta 'addImg' para testar.")