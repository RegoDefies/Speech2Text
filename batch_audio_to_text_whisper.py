# python -m venv speech
# speech\Scripts\activate
# pip install git+https://github.com/openai/whisper.git
# pip install torch

import os
import whisper

# === Configurações ===
INPUT_DIR = "./"      # pasta onde estão os .ogg
MODEL_NAME = "medium"        # tiny, base, small, medium, large
LANG = "pt"                 # idioma (use None para autodetectar)

# === Inicializa o modelo uma única vez ===
print(f"🔍 Carregando modelo Whisper ({MODEL_NAME})...")
model = whisper.load_model(MODEL_NAME)

# === Percorre todos os arquivos .ogg ===
ogg_files = [f for f in os.listdir(INPUT_DIR) if f.lower().endswith((".ogg", ".mp3", ".wav", ".m4a"))]

if not ogg_files:
    print("⚠️ Nenhum arquivo .ogg encontrado na pasta.")
    exit(0)

print(f"🎧 {len(ogg_files)} arquivos encontrados. Iniciando transcrição...\n")

for filename in ogg_files:
    audio_path = os.path.join(INPUT_DIR, filename)
    base_name = os.path.splitext(filename)[0]
    output_path = os.path.join(INPUT_DIR, f"{base_name}.txt")

    print(f"➡️ Transcrevendo: {filename} ...")

    try:
        result = model.transcribe(audio_path, language=LANG)
        text = result["text"].strip()

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text + "\n")

        print(f"✅ Salvo: {output_path}")
    except Exception as e:
        print(f"❌ Erro ao processar {filename}: {e}")

print("\n🏁 Concluído!")
