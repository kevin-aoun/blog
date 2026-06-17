---
title: "GenAI: Cash in the Code"
layout: note
parent: Tech
nav_order: 2
date: 2024-02-23
author: Kevin Aoun
description: "Key insights into LangChain and LlamaIndex for standing out in the AI market."
---

***In this blog post, I will share key insights into LangChain and LlamaIndex that you can leverage to stand out of the crowd in the AI market.***

## Introduction

According to a recent report by McKinsey & Company, generative AI could add the equivalent of $2.6 trillion to $4.4 trillion annually—by comparison, the United Kingdom's entire GDP in 2021 was $3.1 trillion.

This impact is particularly evident in the startup world. More and more entrepreneurs are leveraging these technologies to build innovative solutions that address **specific industry needs.**

***But what exactly makes LLMs and Generative AI so attractive to startups?***

- **Versatility.** LLMs and Generative AI allow startups to focus on their core competencies while fine-tuning AI models for specific functionalities.
- **Efficiency.** By automating tasks and improving decision-making, LLMs and Generative AI can help startups reduce costs and increase operational efficiency.
- **(Almost Unfair) Competitive Advantage.** In a crowded market, incorporating cutting-edge technologies like LLMs and Generative AI can give startups a unique edge and attract investors and customers.

Sounds easy, right? Well, yes, but how useful is a general-purpose model to a huge company with personalized document sources, different departments, hundreds of users per minute and a non-responsive interface? Not so much.

Thus, it seems evident that startups need to invest in fine-tuned, scalable and tunable AI solutions to build trust with their customers.

In LLM development, be it Retrieval Augmented Generation (RAG) or Agentic Behavior Systems, two frameworks seem to stand out: LangChain and LlamaIndex. In this blog post, we'll dive into each one of them, highlighting their strengths and where / how to combine them in production.

## LangChain

With over 20M downloads of their open-source package powering 30k+ apps, it's safe to say that LangChain is one of the most popular LLM orchestrating frameworks as of today.

You can get started with LangChain in a few lines of code:

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

prompt = ChatPromptTemplate.from_template("tell me a joke about {subject}")
api_key = "your_api_key"
model = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=api_key)

chain = (
    prompt
    | model
    | StrOutputParser()
)

chain.invoke({"subject": "AI startups"})
```

This code will allow you to chat with the Gemini Pro model using your custom prompt (assuming you provide your Gemini API key — you can get one at <https://aistudio.google.com/app/apikey>).

The pipe symbol (`|`) is part of the LangChain Expression Language, or LCEL. It allows you to build readable, scalable and efficient chains, passing the output of one element to another. For example, the prompt is the input to the model, and the output of the model is an input to the output parser, which finally returns to the user.

Notice how the parameter passed in the prompt template needs to be the same as the one passed in the dictionary of `chain.invoke()`.

Finally, the output parser's purpose is to make the LLM output more readable and UX-friendly.

However, in my humble experience working with LangChain, I found it particularly useful when planning your own agents.

Agents are intelligent AI systems capable of using tools and making decisions (building a chain of thought, or CoT) to respond to a user query. Read more about agents: <https://python.langchain.com/docs/modules/agents/quick_start>

Moreover, LangSmith proved to be essential while developing agents since it gave me a deeper insight over everything happening under the hood: from which model got called at what time with how many tokens as input, and even how fast it was to generate a response.

This "observability" platform is crucial, especially when you need to examine the chain of thought of your agent to optimize or debug it. You can get started with LangSmith at <https://www.langchain.com/langsmith>.

## LlamaIndex

LlamaIndex is another popular framework for LLM development that caught developers' attention thanks to its highly customizable and controllable query pipeline and routing.

LlamaIndex's strength lies in its diverse data querying engines, supporting pandas, SQL, PDFs, tabular files, and others, making data ingestion pipelines and querying exceptionally convenient.

This comes very handy in techniques such as Retrieval Augmented Generation.

In a nutshell, RAG is a technique where user queries are converted to machine-readable numbers, matched to text embeddings in vector databases (e.g., Chroma, FAISS, Qdrant), and relevant context is retrieved for LLM prompts.

Thus, having a clean data pipeline is paramount, since the answer of the LLM heavily depends on the context window that you provide. Always remember, no matter how good your model is: garbage in equals garbage out.

Let's evaluate a simple example in practice using LlamaIndex:

```python
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()
response = query_engine.query("How to cook a banana cake?")
print(response)
```

Let's evaluate the code line by line to understand the core concepts.

- `documents = SimpleDirectoryReader("data").load_data()`

  We are creating the `documents` object by using a directory reader that reads from the `./data` folder and loads the data found there. In this case, the data is a simple txt file with sample recipes, but as mentioned before, you can find all sorts of document loaders native to LlamaIndex or made by the community. More info at <https://llamahub.ai/> and the LlamaIndex documentation: <https://docs.llamaindex.ai/en/stable/getting_started/starter_example.html>

- `index = VectorStoreIndex.from_documents(documents)`

  Here, we are creating the search index from the documents we loaded previously. Think of it as a primitive vector database that lives in memory.

- `query_engine = index.as_query_engine()`

  Finally, we create the query engine by querying the search index. This will send the user query to the vector database, perform similarity search and return the most relevant answer to the user.

## Conclusion

In conclusion, navigating the dynamic landscape of Generative AI for startups involves considering the context-specific strengths of LangChain and LlamaIndex.

LangChain proves efficient in LLM orchestration and excels in crafting custom agents, complemented by the observability offered by LangSmith. On the other hand, LlamaIndex stands out for its highly customizable query pipeline, enabling precise control over query formulation and context construction.

Recognizing the synergy between the two — LangChain for efficient orchestration and LlamaIndex for efficient data querying — their combined capabilities promise a robust and tailored application ready to face the competitive AI market.

*Disclaimer: The technologies and companies mentioned in this article are for informational purposes only and do not constitute endorsement or sponsorship. Please perform your own research.*
