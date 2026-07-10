# LangChain text splitting: RecursiveCharacterTextSplitter vs CharacterTextSplitter, chunk_size/chunk_overlap parameters, splitting raw text, creating documents, and printing chunks--

# from langchain_text_splitters import RecursiveCharacterTextSplitter

text_data = '''Artificial Intelligence (AI) is one of the most transformative technologies of the modern era. It refers to the ability of machines and computer systems to perform tasks that typically require human intelligence. These tasks include learning from experience, understanding natural language, recognizing patterns, solving problems, and making decisions. AI has evolved significantly over the past few decades, moving from theoretical concepts and research laboratories to practical applications used by millions of people every day.

The history of artificial intelligence can be traced back to the 1950s when computer scientists began exploring the possibility of creating machines that could think and reason like humans. Early AI systems were limited by the computing power available at the time, but researchers remained optimistic about the future of the field. Over the years, advances in hardware, software, and data availability have enabled AI systems to become increasingly sophisticated.

Machine Learning is a major branch of AI that focuses on enabling computers to learn from data without being explicitly programmed for every task. Instead of following fixed instructions, machine learning algorithms identify patterns in data and use those patterns to make predictions or decisions. Examples include email spam filters, recommendation systems, and fraud detection systems. Machine learning has become one of the most widely used AI technologies due to its effectiveness and flexibility.

Deep Learning is a specialized subset of machine learning that uses artificial neural networks inspired by the structure of the human brain. These neural networks consist of multiple layers that process information and learn complex representations of data. Deep learning has achieved remarkable success in areas such as image recognition, speech recognition, and natural language processing. Applications like facial recognition systems, virtual assistants, and self-driving cars rely heavily on deep learning techniques.

Natural Language Processing (NLP) is another important area of AI. NLP focuses on enabling computers to understand, interpret, and generate human language. Technologies such as chatbots, machine translation systems, sentiment analysis tools, and voice assistants are built using NLP. Large Language Models (LLMs) such as GPT, Claude, and Gemini have demonstrated impressive capabilities in understanding context, generating coherent text, answering questions, and assisting with a wide range of tasks.

The development of AI has had a significant impact on many industries. In healthcare, AI is used to analyze medical images, assist with diagnoses, predict disease outbreaks, and support personalized treatment plans. In finance, AI helps detect fraudulent transactions, assess credit risk, and automate trading strategies. In manufacturing, AI-powered robots improve efficiency and reduce operational costs. In transportation, AI contributes to route optimization, traffic management, and autonomous vehicle development.

Education has also benefited from AI technologies. Intelligent tutoring systems can adapt learning materials to the needs of individual students, while automated grading systems help teachers save time. AI-powered educational platforms can provide personalized recommendations, identify areas where students need additional support, and create interactive learning experiences. These tools have the potential to make education more accessible and effective.

Despite its many benefits, AI also presents several challenges and concerns. One major issue is the potential for bias in AI systems. Since machine learning models learn from data, they can inherit biases present in the training data. This can lead to unfair outcomes in areas such as hiring, lending, and law enforcement. Researchers and policymakers are actively working to develop methods for reducing bias and ensuring fairness in AI systems.

Privacy is another important concern. Many AI applications rely on large amounts of personal data, raising questions about how that data is collected, stored, and used. Organizations must implement strong security measures and comply with regulations to protect user privacy. Transparency and accountability are also essential to building trust in AI systems.

The future of AI is expected to bring even more innovations. Researchers are exploring advanced techniques such as reinforcement learning, federated learning, and explainable AI. These approaches aim to improve the performance, reliability, and transparency of AI systems. As AI continues to evolve, it is likely to play an increasingly important role in shaping society, the economy, and everyday life.

Ultimately, artificial intelligence is a powerful tool that has the potential to solve complex problems and improve human well-being. However, responsible development and deployment are crucial to ensuring that its benefits are shared broadly and that potential risks are managed effectively. By balancing innovation with ethical considerations, society can harness the full potential of AI while minimizing negative consequences.'''

# splitter = RecursiveCharacterTextSplitter(
#     chunk_size=100,     
#     chunk_overlap=20   
# )

# chunks = splitter.split_text(text_data)
# print(chunks)
# print(chunks[0])  
# print(chunks[1])

# for i, chunk in enumerate(chunks):
    # print(f"Chunk {i}:\n{chunk}\n{'-'*50}")

# docs = splitter.create_documents([text_data])
# print(docs)
# for doc in docs:
#     print(doc.page_content)

# split_docs = splitter.split_documents(docs)

# for doc in split_docs:
#     print(split_docs)

#character splitter

from langchain_text_splitters import CharacterTextSplitter

splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=100,
    chunk_overlap=20
)

chunks = splitter.split_text(text_data)    
for i, chunk in enumerate(chunks):
   print(f"Chunk {i}:\n{chunk}\n{'-'*50}")