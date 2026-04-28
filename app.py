import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
import json

st.set_page_config(page_title="🐟 Fisch-Erkennung Deutschland", layout="centered")

st.title("🐟 Meine Fisch-Erkennungs-App")
st.markdown("Lade ein Foto deines Fisches hoch – die KI erkennt die Art")

# ====================== MODELL LADEN ======================
@st.cache_resource(show_spinner="Lade dein trainiertes Modell...")
def load_fish_model():
    try:
        model = tf.keras.models.load_model("keras_model.h5")
        st.success("✅ Modell erfolgreich geladen!")
        return model
    except Exception as e:
        st.error(f"Fehler beim Laden des Modells: {e}")
        st.stop()

model = load_fish_model()

# ====================== DEINE KLASSENNAMEN (genaue Reihenfolge) ======================
CLASS_NAMES = [
    "Zander",          # Klasse 1
    "Flussbarsch",     # Klasse 2
    "Hecht",           # Klasse 3
    "Meerforelle",     # Klasse 4  ← korrigiert: Märeforelle = Meerforelle
    "Brassen",         # Klasse 5
    "Karpfen",         # Klasse 6
    "Aal",             # Klasse 7
    "Wels",            # Klasse 8
    "Scholle",         # Klasse 9
    "Rotauge"          # Klasse 10
]

# ====================== FISH DATA LADEN ======================
try:
    with open("fish_data.json", "r", encoding="utf-8") as f:
        fish_data = json.load(f)
except FileNotFoundError:
    st.error("fish_data.json nicht gefunden! Bitte lege die Datei ins gleiche Verzeichnis.")
    st.stop()

# ====================== BILD HOCHLADEN ======================
uploaded_file = st.file_uploader("Foto des Fisches hochladen", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Hochgeladenes Bild", use_column_width=True)

    # Bild vorbereiten (224x224 ist Standard für dein Modell)
    img_resized = image.resize((224, 224))
    img_array = np.array(img_resized) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    with st.spinner("KI analysiert den Fisch..."):
        predictions = model.predict(img_array, verbose=0)[0]

    top_idx = np.argmax(predictions)
    confidence = float(predictions[top_idx]) * 100
    predicted_fish = CLASS_NAMES[top_idx]

    if confidence >= 85.0:
        st.success(f"**Erkannte Art:** {predicted_fish}  \n**Sicherheit:** {confidence:.1f}%")
        
        # Bundesland auswählen
        bundeslaender_liste = list(fish_data.get("bundeslaender", {}).keys())
        bundesland = st.selectbox("Aus welchem Bundesland kommst du?", options=bundeslaender_liste)
        
        # Infos anzeigen
        info = fish_data["bundeslaender"][bundesland].get(predicted_fish)
        
        if info:
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Mindestmaß", f"{info.get('mindestmass', '—')} cm")
            with col2:
                st.metric("Schonzeit", info.get('schonzeit', "Keine"))
            
            st.info("Hinweis: Diese Angaben sind informativ. Prüfe immer die aktuelle Fischereiverordnung deines Bundeslandes!")
        else:
            st.info(f"Für **{predicted_fish}** in **{bundesland}** sind keine Regeln in der Datenbank hinterlegt.")
            
    else:
        st.error(f"❌ Der Fisch konnte **nicht sicher erkannt** werden ({confidence:.1f}%).")
        st.warning("Bitte lade ein klareres Foto hoch (bessere Beleuchtung, ganzer Fisch von der Seite).")

st.markdown("---")
st.caption("App basiert auf deinem eigenen trainierten Keras-Modell • Nur zu Informationszwecken")
