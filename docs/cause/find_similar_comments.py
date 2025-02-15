from sentence_transformers import SentenceTransformer, util

# Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Read comments from the file
with open(r"C:\Users\spand\Desktop\IITMTDS PROJECT1\comments.txt", encoding="utf-8") as f:
    comments = [line.strip() for line in f.readlines() if line.strip()]

# Compute embeddings
embeddings = model.encode(comments, convert_to_tensor=True)

# Find the most similar pair
max_sim = -1
most_similar_pair = (None, None)
for i in range(len(comments)):
    for j in range(i + 1, len(comments)):
        sim = util.pytorch_cos_sim(embeddings[i], embeddings[j]).item()
        if sim > max_sim:
            max_sim = sim
            most_similar_pair = (comments[i], comments[j])

# Write the most similar comments to the output file
with open("/data/comments-similar.txt", "w", encoding="utf-8") as f:
    f.write(most_similar_pair[0] + "\n" + most_similar_pair[1])

print("Task A9 completed: Most similar comments written to /data/comments-similar.txt")
