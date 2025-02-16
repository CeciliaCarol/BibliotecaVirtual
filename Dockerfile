# usa a imagem oficial do python
FROM python:3.10

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos do projeto para dentro do container
COPY . .

# Instala as dependencias
RUN pip install --no-cache-dir -r requirements.txt

#Expoe a porta do django
EXPOSE 8000

#Comando para rodas a aplicação
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]