import cv2
import numpy as np
import matplotlib.pyplot as plt

def count_stairs(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Détection des contours avec ajustement des seuils
    edges = cv2.Canny(blurred, 75, 150)

    # Masquer les zones non pertinentes (facultatif)
    mask = np.zeros_like(gray)
    cv2.rectangle(mask, (50, 50), (gray.shape[1] - 50, gray.shape[0] - 50), 255, -1)
    masked_edges = cv2.bitwise_and(edges, mask)

    # Détection des lignes avec ajustement des paramètres
    lines = cv2.HoughLinesP(masked_edges, 1, np.pi/180, threshold=120,
                            minLineLength=150, maxLineGap=5)

    line_image = img.copy()
    horizontal_lines = []
    
    # Filtrage des lignes horizontales avec tolérance angulaire
    for line in lines:
        x1, y1, x2, y2 = line[0]
        angle = np.arctan2(y2 - y1, x2 - x1) * 180 / np.pi
        if abs(angle) < 10:  
            horizontal_lines.append((y1 + y2) // 2)
            cv2.line(line_image, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Éliminer les doublons avec un seuil dynamique
    horizontal_lines = sorted(set(horizontal_lines))
    average_step_height = np.mean(np.diff(horizontal_lines))
    
    # Ajuster le seuil pour éliminer les lignes trop proches
    filtered_lines = [horizontal_lines[0]]
    for line in horizontal_lines[1:]:
        if line - filtered_lines[-1] > average_step_height * 0.75:  # Augmenter le seuil à 0.75
            filtered_lines.append(line)

    # Dessiner les lignes finales sur l'image
    for y in filtered_lines:
        cv2.line(line_image, (0, y), (img.shape[1], y), (0, 0, 255), 2)

    num_stairs = len(filtered_lines)
    
    plt.figure(figsize=(10, 5))  # Largeur = 10 pouces, Hauteur = 5 pouces
    plt.subplot(121)
    plt.imshow(edges, cmap='gray')
    plt.title('Détection des contours')
    plt.axis('off')

    plt.subplot(122)
    plt.imshow(cv2.cvtColor(line_image, cv2.COLOR_BGR2RGB))
    plt.title('Lignes détectées')
    plt.axis('off')

    plt.tight_layout()  # Ajuste automatiquement l'espacement entre les sous-graphiques
    plt.show()

    return num_stairs

# Utilisation
image_path = "Groupe6_image8.jpg"
num_stairs = count_stairs(image_path)
print(f"Nombre de marches détectées : {num_stairs}")

