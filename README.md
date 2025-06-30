# Impact of Input Representation on LLMs for Legal Document Classification in Portuguese: A Comparative Study

This study evaluates the use of Large Language Models (LLMs) with prompt engineering for classifying legal petitions in Portuguese by procedural type. Four input representations are compared: full text, summaries, centroids, and semantic descriptions. The experiments use real data in Portuguese from a Public Defender's Office in Brazil. Results show that summaries reduce token cost by more than 90\% and improve macro F1-score. The findings confirm that input representation can impact LLM effectiveness. LLMs via prompting outperform traditional models without requiring labeled data or training. The approach can be flexible and economically viable for legal document classification.

## Prerequisites

- **Python 3.8+**
- **Google Colab** (or local environment with Jupyter Notebook)
- **API Key** to access the model 

## Installation

Install necessary dependencies:

```bash
pip install tiktoken langchain-community langchainhub langchain_openai langchain pandas matplotlib scikit-learn seaborn
pip install imbalanced-learn
```

1. Mount Google Drive:
   - The project required access to Google Drive to load the corpus and save the results.
   - Run the following command in Colab:
     
```bash
from google.colab import drive
drive.mount('/content/drive')
```

2. Model Configuration:
  - Configure ChatOpenAI with your desired API key and template. The LLMs available from the [Together.AI](https://docs.together.ai/docs/chat-models).

**meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo**

```bash

from langchain_openai import ChatOpenAI

api_key = 'YOUR_API_KEY'
llm = ChatOpenAI(api_key=api_key, model='meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo')

```

3. Preparation of Corpus:
   - Upload the corpus of legal petitions from Google Drive and filter texts with less than **XXX** tokens ([Context length - Together.AI](https://docs.together.ai/docs/chat-models)).

4. Classification and Generation of Summaries:
   - Use customized methods (**Original-Text**, **Centroids**, **Descriptions** and **Summaries**) to classify and summarize legal texts.
  
5. Metrics and Visualizations:
   - Calculate metrics such as precision, recall, F1-score.
   - Visualize results using bar charts, histograms, and confusion matrices.
  
6. Saving the Results:
   - Save results, including classifications, metrics reports, and confusion matrices, directly to Google Drive.

7. Credits
   - This project was developed by **MSc. Willgnner Ferreira Santos** [Lattes](http://lattes.cnpq.br/3203020327904139), **Prof. Dr. Arlindo Rodrigues Galvão Filho** [Lattes](http://lattes.cnpq.br/7744765287200890), **Prof. Dr. Sávio Salvarino Teles de Oliveira** [Lattes](http://lattes.cnpq.br/1905829499839846), and **MSc. João Paulo Cavalcante Presa** [Lattes](http://lattes.cnpq.br/5092666506514753) as part of a study on the evaluation of large language models for classifying legal documents in portuguese.
 

















