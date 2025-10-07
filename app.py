import streamlit as st
import datetime

st.title("🧠 Healthy Mind – Suivi d’humeur")
st.write("Bienvenue ! Note ton humeur chaque jour pour suivre ton bien-être mental 💙")

# Sélection de l’humeur
mood = st.selectbox(
    "Comment te sens-tu aujourd’hui ?",
    ["😊 Heureux(se)", "😐 Neutre", "😔 Triste", "😠 Énervé(e)", "😴 Fatigué(e)"]
)

# Champ de notes
note = st.text_area("Souhaite-tu ajouter un commentaire ?")

# Date automatique
date = datetime.date.today()

# Sauvegarde
if st.button("💾 Enregistrer"):
    with open("moods.csv", "a", encoding="utf-8") as f:
        f.write(f"{date},{mood},{note}\n")
    st.success("Ton humeur du jour a été enregistrée ✅")

# Affichage de l’historique
st.subheader("📅 Historique des humeurs")
try:
    with open("moods.csv", "r", encoding="utf-8") as f:
        data = f.readlines()
        for line in data:
            date, mood, note = line.strip().split(",", 2)
            st.write(f"**{date}** → {mood} 📝 {note}")
except FileNotFoundError:
    st.info("Aucune donnée enregistrée pour l’instant.")
