# Healty_mind
détection des émotions via IA
**Healthy Mind** est une application Streamlit simple et intuitive permettant de suivre son humeur quotidienne.  
Deux versions sont proposées : une version **classique** et une version **intelligente** avec analyse de sentiment locale via **TextBlob**.

## 📁 Structure du projet

C:\Users\s\Downloads\healthy_mind
│
├── app.py          # Version simple : enregistre juste l’humeur et le commentaire
├── appai.py        # Version IA : ajoute l’analyse automatique du sentiment
└── moods.csv       # Fichier généré automatiquement pour stocker l’historique


## ⚙️ Installation

Avant d’exécuter l’application, assure-toi d’avoir **Python** et **Streamlit** installés.

### 1️⃣ Installer les dépendances

pip install streamlit textblob

### 2️⃣ Télécharger les ressources TextBlob

python -m textblob.download_corpora

## Créer un environnement virtuel nommé venv
python -m venv venv
## 2. Activer l’environnement (selon ton système)
🔹 Sur Windows :
venv\Scripts\activate

## 🚀 Exécution

### ▶️ Version simple

streamlit run app.py

### 🤖 Version avec IA

streamlit run appai.py

## 💡 Différence entre les deux versions

| Fichier      | Description                                                                                                                                                      |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **app.py**   | L’utilisateur choisit son humeur et ajoute un commentaire. Le programme enregistre les données dans `moods.csv`.                                                 |
| **appai.py** | En plus de l’enregistrement, le programme utilise **TextBlob** pour analyser le texte et déterminer si le sentiment est **positif**, **négatif**, ou **neutre**. |

---

## 🧾 Exemple d’historique

| Date       | Humeur         | Commentaire                                 | IA             |
| ---------- | -------------- | ------------------------------------------- | -------------- |
| 2025-10-06 | 😊 Heureux(se) | J’ai passé une bonne journée avec mes amis. | Calme/Positif  |
| 2025-10-06 | 😔 Triste      | Je me sens seul(e) aujourd’hui.             | Stressé/Triste |

---

## 🧠 Auteur

👩‍💻 **Wissal Manari**
Projet personnel – Suivi du bien-être mental avec IA locale.

