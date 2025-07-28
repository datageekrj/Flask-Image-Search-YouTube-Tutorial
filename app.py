from flask import Flask, request, render_template
import clip
import os
from PIL import Image
import numpy as np
import torch

model, preprocess = clip.load("ViT-B/32", device = "cpu")
image_files = [f for f in os.listdir("static/images")]

embeddings = []
for img_file in image_files:
    image = Image.open(os.path.join("static/images", img_file))
    image_preprocessed = preprocess(image).unsqueeze(0).to("cpu")
    with torch.no_grad():
        image_embedding = model.encode_image(image_preprocessed)
        image_embedding /= image_embedding.norm(dim = -1, keepdim = True)
    embeddings.append(image_embedding.cpu().numpy())

embeddings = np.vstack(embeddings)

def search_images(query, top_k = 1):
    text = clip.tokenize([query]).to("cpu")
    with torch.no_grad():
        text_embedding = model.encode_text(text)
        text_embedding /= text_embedding.norm(dim = -1, keepdim = True)
    sims = (embeddings @ text_embedding.cpu().numpy().T).squeeze()
    top_indices = sims.argsort()[-top_k:][::-1]
    return [image_files[i] for i in top_indices]

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def home():
    results = []
    if request.method == "POST":
        query = request.form.get("query")
        results = search_images(query)
    return render_template("index.html", results = results)

if __name__ == "__main__":
    app.run(debug = True)