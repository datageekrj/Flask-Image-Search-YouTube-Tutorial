# 🔍 AI Image Search App with CLIP + Flask

An **AI-powered Image Search App** built with [OpenAI's CLIP model](https://github.com/openai/CLIP) and Flask.  
Enter a text query like **"a cute cat"** and retrieve the most relevant images from your dataset.

---

## 🚀 Demo
![Demo Screenshot](static/demo.png)  
*(Add a screenshot of your web app here)*

---

## ✨ Features
- **CLIP Embeddings:** Encodes both text and images into the same semantic space.
- **Text-to-Image Search:** Finds the most relevant images using cosine similarity.
- **Flask Web Interface:** A simple search form with real-time results.
- **CPU-Friendly:** Works on any machine without GPU acceleration.

---

## 📦 Installation
### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/clip-image-search.git
cd clip-image-search
````

### 2. Install Dependencies

```bash
pip install torch torchvision pillow ftfy regex tqdm flask
pip install git+https://github.com/openai/CLIP.git
```

---

## 🖼️ Add Your Images

Place your dataset images inside:

```
static/images/
```

Example:

```
static/images/
  ├── cat1.jpg
  ├── dog1.jpg
  └── car1.jpg
```

---

## ▶️ Run the App

```bash
python app.py
```

Now open your browser at:
**[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

## 📂 Project Structure

```
clip-image-search/
│
├── app.py                   # Main Flask app
├── search.py                # Search logic using CLIP
├── generate_embeddings.py   # Precompute embeddings
├── templates/
│   └── index.html           # Frontend template
└── static/
    └── images/              # Image dataset
```

---

## 🎥 YouTube Tutorial

I’ve created a **step-by-step video guide** on building this project:
👉 **[Watch on YouTube](https://youtube.com/yourvideo)**

---

## 🧠 Next Steps / Improvements

* Add **image-to-image search** (query with an image instead of text).
* Use **FAISS** for fast vector search on large datasets.
* Deploy the app on **Render**, **Vercel**, or **Heroku**.

---

## 📜 License

This project is licensed under the **MIT License** – feel free to use and modify.

---

## ⭐ Show Your Support

If this project helped you, **star the repo** ⭐ and share it with others!

```
