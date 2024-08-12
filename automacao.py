import pyautogui
from time import sleep
import logging
import os

# Configurações de log
logging.basicConfig(filename='automacao.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Parâmetros de configuração
usuario = 'marcosv'
senha = 'p48z4h'
endereco_balanca = '\\\\192.168.1.210\\Toledo Carga\\'
endereco_tela = '\\\\192.168.1.246\\Toledo Carga\\'
produto_base = '1367'
valor = '7,50'
descricao = '%'

# Funções utilitárias
def clicar(x, y, duracao=2):
    try:
        pyautogui.click(x, y, duration=duracao)
        logging.info(f"Clicou na posição ({x}, {y}) com duração de {duracao} segundos.")
    except Exception as e:
        logging.error(f"Erro ao clicar na posição ({x}, {y}): {e}")

def escrever(texto):
    try:
        pyautogui.write(texto)
        logging.info(f"Escreveu o texto: {texto}")
    except Exception as e:
        logging.error(f"Erro ao escrever o texto: {texto} - {e}")
        
def pressionar_enter():
    try:
        pyautogui.press('enter')
        logging.info("Pressionou a tecla Enter.")
    except Exception as e:
        logging.error(f"Erro ao pressionar a tecla Enter: {e}")


# INÍCIO EXECUÇÃO
try:
    logging.info("Início da execução do script.")

     # Abre aplicativo (VRMASTER) com clique duplo
    pyautogui.doubleClick(43,362, duration=2)
    logging.info("Aplicativo VRMASTER aberto com clique duplo.")
    
    # Insere usuário
    clicar(524, 388, duracao=5)
    escrever(usuario)
    
    # Insere senha
    clicar(527, 435, duracao=1)
    escrever(senha)
    
    # Confirma
    clicar(592, 480, duracao=1)
    
    # CARGA PARA AS BALANÇAS
    clicar(656, 11, duracao=6)  # Vai no menu e seleciona Interface
    clicar(682, 39, duracao=1)  # Vai no submenu e seleciona Exportação
    clicar(765, 52, duracao=1)  # Vai no submenu e seleciona Balança
    clicar(876, 78, duracao=1)  # Vai no menu e seleciona Toledo
    clicar(813, 411, duracao=1)  # Desce o mouse e clica em Exportar
    clicar(718, 478, duracao=10)  # Aguarda exportação e aperta OK
    clicar(702, 366, duracao=1)  # Clica na aba endereço
    escrever(endereco_balanca)   # Insere novo endereço
    clicar(813, 411, duracao=1.5)  # Desce o mouse e clica em Exportar
    clicar(720,481, duracao=8)  # Aguarda exportação e aperta OK
    clicar(916,273 , duracao=1)  # Clica em fechar guia de exportação Balança
    
    # CARGA PARA AS TELAS
    clicar(656, 11, duracao=1)  # Vai no menu e seleciona Interface
    clicar(682, 39, duracao=1)  # Vai no submenu e seleciona Exportação
    clicar(778, 30, duracao=1)  # Vai no submenu e seleciona arquivo
    clicar(24, 103, duracao=1)  # Desce e clica em Consultar
    clicar(35, 255, duracao=1)  # Desce e seleciona OFERTA
    clicar(115, 105, duracao=1)  # Sobe e clica em Exportar
    clicar(621, 366, duracao=1)  # Clica na aba endereço
    escrever(endereco_tela)      # Insere novo endereço
    clicar(771, 405, duracao=1.5)  # Clica em Exportar
    clicar(717, 478, duracao=5)  # Aguarda exportação e aperta OK
    clicar(1425, 78, duracao=1)  # Clica em fechar guia de exportação Arquivo

    #PRECIFICAÇÃO ECOMMERCE
    clicar(15, 43, duracao=1)  # Vai em Administração de Preço
    clicar(291, 146, duracao=1.5)  # Vai na barra produto
    escrever(produto_base)  # Insere código do produto base
    pressionar_enter() # Pressiona enter
    clicar(557, 104, duracao=1)  #  Clica em Administração de Preço da Loja Virtual
    clicar(59, 154, duracao=1)  # Clica em Lote
    clicar(713, 287, duracao=1)  # Clica em Valor
    escrever(valor) #Insere Valor Loja Virtual
    pressionar_enter() # Pressiona enter
    clicar(813, 536, duracao=1.5)  # Clica em incluir
    clicar(40, 168, duracao=1.5)  # Clica em Descrição
    escrever(descricao)
    clicar(27, 105, duracao=1)  # Clica em Consultar
    clicar(21, 203, duracao=8)  # Clica em Selecionar Todos
    clicar(85, 101, duracao=1.5)  # Clica em Carregar
    clicar(773, 566, duracao=6)  # Clica em Salvar
    clicar(718, 481, duracao=50)  # Aguarda e clica em OK
    clicar(870, 189, duracao=1)  # Clica em fechar guia de Lote de Admin de preço de Lj Virt
    clicar(604, 129, duracao=1)  # Clica em fechar guia Adm de Preço Lj Virt
    clicar(1260, 78, duracao=1)  # Clica em fechar guia Adm Preço
    
    # Fecha aplicativo
    clicar(1420, 6, duracao=1)  # Clica em fechar aplicativo
    clicar(696, 480, duracao=1)  # Clica em SIM

    logging.info("Execução do script finalizada com sucesso.")
    
except Exception as e:
    logging.error(f"Ocorreu um erro durante a execução do script: {e}")
finally:
    logging.info("Fim da execução.")
