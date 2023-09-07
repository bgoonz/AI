# AI Chat-GPT & LLM's

### (Chat Generative Pre-trained Transformer) and Large Language Models (LLMs) like GPT-3 are a type of artificial intelligence model designed for natural language processing. Here's a summary of how they work:

#### [Link To Chat](https://chat.openai.com/)

1. Pre-training:

- These models are pre-trained on vast amounts of text data from the internet. During this phase, they learn to predict the next word in a sentence by analyzing the context of the previous words. This process helps them develop an understanding of grammar, syntax, and some level of world knowledge.

2. Transformer Architecture:

- Both Chat-GPT and LLMs are built on the Transformer architecture, which is a deep neural network model. The Transformer architecture is designed to handle sequential data, making it well-suited for natural language understanding and generation tasks.

3. Tokenization:

- Text is divided into smaller units called tokens, which can be words, subwords, or characters. These models tokenize input text, allowing them to process and generate text in discrete chunks.

4. Attention Mechanism:

- Transformers use attention mechanisms to weigh the importance of different tokens in a sequence. This helps capture long-range dependencies and relationships between words.

5. Fine-tuning:

- After pre-training, these models are fine-tuned on specific tasks or domains. For example, they can be fine-tuned for chatbot applications, text completion, translation, question-answering, and more. Fine-tuning helps customize the model's behavior for a particular task.

6. Inference:

- When you input a query or text to Chat-GPT or an LLM, the model generates responses or predictions based on its pre-trained knowledge and fine-tuning. It uses the learned patterns, context, and statistical relationships between words to generate coherent and contextually relevant responses.

7. Contextual Understanding:

- These models have the ability to maintain context over multiple turns of conversation, allowing them to generate responses that are contextually relevant to the ongoing conversation.

8. Limitations:

- Despite their impressive capabilities, Chat-GPT and LLMs have limitations. They can produce plausible-sounding but incorrect or biased information, as they generate responses based on patterns in their training data. Ensuring the accuracy and reliability of their responses is an ongoing challenge.

9. Ethical and Bias Concerns:

- These models can inadvertently perpetuate biases present in their training data, and they can be used for malicious purposes. Efforts are being made to address these ethical concerns and improve model behavior.

---

### Prompts:

- A prompt is text input that describes your problem or request.

  > Some exapmles of prompts:

- How many citizens are there in Barcelona?
- Who is the first president of the United States...
- Who is Michael Jordan?

- In all of the examples above the questions are unrelated to each other... however Chat-GPT is context aware... which means that (up to a certain number of tokens) it can factor in previous questions for context in answering the most current question asked of it.
- Chat-GPT is programmed to have a certain amount of randomness to it's responses so the same question asked multiple times will not always result in the same answer.

> Example of answering a question with context:

- What is a Wiener Schnitzel?
- Please give me the recipe?

  - In this case chat GPT will use the first question to help answer the second question.


> Chat-GPT was trained on data up to `September 2021`


- If you give chat-GPT a url and ask it to sumarize the article... it will fake a description of the article... it will not actually summarize the article... rember it does not actually have access to the internet.


