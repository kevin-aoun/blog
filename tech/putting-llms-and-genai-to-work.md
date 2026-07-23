---
title: "Putting LLMs and GenAI to Work"
layout: note
parent: Tech
date: 2024-02-16
author: Kevin Aoun
description: "A personal journey into the GenAI startup world, and five lessons from shipping with LLMs."
legacy: true
---

***In this blog post, I will share with you my journey venturing into the Generative AI startup world. By the end of the article, I will have shared 5 key lessons that you can leverage to stand out of the crowd in the AI market.***

> [!note] Disclaimer
> The technologies and companies mentioned in this article are for informational purposes only and do not constitute endorsement or sponsorship. Please perform your own research.

## Introduction

LLMs and Generative AI have taken the world by storm, and for good reason. These powerful technologies are transforming how we interact with information, create content, and automate tasks.

According to a recent report by McKinsey & Company, generative AI could add the equivalent of $2.6 trillion to $4.4 trillion annually—by comparison, the United Kingdom's entire GDP in 2021 was $3.1 trillion.[^mckinsey]

Another study by PwC shows that, quote, "AI could contribute up to $15.7 trillion to the global economy in 2030, more than the current output of China and India combined," endquote.[^pwc]

This impact is particularly evident in the startup world. More and more entrepreneurs are leveraging these technologies to build innovative solutions that address **specific industry needs.**

***But what exactly makes LLMs and Generative AI so attractive to startups?***

- **Versatility.** LLMs and Generative AI allow startups to focus on their core competencies while fine-tuning AI models for specific functionalities.
- **Efficiency.** By automating tasks and improving decision-making, LLMs and Generative AI can help startups reduce costs and increase operational efficiency.
- **(Almost Unfair) Competitive Advantage.** In a crowded market, incorporating cutting-edge technologies like LLMs and Generative AI can give startups a unique edge and attract investors and customers.

Thus, it seems evident that startups need to invest in explainable AI solutions to build trust with their customers.

And with more and more competition in this early field, you're going to need more than an AI to chat with. As of now, you can do that in 3 lines of code using frameworks such as LangChain.[^lcel]

Sounds easy, right? Well, yes, but how useful is this to a huge company with different document sources, different departments, hundreds of users per minute and a non-responsive interface? Not so much.

## Building something useful

The best advice that I can give you is: build something industry-specific that solves a genuine problem / inefficiency that industry has, and will either:

- Bring people closer to happiness;
- Move people away from inconveniences.

> [!target] Build an MLP, not an MVP
> Forget the MVP. Build an MLP (Minimum Lovable Product, as my team mentor always said) around that pain point — but remember, your final validation lies with the clients.

Get their hands on it, listen to their feedback, and iterate rapidly. Remember, a product loved by its creators but ignored by its users is perfect for gathering dust on the shelf.

## Pivoting fast

While in the bootstrap period, you will realize that some technologies are just better in some areas, while others might shine somewhere else.

The important takeaway is not to get anchored to a framework you love, just out of subjectivity.

For example, I realized that to build the data ingestion pipeline, LlamaIndex stood out thanks to its various plugins and data funnels.

On the other hand, LangChain (and LangSmith) proved to be better off when building agentic behavior (the "brains" of the product), since it gave me deeper control over everything happening under the hood.

## Try not to break the server, but when you do, learn from it

I broke the server twice. Thankfully, no users were using the application (yet). When I look back at it, I feel as if it was an inevitable stepping stone towards a better product.

In fact, some errors are just impossible to diagnose locally. For our case, we faced severe CPU spikes every time a query was received. Eventually, we pivoted towards a cloud-hosted solution, and the server was back up and running again.

I realized how I learned invaluable lessons, and I enjoyed every moment of it — until I had to figure out where the error came from. And I wish it was a semicolon.

## Optimizing your Infrastructure: Get Structure from Chaos

When you want to build a personal project never meant to see the light, you don't care much about optimizing algorithms and efficiency. But when user experience and churn rate depend on the latency and accuracy of the response, it's a different game. Optimizing your infrastructure becomes paramount.

For me, the challenge was the novel field, the lightning-fast evolving frameworks and the lack of (stable) documentation. In fact, you might wake up one day, work with a version of the docs, go grab a coffee, and come back to a new release.

Additionally, while my teammates and I were used to working with traditional, 100% predictable code, relying on this factor of "intelligent randomness" was certainly a challenge as well as an opportunity to learn.

## Strategic Team Building

I cannot stress how important it is to have reliable, loyal and dynamic team members, especially in the startup world. While the world around you is moving this fast, you must find responsible individuals to help you navigate the storm and build a genuinely useful solution.

Therefore, by having passionate and talented people on your side, you can focus more on building a product people love.

## Conclusion and Final Thoughts

It's important to remember that using LLMs and Generative AI in production is not without its challenges. These technologies require careful planning and development to ensure they are deployed ethically, responsibly, and securely.

However, while challenges exist, the potential of LLMs and Generative AI for startups is undeniable. By leveraging these technologies responsibly and strategically, startups can gain a competitive advantage, accelerate their growth, and create innovative solutions that address real-world problems.

[^mckinsey]: McKinsey & Company, [The economic potential of generative AI](https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/the-economic-potential-of-generative-AI-the-next-productivity-frontier) (2023).
[^pwc]: PwC, [Sizing the prize — Global AI Study](https://www.pwc.com/gx/en/issues/data-and-analytics/publications/artificial-intelligence-study.html).
[^lcel]: LangChain, [Prompt + LLM — the LCEL cookbook](https://python.langchain.com/docs/expression_language/cookbook/prompt_llm_parser).
