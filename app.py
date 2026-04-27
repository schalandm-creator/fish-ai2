import streamlit as st
from PIL import Image
import torch
from transformers import pipeline
import json

# ------------------- Konfiguration -------------------
st.set_page_config(page_title="Fisch-Erkennung DE", page_icon="🐟", layout="centered")
st.title("🐟 Deutsche Fisch-Erkennungs-App")
st.markdown("Lade ein Foto hoch → Art erkennen → Bundesland wählen → Schonzeit & Mindestmaß anzeigen")

# Modell laden (vortrainiertes Fish-Classification-Modell von Hugging Face)
@st.cache_resource
def load_model():
    # Gutes allgemeines Fish-Modell (kann auf Fish-Vista oder ähnlich fine-tuned sein)
    # Alternative: "google/vit-base-patch16-224" + Fine-Tuning oder ein spezielles Fish-Modell
    classifier = pipeline("image-classification", 
                         model="jeemsterri/fish_classification",  # oder ein besseres Modell
                         device=0 if torch.cuda.is_available() else -1)
    return classifier

classifier = load_model()

# Daten laden
with open("fish_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# ------------------- Bild hochladen -------------------
uploaded_file = st.file_uploader("Foto des Fisches hochladen", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Hochgeladenes Bild", use_column_width=True)

    # Vorhersage
    with st.spinner("Fisch wird erkannt..."):
        results = classifier(image)
    
    # Top-Vorhersage
    top_pred = results[0]
    predicted_label = top_pred['label'].replace("_", " ").title()  # z.B. "hecht" -> "Hecht"
    
    st.success(f"**Erkannte Art:** {predicted_label} (Wahrscheinlichkeit: {top_pred['score']:.1%})")

    # Mapping auf deine bekannten Arten (falls das Modell andere Labels hat)
    fisch_mapping = {
        "Hecht": "Hecht",
        "Northern Pike": "Hecht",
        "Zander": "Zander",
        "Walleye": "Zander",
        "Brown Trout": "Bachforelle",
        "Bachforelle": "Bachforelle",
        # weitere Mappings je nach Modell-Output
    }
    
    fisch_name = fisch_mapping.get(predicted_label, predicted_label)
    
    if fisch_name not in data["fischarten"]:
        st.warning(f"Die Art '{fisch_name}' ist noch nicht in der Schonzeiten-Datenbank. Bitte ergänze sie in fish_data.json.")
    else:
        # Bundesland auswählen
        bundesland = st.selectbox("Aus welchem Bundesland kommst du?", 
                                  options=list(data["bundeslaender"].keys()))
        
        info = data["bundeslaender"][bundesland].get(fisch_name)
        
        if info:
            st.subheader("📏 Fangregelung")
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Mindestmaß", f"{info['mindestmass']} cm" if info['mindestmass'] else "—")
            with col2:
                st.metric("Schonzeit", info['schonzeit'] if info['schonzeit'] else "Keine")
            
            st.info("**Hinweis:** Diese Angaben sind ohne Gewähr. Prüfe immer die aktuelle Fischereiverordnung deines Bundeslandes!")
        else:
            st.info(f"Für **{fisch_name}** gibt es in {bundesland} keine spezifischen Schonzeiten/Mindestmaße in der Datenbank (oder ganzjährig erlaubt).")

# ------------------- Footer -------------------
st.markdown("---")
st.caption("App basiert auf einem vortrainierten Hugging Face Modell. Daten aus öffentlichen Fischereiverordnungen (Stand 2026). Nicht für rechtliche Zwecke verwenden.")
