"""
Script para fazer push de prompts otimizados ao LangSmith Prompt Hub.

Este script:
1. Lê os prompts otimizados de prompts/bug_to_user_story_v2.yml
2. Valida os prompts
3. Faz push PÚBLICO para o LangSmith Hub
4. Adiciona metadados (tags, descrição, técnicas utilizadas)

SIMPLIFICADO: Código mais limpo e direto ao ponto.
"""

import os
import sys
from dotenv import load_dotenv
from langchain import hub
from langchain_core.prompts import ChatPromptTemplate
from utils import load_yaml, check_env_vars, print_section_header
from langsmith import Client

load_dotenv()


def push_prompt_to_langsmith(prompt_name: str, prompt_data: dict) -> bool:
    """
    Faz push do prompt otimizado para o LangSmith Hub (PÚBLICO).

    Args:
        prompt_name: Nome do prompt
        prompt_data: Dados do prompt

    Returns:
        True se sucesso, False caso contrário
    """
    try:
        client = Client()
        prompt_content = prompt_data.get("bug_to_user_story_v2", {})
        url = client.push_prompt(
            "bug_to_user_story_v2",
            object=ChatPromptTemplate.from_messages(
                [
                    ("system", prompt_content.get("system_prompt", "")),
                    ("user", prompt_content.get("user_prompt", "")),
                ]
            ),
            is_public=True,
            tags=prompt_content.get("tags", []),
            description=prompt_content.get("description"),
        )
        print(url)
        print(f"✅ Prompt '{prompt_name}' publicado com sucesso!")
        return True
    except Exception as e:
        print(f"❌ Erro ao publicar o prompt: {e}")
        return False


def validate_prompt(prompt_data: dict) -> tuple[bool, list]:
    """
    Valida estrutura básica de um prompt (versão simplificada).

    Args:
        prompt_data: Dados do prompt

    Returns:
        (is_valid, errors) - Tupla com status e lista de erros
    """
    errors = []

    prompt_content = prompt_data.get("bug_to_user_story_v2") or {}
    if not prompt_content.get("system_prompt"):
        errors.append("Campo 'system_prompt' é obrigatório e não pode ser vazio.")
    if not prompt_content.get("user_prompt"):
        errors.append("Campo 'user_prompt' é obrigatório e não pode ser vazio.")

    return not errors, errors


def main():
    """Função principal"""
    check_env_vars(["USERNAME_LANGSMITH_HUB"])

    prompt_template = load_yaml("prompts/bug_to_user_story_v2.yml")

    if not prompt_template:
        print("❌ Falha ao carregar o prompt otimizado.")
        return False

    is_valid, errors = validate_prompt(prompt_template)
    if not is_valid:
        print("❌ Erros de validação encontrados:")
        for error in errors:
            print(f"  - {error}")
        return False

    push_prompt_to_langsmith("mauroscl/bug_to_user_story_v2", prompt_template)


if __name__ == "__main__":
    sys.exit(main())
