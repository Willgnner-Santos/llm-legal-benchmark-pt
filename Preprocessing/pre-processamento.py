import os
import re
import pandas as pd
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import string
import unidecode
from docx import Document
import pypandoc
from tqdm import tqdm

import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Diretório base atualizado
base_dir = r'C:\Users\engwi\OneDrive\Documentos\Pasta compactada - peças DPE'

# Inicializar lematizador
lemmatizer = WordNetLemmatizer()

# Carregar stopwords
stop_words = set(stopwords.words('portuguese'))

# Verifique e instale o pandoc, se necessário
try:
    if not pypandoc.get_pandoc_path():
        pypandoc.download_pandoc()
except OSError as e:
    print(e)

def clean_text(text):
    # Remoção de HTML
    text = BeautifulSoup(text, "html.parser").get_text()

    # Remoção de URLs, emails, etc.
    text = re.sub(r'http\S+|www\S+|https\S+|@\S+', '', text, flags=re.MULTILINE)

    # Remoção de caracteres não alfanuméricos
    text = re.sub(r'\W', ' ', text)

    # Remoção de números
    text = re.sub(r'\d', '', text)

    # Transformar em minúsculas
    text = text.lower()

    # Remover acentuação
    text = unidecode.unidecode(text)

    # Remover stopwords e lematizar
    tokens = word_tokenize(text)
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words and word not in string.punctuation]

    # Juntar tokens em uma string
    text = ' '.join(tokens)

    return text

def read_docx(file_path):
    doc = Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])

def convert_to_docx(file_path, new_extension='.docx'):
    new_file_path = file_path.rsplit('.', 1)[0] + new_extension
    if file_path.endswith('.odt'):
        pypandoc.convert_file(file_path, 'docx', outputfile=new_file_path)
    return new_file_path

def process_directory(directory):
    rows = []
    category_id_map = {}
    current_id = 1
    file_count = sum([len(files) for r, d, files in os.walk(directory)])

    with tqdm(total=file_count, desc="Processing files") as pbar:
        for root, dirs, files in os.walk(directory):
            category = os.path.basename(root)
            if category not in category_id_map:
                category_id_map[category] = current_id
                current_id += 1
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    if file.endswith('.docx'):
                        content = read_docx(file_path)
                    elif file.endswith('.odt'):
                        docx_file_path = convert_to_docx(file_path)
                        content = read_docx(docx_file_path)
                    else:
                        print(f'Arquivo com a extensão {file.split(".")[-1]} (ignorado): {file_path}')
                        pbar.update(1)
                        continue
                    cleaned_text = clean_text(content)
                    rows.append({
                        'COLUNA_TEXTO': cleaned_text,
                        'CATEGORIA': category,
                        'ID_CATEGORIA': category_id_map[category]
                    })
                except Exception as e:
                    print(f'Error processing file {file_path}: {e}')
                pbar.update(1)
    return rows

# Processar o diretório e obter os dados
data = process_directory(base_dir)

# Criar DataFrame e salvar em Excel
df = pd.DataFrame(data)
output_path = os.path.join(base_dir, 'preprocessed_texts.xlsx')
df.to_excel(output_path, index=False)

print(f'Processamento concluído e dados salvos em {output_path}')
