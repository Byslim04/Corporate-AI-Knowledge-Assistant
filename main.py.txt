import os
import json

print("=== Corporate AI Knowledge Assistant Demo ===")
print("Инициализация базы знаний компании (company_knowledge)...")

# Демонстрация загрузки документов и структуры payload (Source, Page)
documents_dir = "data"
chunks_with_payload = []

if os.path.exists(documents_dir):
    for filename in os.listdir(documents_dir):
        if filename.endswith(".txt"):
            file_path = os.path.join(documents_dir, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                # Имитация чанкирования и добавления payload
                chunks_with_payload.append({
                    "chunk_text": content,
                    "payload": {
                        "Source": filename,
                        "Page": "Page 1"
                    }
                })
    print(f"[Успех] Загружено документов: {len(chunks_with_payload)}")
else:
    print("[Ошибка] Папка data не найдена!")

# Загрузка тестовых вопросов
if os.path.exists("test_questions.json"):
    with open("test_questions.json", "r", encoding="utf-8") as f:
        test_questions = json.load(f)
        print(f"[Успех] Загружено тестовых вопросов: {len(test_questions)}")

print("\nПайплайн n8n (Question -> Embedding -> Qdrant -> Top-K -> Context -> LLM -> Answer) готов к интеграции!")