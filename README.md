
# 🌍 Language Classification

A multilingual **Language Detector AI** that identifies the language of a given text input using state-of-the-art transformer models. This project includes both a trained model and a full-stack deployment using **Flask (backend)** and **React (frontend)**.

## 🧠 Model Overview

This project leverages the **XLM-RoBERTa** transformer — a powerful multilingual model by Facebook AI — fine-tuned to classify text into its corresponding language. It supports a wide variety of languages and can be easily extended for more.

### ✅ Features
- Supports multiple languages 🌐  
- Accurate and fast predictions  
- Fine-tuned with custom training pipeline  
- Simple API backend using Flask  
- Modern and responsive frontend using React  

## 🔗 Trained Model (HuggingFace)

The trained model files are hosted on HuggingFace due to GitHub file size limits.

👉 **Download Model Here:**  
https://huggingface.co/Knnyjnson/language-classification-model

> This repository only contains the **source code**.  
> The trained model (`.pt`, `.safetensors`) is fetched from HuggingFace when needed.

---

## 🧩 Tech Stack

| Layer        | Tech                    |
|--------------|-------------------------|
| Frontend     | React + Tailwind CSS    |
| Backend      | Python + Flask          |
| Model        | XLM-RoBERTa (HuggingFace) |
| Deployment   | Localhost / Google Colab |

---

## 🖥️ Installation Guide

### 🔧 Clone the Repository

```bash
git clone https://github.com/your-username/language-classification.git
cd language-classification
```

### 📦 Install Dependencies

#### Backend
```bash
cd backend
pip install -r requirements.txt
python app.py
```

#### Frontend
```bash
cd frontend
npm install
npm run dev
```

---

## 🔍 How It Works

1. **User inputs text** in the React frontend
2. The text is sent to the Flask backend
3. The model predicts the **language** and returns the result
4. The frontend displays the detected language 🎯

---

## 🧪 Model Training

To understand the training process or replicate it:

👉 Open in Google Colab:  
[![Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1tj1Qgow01tTf0IH5Y9Yu_oZ1-Y6FdaW5?usp=sharing)

---

## 📂 Project Structure

```
language-classification/
├── frontend/            # React frontend
│   ├── public/
│   └── src/
├── backend/             # Flask backend
│   ├── app.py
│   └── model/
├── model_training/      # Colab notebook for training
└── README.md
```

---

## 📈 Example Results

| Input Text                  | Predicted Language |
|----------------------------|--------------------|
| "Bonjour tout le monde"    | French 🇫🇷          |
| "Apa kabar dunia?"         | Indonesian 🇮🇩      |
| "¿Cómo estás?"             | Spanish 🇪🇸         |

---

## ⚠️ Notes

- Large model files are NOT stored in this repository.

- All trained models are hosted on HuggingFace Hub.

- This ensures:

    - ✅ Faster GitHub cloning

    - ✅ No file size limit issues

    - ✅ Cleaner repository

## 👨‍💻 Author

- Developed by Kenny Janson
- Project: Language Classification using Transformer Models
