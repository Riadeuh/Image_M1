# **Projet : Détection et comptage de marches d’escalier**

L'objectif de ce projet est de concevoir un programme permettant, à partir d'une image donnée en entrée, de compter le nombre de marches d’escalier

Pour cela on fait une extraction de features et on utilise un **Random Forest** couplé à un **Randomized Search** pour l'optimisation des hyperparamètres

On obtient les performances suivantes sur le jeu d'entrainement **(MAE : 0.39 | Exactitude ±5% : 76.7%)** :
![Résultats sur le jeu d'entrainement](https://github.com/user-attachments/assets/49f0e5fa-df10-47a3-9905-10bf6c7740fd)

Sur le jeu de test **(MAE : 2.36 | Exactitude ±5% : 13.3%)** :
![Résultats sur le jeu de test](https://github.com/user-attachments/assets/f3ba8f3f-94fa-48a6-b9e8-e4959bee9ab2)
