# Use a imagem oficial do Python como base
FROM python:3.11

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências do projeto
Run pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copia o arquivo main.py para o diretório de trabalho
COPY main.py .

# Define a porta que o contêiner irá expor
EXPOSE 5000
# Comando para executar o aplicativo quando o contêiner for iniciado
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:main"]
