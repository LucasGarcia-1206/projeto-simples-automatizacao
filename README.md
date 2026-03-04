# projeto-simples-automatizacao

Projeto simples de automatizacao com `pyautogui` para preencher formularios automaticamente a partir do arquivo `produtos.csv`.

## Requisitos

- Python 3.10+
- Google Chrome instalado
- Ambiente com interface grafica (desktop). Nao funciona em servidor headless sem `DISPLAY`.

## Arquivos do projeto

- `auto.py`: script principal da automacao
- `produtos.csv`: base de produtos a serem cadastrados

## Como rodar

### Windows (PowerShell)

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install pyautogui pandas
python auto.py
```

### Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pyautogui pandas
python auto.py
```

## Observacoes importantes

- O script usa coordenadas fixas de clique (`EMAIL_FIELD_POSITION` e `PRODUCT_CODE_FIELD_POSITION`) definidas em `auto.py`.
- Mantenha o Chrome e a tela na mesma configuracao esperada pelo script.
- As credenciais estao no codigo (`Config.EMAIL` e `Config.PASSWORD`). Se for compartilhar o projeto, substitua por variaveis de ambiente.
