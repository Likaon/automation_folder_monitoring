import os
import shutil
import time

# Caminho da pasta para monitorar (mude para a sua pasta de downloads)
DOWNLOADS_FOLDER = os.path.expanduser("~/Downloads")

# Pastas de destino organizadas por tipo
FOLDERS = {
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Arquivos_Comprimidos": [".zip", ".rar", ".tar", ".gz"],
    "Programas": [".exe", ".msi", ".bat", ".sh"],
}

def organizar_arquivos():
    arquivos = os.listdir(DOWNLOADS_FOLDER)
    for arquivo in arquivos:
        caminho_arquivo = os.path.join(DOWNLOADS_FOLDER, arquivo)

        # Ignora pastas
        if os.path.isdir(caminho_arquivo):
            continue

        extensao = os.path.splitext(arquivo)[1].lower()

        for pasta, ext_list in FOLDERS.items():
            if extensao in ext_list:
                pasta_destino = os.path.join(DOWNLOADS_FOLDER, pasta)
                if not os.path.exists(pasta_destino):
                    os.makedirs(pasta_destino)

                destino = os.path.join(pasta_destino, arquivo)
                try:
                    shutil.move(caminho_arquivo, destino)
                    print(f"Movido: {arquivo} -> {pasta_destino}")
                except Exception as e:
                    print(f"Erro ao mover {arquivo}: {e}")
                break

if __name__ == "__main__":
    print("Organizador de Downloads iniciado. Ctrl+C para parar.")
    try:
        while True:
            organizar_arquivos()
            time.sleep(30)  # Roda a cada 30 segundos
    except KeyboardInterrupt:
        print("Programa finalizado pelo usuário.")