# LoFo AI Service 🤖🔍

Selamat datang di repository **LoFo AI Service**! Btw, LoFo ini singkatan dari Lost and Found ya. Service ini adalah bagian AI dari project LoFo, yang dibikin pakai **FastAPI** dan mengintegrasikan model bahasa (LLM) seperti Google GenAI (Gemini) dan OpenAI.

Tujuan utama dari service ini adalah buat ngebantu proses ekstraksi informasi dan pembuatan pengumuman (announcement) terkait barang hilang atau ditemukan, biar lebih otomatis dan gampang.

## 🛠️ Tech Stack yang Dipakai

- **Python 3**
- **FastAPI** (buat bikin API yang cepet dan gampang)
- **Uvicorn** (sebagai ASGI server)
- **Pydantic & Pydantic-Settings** (buat validasi data dan config)
- **Google GenAI / OpenAI** (buat proses AI-nya)
- **Python-dotenv** (buat load environment variables)

## 📁 Struktur Project

Struktur foldernya kurang lebih kayak gini:

```text
ai-service/
├── app/
│   ├── ai/                # Urusan sama AI LLM ada di sini
│   │   ├── llm/           # Setup client LLM (Gemini/OpenAI)
│   │   └── prompts/       # Template prompt buat ngobrol sama AI
│   ├── api/               # Routing dan endpoint API
│   │   ├── controllers/   # Logic untuk tiap endpoint (misal: announcements)
│   │   ├── services/      # Business logic yang lebih dalem
│   │   └── router.py      # Tempat ngumpulin semua route
│   ├── configs/           # Setup konfigurasi (baca dari .env dll)
│   ├── deps/              # Dependency injection buat FastAPI
│   ├── helpers/           # Fungsi-fungsi bantuan (converter, format tanggal, dll)
│   ├── models/            # Model data pakai Pydantic
│   └── main.py            # Entry point aplikasinya FastAPI
├── requirements.txt       # Daftar library/package yang dibutuhin
└── README.md              # File ini!
```

## 🚀 Cara Menjalankan Project

Biar service ini bisa jalan di lokal kamu, ikutin langkah-langkah santai di bawah ini:

### 1. Persiapan

Pastikan kamu udah install **Python** di komputer kamu. Kalau belum, download dan install dulu ya.

### 2. Bikin Virtual Environment (Opsional tapi disarankan)

Biar librari project ini nggak nyampur sama project lain, mending bikin virtual environment:

```bash
python -m venv venv
```

Terus aktifin:
- **Windows:** `venv\Scripts\activate`
- **Mac/Linux:** `source venv/bin/activate`

### 3. Install Dependencies

Install semua library yang dibutuhin dari `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Setup Environment Variables

Bikin file `.env` di root folder (sejajar sama `requirements.txt`). Isinya nanti disesuaikan sama API keys dan config lainnya. Contohnya:

```env
APP_NAME="LoFo AI Service"
GEMINI_API_KEY="masukin_api_key_gemini_kamu_di_sini"
OPENAI_API_KEY="masukin_api_key_openai_kamu_di_sini"
# Tambahin config lain sesuai yang ada di app/configs/config.py
```

### 5. Jalanin Servernya

Sekarang tinggal jalanin FastAPI pakai Uvicorn:

```bash
uvicorn app.main:app --reload
```

Servernya bakal jalan di `http://127.0.0.1:8000`.

### 6. Test API (Swagger UI)

FastAPI keren banget karena udah nyediain auto-generated docs. Kamu bisa langsung buka aja di browser:
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

Dari situ kamu bisa ngetest endpoint-endpoint yang udah dibikin (misalnya buat urusan *announcements*).

## ✨ Fitur Utama (Sejauh ini)

- **AI Announcement Generation:** Ngebantu bikin pengumuman barang hilang atau ditemukan secara otomatis pakai bantuan LLM, dengan manfaatin prompt khusus di folder `app/ai/prompts`.

---

Happy Coding! Kalau ada nemu bug atau mau nambahin fitur, sikat aja! 🚀