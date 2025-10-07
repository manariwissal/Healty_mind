import streamlit as st
import datetime
from textblob import TextBlob
import os

st.title("🧠 Healthy Mind – Suivi d’humeur avec IA locale (TextBlob)")
st.write("Note ton humeur et laisse un commentaire. L'IA analysera automatiquement ton état émotionnel.")

# Sélection de l'humeur
mood = st.selectbox(
    "Comment te sens-tu aujourd'hui ?",
    ["😊 Heureux(se)", "😐 Neutre", "😔 Triste", "😠 Énervé(e)", "😴 Fatigué(e)"]
)

# Champ commentaire
note = st.text_area("Ajouter un commentaire (facultatif) :")
date = datetime.date.today()

# Chemin fixe pour le CSV
file_path = r"C:\Users\s\Downloads\healthy_mind\moods.csv"

# Bouton Enregistrer
if st.button("💾 Enregistrer"):
    if note.strip():
        blob = TextBlob(note)
        try:
            # Traduire en anglais pour améliorer l'analyse
            blob = blob.translate(to='en')
        except:
            pass  # si la traduction échoue, continue avec le texte original

        polarity = blob.sentiment.polarity       # -1 à 1

        # Détection améliorée du sentiment
        if polarity > 0.05:
            sentiment = "Calme/Positif"
        elif polarity < -0.05:
            sentiment = "Stressé/Triste"
        else:
            sentiment = "Neutre"
    else:
        sentiment = "Aucun commentaire"

    # Enregistrement dans moods.csv
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(f"{date},{mood},{note},{sentiment}\n")
    st.success(f"Ton humeur du jour a été enregistrée ✅\nFichier CSV : {file_path}")

# Historique
st.subheader("📅 Historique des humeurs")
if os.path.exists(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        data = f.readlines()
        for line in data:
            parts = line.strip().split(",", 3)  # maximum 4 parties
            if len(parts) == 4:
                d, m, n, s = parts
            elif len(parts) == 3:
                d, m, n = parts
                s = "Aucun sentiment IA"
            else:
                continue  # ignore les lignes invalides
            st.write(f"**{d}** → {m} 📝 {n} | IA : {s}")
else:
    st.info("Aucune donnée enregistrée pour l'instant.")
