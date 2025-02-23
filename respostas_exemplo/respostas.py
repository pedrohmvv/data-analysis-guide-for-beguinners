import json
import os
from IPython.display import display, Markdown

FILE_PATH = os.path.dirname(os.path.abspath(__file__))
RESPOSTAS_PATH = os.path.join(FILE_PATH, "respostas.json")

class Respostas:
    def __init__(self, arquivo_json=RESPOSTAS_PATH):
        self.arquivo_json = arquivo_json
        if not os.path.exists(arquivo_json):
            with open(arquivo_json, 'w', encoding='utf-8') as f:
                json.dump({}, f, indent=4)
        self._carregar_dados()

    def _carregar_dados(self):
        """Carrega os dados do JSON."""
        with open(self.arquivo_json, 'r', encoding='utf-8') as f:
            self.dados = json.load(f)

    def obter_resposta(self, chave):
        """Retorna a resposta formatada corretamente."""
        codigo = self.dados.get(chave, "Resposta não encontrada.")
        return codigo.replace("\\n", "\n")  # Converte '\n' em quebras de linha reais

    def salvar_resposta(self, chave, codigo):
        """Salva ou atualiza uma resposta no JSON."""
        self.dados[chave] = codigo
        with open(self.arquivo_json, 'w', encoding='utf-8') as f:
            json.dump(self.dados, f, indent=4, ensure_ascii=False)
        print(f"✅ Resposta '{chave}' salva com sucesso!")

    def mostrar_resposta_formatada(self, chave):
        """Exibe a resposta formatada como código Python."""
        codigo = self.obter_resposta(chave)
        if codigo == "Resposta não encontrada.":
            print("🔴 Resposta não encontrada para a chave:", chave)
            return
        
        display(Markdown(f"```python\n{codigo}\n```"))
