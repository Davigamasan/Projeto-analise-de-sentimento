
# install_deps.py
import subprocess
import sys

def install_packages():
    packages = [
        "streamlit==1.32.0",
        "transformers==4.40.0",
        "torch==2.3.0 --index-url https://download.pytorch.org/whl/cpu",
        "pandas==2.2.2",
        "plotly==5.22.0",
        "accelerate==0.30.1",
        "safetensors==0.4.3",
        "protobuf==4.25.3",
        "numpy==1.26.4"
    ]
    
    print("Instalando dependências compatíveis com Python 3.12...")
    
    for package in packages:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"✅ {package} instalado")
        except subprocess.CalledProcessError:
            print(f"❌ Falha ao instalar {package}")
    
    print("\nInstalação concluída! Execute: streamlit run app.py")

if __name__ == "__main__":
    install_packages()
