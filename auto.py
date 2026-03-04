import pyautogui as autogui
import pandas as pd
import time
from typing import Tuple, Dict, Any


# CONSTANTES DE CONFIGURAÇÃO
class Config:
    """Centraliza todas as configurações da aplicação."""

    LOGIN_URL = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
    EMAIL = 'lucasgmikas@gmail.com'
    PASSWORD = '123'
    
    EMAIL_FIELD_POSITION = (399, 353)
    PRODUCT_CODE_FIELD_POSITION = (460, 249)
    
    AUTOMATION_PAUSE = 0.5
    PAGE_LOAD_DELAY = 2
    SCROLL_AMOUNT = 5000
    
    PRODUCTS_CSV_FILE = 'produtos.csv'


def setup_automation() -> None:
    """Configura as definições iniciais da automação."""
    autogui.PAUSE = Config.AUTOMATION_PAUSE


def open_browser_and_navigate(url: str) -> None:
    """
    Abre o navegador Chrome e navega para a URL especificada.
    
    Args:
        url: URL de destino
    """
    autogui.press('win')
    autogui.write('chrome')
    autogui.press('enter')
    autogui.write(url)
    autogui.press('enter')
    time.sleep(Config.PAGE_LOAD_DELAY)


def perform_login(email: str, password: str, email_position: Tuple[int, int]) -> None:
    """
    Realiza o login no sistema.
    
    Args:
        email: Email para login
        password: Senha para login
        email_position: Posição do campo de email na tela
    """
    autogui.click(x=email_position[0], y=email_position[1])
    autogui.write(email)
    
    autogui.press('tab')
    autogui.write(password)
    
    autogui.press('tab')
    autogui.press('enter')
    time.sleep(Config.PAGE_LOAD_DELAY)


def load_products_data(file_path: str) -> pd.DataFrame:
    """
    Carrega os dados dos produtos do arquivo CSV.
    
    Args:
        file_path: Caminho para o arquivo CSV
        
    Returns:
        DataFrame com os dados dos produtos
    """
    return pd.read_csv(file_path)


def extract_product_data(row: pd.Series) -> Dict[str, str]:
    """
    Extrai e converte os dados de um produto para string.
    
    Args:
        row: Linha do DataFrame com os dados do produto
        
    Returns:
        Dicionário com os dados do produto convertidos para string
    """
    return {
        'codigo': str(row['codigo']),
        'marca': str(row['marca']),
        'tipo': str(row['tipo']),
        'categoria': str(row['categoria']),
        'preco_unitario': str(row['preco_unitario']),
        'custo': str(row['custo']),
        'obs': str(row['obs'])
    }


def fill_product_form(product_data: Dict[str, str], code_field_position: Tuple[int, int]) -> None:
    """
    Preenche o formulário com os dados de um produto.
    
    Args:
        product_data: Dicionário com os dados do produto
        code_field_position: Posição do primeiro campo na tela
    """
    autogui.click(x=code_field_position[0], y=code_field_position[1])
    
    fields_sequence = ['codigo', 'marca', 'tipo', 'categoria', 'preco_unitario', 'custo']
    
    for field in fields_sequence:
        autogui.write(product_data[field])
        autogui.press('tab')
    
    if product_data['obs'] != 'nan':
        autogui.write(product_data['obs'])
    
    autogui.press('tab')
    autogui.press('enter')
    autogui.scroll(Config.SCROLL_AMOUNT)


def process_all_products(products_df: pd.DataFrame) -> None:
    """
    Processa todos os produtos da planilha.
    
    Args:
        products_df: DataFrame com todos os produtos
    """
    for index in products_df.index:
        product_row = products_df.loc[index]
        product_data = extract_product_data(product_row)
        fill_product_form(product_data, Config.PRODUCT_CODE_FIELD_POSITION)


def main() -> None:
    """Função principal que executa todo o fluxo da automação."""
    try:
        setup_automation()

        open_browser_and_navigate(Config.LOGIN_URL)
        perform_login(Config.EMAIL, Config.PASSWORD, Config.EMAIL_FIELD_POSITION)
        
        products_df = load_products_data(Config.PRODUCTS_CSV_FILE)
        process_all_products(products_df)
        
        print("Automação concluída com sucesso!")
        
    except Exception as error:
        print(f"Erro durante a execução: {error}")


if __name__ == "__main__":  
    main()
    