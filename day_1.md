# AI Engineer — Fundamentals Notes

## What is an AI Engineer?

An **AI Engineer** is a software developer who builds practical, production-ready AI applications. Instead of building complex AI models from scratch, they focus on integrating existing pre-trained models (like LLMs) and AI APIs into real-world systems — optimizing user experience while ensuring scalability and safety.

**The hierarchy:**

```
AI  >  ML  >  DL  >  LLM
```

Each layer is a subset of the one before it — AI is the broadest field, and LLMs are a highly specialized, modern application of Deep Learning.

---

## 1. AI (Artificial Intelligence)

**Definition:** The ability of a machine or computer to perform tasks that normally require human intelligence.

**Examples:**
- ChatGPT
- Siri & Google Assistant
- Self-driving cars
- Face recognition in smartphones
- Recommendation systems on YouTube & Netflix

**Goals of AI** — to make machines:

| Learn | Reason |
|---|---|
| Understand language | Solve problems |
| Make decisions | — |

---

## 2. ML (Machine Learning)

**Definition:** A subset of AI. Instead of directly programming every rule, we provide data and the machine learns patterns from it.

**Example — Spam Detection:**

| Approach | Formula |
|---|---|
| Traditional Programming | Rules + Data → Output |
| Machine Learning | Data + Output → **Model** |

> The model learns the rules automatically.

**Applications:** Spam detection · Stock prediction · Product recommendations

### Types of Machine Learning

#### a) Supervised Learning
The model learns from **labelled data** — meaning the correct answer is already provided.

| Input | Output |
|---|---|
| Spam Email | Spam |
| Email | Not Spam |

The model learns from these examples and predicts labels for new, unseen emails.

**Applications:** Spam detection · House price prediction · Student result prediction

#### b) Unsupervised Learning
The data has **no labels**. The model finds patterns or groups on its own.

**Example:** A shopping website has customer data but no predefined categories. The model may create groups like:
- High spenders
- Medium spenders
- New shoppers

**Applications:** Customer segmentation · Market analysis · Recommendation systems · Pattern detection

#### c) Reinforcement Learning
An **agent** learns by interacting with an environment, receiving:
- **Reward** for correct actions
- **Penalty** for wrong actions

The goal is to **maximize rewards**.

**Example — Teaching a dog:**
- Correct trick → Reward 🦴
- Wrong trick → No reward

The AI learns through trial and error, just like the dog.

**Applications:** Self-driving cars · Robotics · Game playing

#### d) Semi-Supervised Learning
Combines supervised and unsupervised learning. The dataset contains:
- A small amount of labelled data
- A large amount of unlabelled data

**Example:** Out of 10,000 images — 1,000 are labelled, 9,000 are unlabelled. The model uses both to improve learning.

**Applications:** Image recognition · Speech recognition · Medical diagnosis

> 💡 **Which type of ML does ChatGPT use?**
> ChatGPT is based on **Deep Learning** (a subset of ML) and is trained using a combination of:
> - Supervised Learning
> - Reinforcement Learning from Human Feedback (**RLHF**)

---

## 3. DL (Deep Learning)

**Definition:** A subset of ML that uses **Artificial Neural Networks**, inspired by the structure of the human brain.

**Why Deep Learning?**
It excels at handling complex, unstructured data:
- Images
- Voice
- Video
- Natural language

**Examples:** Face recognition · Self-driving cars · Medical image analysis

---

## 4. LLM (Large Language Model)

**Definition:** A Deep Learning model trained on huge amounts of text data.

**Examples:**
- OpenAI ChatGPT
- Google Gemini
- Meta Llama
- Claude (Anthropic)

**What can LLMs do?**
- Answer questions
- Generate code
- Write emails
- Translate languages
- Summarize text
- Create content

**How LLMs work (simplified pipeline):**

```
Train on massive data → Learn language patterns → Predict the next word
```

---

## Quick Reference Summary

| Layer | Subset of | Core Idea | Example |
|---|---|---|---|
| **AI** | — | Machines performing human-like tasks | Siri, self-driving cars |
| **ML** | AI | Learning patterns from data instead of hardcoded rules | Spam filters |
| **DL** | ML | Neural networks for complex, unstructured data | Face recognition |
| **LLM** | DL | Neural networks trained on massive text corpora | ChatGPT, Claude |
