import subprocess

def test_ola():
    # Executar o script ola.py e capturar a saída
    result = subprocess.run(['python', 'ola.py'], capture_output=True, text=True)
    
    # Verificar se a saída contém "Olá"
    assert "Olá" in result.stdout
