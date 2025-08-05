# 📂 Automation: Folder Monitoring and File Organizer
Python script to monitor a downloads folder and automatically organize files into subfolders by type (documents, images, videos, etc).

---

# ✅ Features
📁 Moves files to specific folders based on extension
(e.g. .pdf → Documentos, .jpg → Imagens)


 📦 Automatically creates target folders if they don’t exist


 🔄 Runs in loop (every 30 seconds)


 🛠️ Easy to customize with new file types and destinations

---

# 🧱 Requirements
Python 3.x
OS: Windows, macOS, or Linux

---

# ⚙️ How to Use
Clone or download this repository

Edit the download folder path
In organizador_downloads.py, update this variable:

DOWNLOADS_FOLDER = 'Path/to/your/Downloads/folder'
Run the script

python automation.py
The script will continuously monitor the folder.
Press Ctrl+C to stop.

---

# 💡 Example
Suppose your Downloads folder contains:


documento.pdf
foto.jpg
video.mp4
After running the script:

documento.pdf → moved to Documentos/

foto.jpg → moved to Imagens/

video.mp4 → moved to Videos/

---

# 📂 Automação: Monitoramento de Pasta e Organização de Arquivos

Script em Python que monitora a pasta de downloads e organiza automaticamente os arquivos em subpastas conforme o tipo (documentos, imagens, vídeos, etc).

---

## ✅ Funcionalidades

- 📁 Move arquivos para pastas específicas com base na extensão  
  (ex: `.pdf` → **Documentos**, `.jpg` → **Imagens**)

- 📦 Cria automaticamente as pastas de destino, se não existirem

- 🔄 Executa em loop (verifica a cada 30 segundos)

- 🛠️ Fácil de personalizar com novos tipos de arquivos e pastas

---

## 🧱 Requisitos

- Python 3.x  
- Sistema operacional: Windows, macOS ou Linux

---

## ⚙️ Como Usar

1. **Clone ou baixe este repositório**

2. **Edite o caminho da pasta de downloads**  
   No arquivo `organizador_downloads.py`, atualize a variável:

   ```python
   DOWNLOADS_FOLDER = 'Caminho/para/sua/pasta/Downloads'
Execute o script

python automation.py
O script ficará rodando em segundo plano.
Pressione Ctrl+C para encerrar.

💡 Exemplo de Uso
Suponha que sua pasta de Downloads contenha:

documento.pdf
foto.jpg
video.mp4
Após rodar o script:

documento.pdf → movido para Documentos/

foto.jpg → movido para Imagens/

video.mp4 → movido para Videos/

---

# ✍️ Autor
Rodrigo Assarice

📧 rodrigo.assarice@hotmail.com
