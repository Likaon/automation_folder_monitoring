# automation_folder_monitoring

Este script em Python monitora uma pasta de downloads e organiza automaticamente os arquivos em subpastas de acordo com o tipo (documentos, imagens, vídeos, etc).

Funcionalidades
Move arquivos para pastas específicas conforme a extensão (ex: PDFs vão para "Documentos", imagens para "Imagens").

Cria as pastas automaticamente caso não existam.

Roda em loop, verificando a pasta a cada 30 segundos.

Fácil de personalizar para incluir novos tipos de arquivos e pastas.

Requisitos
Python 3

Sistema operacional: Windows, macOS ou Linux

Como usar
Clone ou baixe este repositório.

Ajuste o caminho da pasta de downloads no arquivo organizador_downloads.py na variável DOWNLOADS_FOLDER.

Execute o script com:

bash
Copiar
Editar
python automation.py
O script ficará rodando em loop e organizará os arquivos automaticamente. Para parar, pressione Ctrl+C.

Exemplo de uso
Suponha que você tenha vários arquivos diferentes na pasta de downloads. Quando o script rodar, ele moverá arquivos como:

documento.pdf → pasta Documentos/

foto.jpg → pasta Imagens/

video.mp4 → pasta Videos/

Contato
Rodrigo Assarice
rodrigo.assarice@hotmail.com
