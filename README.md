# Corporate AI Knowledge Assistant 🤖💼

Проект представляет собой корпоративный ИИ-ассистент на базе архитектуры RAG (Retrieval-Augmented Generation), интегрированный через n8n и векторную базу данных Qdrant.

## 🚀 Архитектура и пайплайн (n8n Workflow)
Пайплайн обработки запроса пользователя состоит из следующих шагов:
1. Question — получение пользовательского вопроса.
2. Embedding — векторизация текста запроса.
3. Qdrant (Vector Database) — поиск похожих векторов в коллекции company_knowledge.
4. Top-K — выборка наиболее релевантных фрагментов.
5. Context — формирование единого контекста из найденных чанков.
6. LLM — генерация ответа языковой моделью строго на основе контекста.
7. Answer — выдача ответа с обязательным указанием метаданных Source и Page.

## 📁 Структура проекта
- data/ — текстовые документы компании (продукты, доставка, возвраты, оплата, FAQ).
- test_questions.json — набор из 20 тестовых вопросов для проверки точности ассистента.
- main.py — демонстрационный скрипт инициализации данных и проверки пайплайна.

## 🛠 Технологии
- Low-code / Workflow: n8n
- Vector DB: Qdrant
- Embeddings & LLM: OpenAI / HuggingFace
- Language: Python


----------


# Corporate AI Knowledge Assistant

This project represents a corporate AI assistant based on RAG (Retrieval-Augmented Generation) architecture, integrated via n8n and the Qdrant vector database.

## ⚙️ Architecture and Pipeline (n8n Workflow)

The user query processing pipeline consists of the following steps:

1. Question — receiving the user's question.
2. Embedding — vectorization of the query text.
3. Qdrant (Vector Database) — searching for similar vectors in the company_knowledge collection.
4. Top-K — selecting the most relevant fragments.
5. Context — forming a unified context from the found chunks.
6. LLM — generating a response by the language model strictly based on the context.
7. Answer — issuing the response with mandatory indication of the Source and Page metadata.

## 📂 Project Structure

* data/ — company text documents (products, delivery, returns, payment, FAQ).
* test_questions.json — a set of 20 test questions to check the assistant's accuracy.
* main.py — a demonstration script for data initialization and pipeline verification.

## 🛠️ Technologies

* Low-code / Workflow: n8n
* Vector DB: Qdrant
* Embeddings & LLM: OpenAI / HuggingFace
* Language: Python
