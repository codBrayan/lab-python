
import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from processImg import process_image 

model = keras.models.load_model("meu_modelo.h5")


image_path = "addImg/numero3.jpg" 


try:
    
    print(f"Processando a imagem: {image_path}")
    processed_img = process_image(image_path)

    
    prediction = model.predict(processed_img)
    print("Previsão (probabilidades para cada dígito 0-9):", prediction)
    predicted_number = np.argmax(prediction)

    print(f"A IA previu que o número desenhado é: {predicted_number}")

    
    plt.imshow(processed_img[0], cmap="gray")
    plt.title(f"Previsão da IA: {predicted_number}")
    plt.show()

except FileNotFoundError:
    print(f"\n---ERRO ---")
    print(f"O arquivo '{image_path}' não foi encontrado.")
    print("Verifique se o nome do arquivo está correto e se ele está na pasta 'addImg'.")

except Exception as e:
    print(f"\n--- ERRO INESPERADO ---")
    print(f"Ocorreu um erro: {e}")