import subprocess

def test_ola():
    result = subprocess.run(['python', 'ola.py'], capture_output=True, text=True)
    
    assert "Olá Thayse" in result.stdout
