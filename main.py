import os
import json

print("=== Corporate AI Knowledge Assistant Demo ===")
print("Reading and preparing documents (company_knowledge)...")

# Preparing document structure and payload (Source, Page)
documents_dir = "data"
chunks_with_payload = []

if os.path.exists(documents_dir):
    for filename in os.listdir(documents_dir):
        if filename.endswith(".txt"):
            file_path = os.path.join(documents_dir, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                # Adding text and file metadata to payload
                chunks_with_payload.append({
                    "chunk_text": content,
                    "payload": {
                        "Source": filename,
                        "Page": "Page 1"
                    }
                })
    print(f"✅ Prepared chunks: {len(chunks_with_payload)}")
else:
    print("❌ Error: 'data' folder not found!")

# Reading test questions
if os.path.exists("test_questions.json"):
    with open("test_questions.json", "r", encoding="utf-8") as f:
        test_questions = json.load(f)
        print(f"✅ Loaded test questions: {len(test_questions)}")

print("\nn8n pipeline (Question -> Embedding -> Qdrant -> Top-K -> Context -> LLM -> Answer) data is ready!")
