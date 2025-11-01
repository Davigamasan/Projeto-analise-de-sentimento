📊 Projeto de Análise de Sentimento
Um projeto web completo para análise de sentimentos em textos usando Flask e modelos de machine learning pré-treinados da Hugging Face.

🚀 Visão Geral
Este projeto permite que usuários analisem o sentimento (positivo ou negativo) de qualquer texto através de uma interface web simples e intuitiva. A aplicação combina o poder do Flask para o backend com modelos de IA state-of-the-art para classificação de sentimentos.

🛠️ Como Funciona
Arquitetura do Sistema
text
Frontend (HTML/JS) → Backend (Flask) → Modelo Hugging Face → Resposta
Fluxo de Execução
Inicialização:

Servidor Flask é iniciado

Modelo de IA é carregado uma vez durante o startup

Rotas são configuradas

Interação do Usuário:

Usuário digita texto na interface web

JavaScript captura o texto e envia para o backend

Flask processa a requisição e usa o modelo para análise

Resultado é retornado e exibido na página

📁 Estrutura do Projeto
text
projeto-analise-sentimento/
├── app.py                 # Aplicação Flask principal
├── templates/
│   └── index.html        # Interface do usuário
├── static/
│   └── style.css         # Estilos CSS (opcional)
├── requirements.txt      # Dependências do projeto
└── README.md            # Este arquivo
🔧 Tecnologias Utilizadas
Backend: Flask

Modelo de IA: Hugging Face Transformers

Frontend: HTML5, JavaScript, CSS3

Processamento: PyTorch/TensorFlow (dependendo do modelo)

⚙️ Instalação e Configuração
Pré-requisitos
Python 3.8+

pip (gerenciador de pacotes Python)
