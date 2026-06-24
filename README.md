# 📂 File Automator

> Um script em Python moderno e Orientado a Objetos (OOP) para automatizar a organização e limpeza de diretórios.

O **File Automator** é uma ferramenta de Linha de Comando (CLI) desenvolvida para acabar com a bagunça de pastas de download e áreas de trabalho. Ele permite mover arquivos específicos para pastas organizadas ou limpar arquivos desnecessários (como `.zip`) de forma rápida e segura.

---

## ✨ Funcionalidades

* **Mover Arquivos em Massa:** Transfere todos os arquivos de uma extensão específica (ex: `.png`) para um diretório de destino.
* **Mover Arquivos Específicos:** Permite escolher nomes exatos de arquivos para serem movidos.
* **Limpeza Automática:** Deleta todos os arquivos `.zip` de uma pasta com um único comando.
* **Deleção Cirúrgica (Dry Run):** Permite deletar arquivos específicos, contando com um sistema de simulação de segurança (*Dry Run*) para você visualizar o que será apagado antes de confirmar a ação.
* **Sistema de Configuração:** Lê os caminhos das pastas diretamente de um arquivo JSON, evitando que você precise mexer no código-fonte.

---

## 🚀 Como usar

### 1. Pré-requisitos
Certifique-se de ter o **Python 3.x** instalado na sua máquina. O projeto utiliza apenas bibliotecas nativas do Python (`os`, `shutil`, `json`, `pathlib`), então **não é necessário** instalar dependências externas com o `pip`.

### 2. Configuração do Ambiente
Antes de rodar o script, você precisa dizer ao robô onde ele deve trabalhar. Crie um arquivo chamado `config.json` na mesma pasta do seu script com a seguinte estrutura:

```json
{
    "source_dir": "C:/Caminho/Para/Sua/Pasta/De/Origem",
    "dest_dir": "C:/Caminho/Para/Sua/Pasta/De/Destino"
}
