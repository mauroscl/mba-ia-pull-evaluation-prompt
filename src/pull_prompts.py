"""
Script para fazer pull de prompts do LangSmith Prompt Hub.

Este script:
1. Conecta ao LangSmith usando credenciais do .env
2. Faz pull dos prompts do Hub
3. Salva localmente em prompts/bug_to_user_story_v1.yml

SIMPLIFICADO: Usa serialização nativa do LangChain para extrair prompts.
"""

import sys
from datetime import date
from dotenv import load_dotenv
from utils import save_yaml, check_env_vars, print_section_header
from langsmith import Client
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts.chat import (
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)

load_dotenv()

client = Client()


def _safe_template_text(message) -> str:
    """Extrai texto do template sem depender de um subtipo específico de prompt."""
    prompt = getattr(message, "prompt", None)

    template = getattr(prompt, "template", None)
    if template is not None:
        return str(template)

    if isinstance(prompt, list):
        for item in prompt:
            if hasattr(item, "template"):
                return str(item.template)

    return ""


def prompt_to_yaml_dict(prompt_obj: ChatPromptTemplate, prompt_key: str) -> dict:
    """Converte o retorno de client.pull_prompt para o formato YAML esperado."""
    if not isinstance(prompt_obj, ChatPromptTemplate):
        raise TypeError("O retorno de client.pull_prompt não é ChatPromptTemplate")

    system_prompt = ""
    user_prompt = ""

    for message in prompt_obj.messages:
        print(message)
        if isinstance(message, SystemMessagePromptTemplate):
            system_prompt = _safe_template_text(message)
        elif isinstance(message, HumanMessagePromptTemplate):
            user_prompt = _safe_template_text(message)

    version = prompt_key.rsplit("_", 1)[-1] if "_" in prompt_key else "v1"

    return {
        prompt_key: {
            "description": "Prompt para converter relatos de bugs em User Stories",
            "system_prompt": system_prompt.strip(),
            "user_prompt": user_prompt.strip(),
            "version": version,
            "created_at": date.today().isoformat(),
            "tags": ["bug-analysis", "user-story", "product-management"],
        }
    }

def pull_prompts_from_langsmith():  # sourcery skip: avoid-builtin-shadow
    prompt_name = "leonanluppi/bug_to_user_story_v1"
    prompt_key = prompt_name.split("/", 1)[1]

    prompt_obj = client.pull_prompt(prompt_name)
    prompt_dict = prompt_to_yaml_dict(prompt_obj, prompt_key)

    save_yaml(prompt_dict, f"prompts/{prompt_key}.yml")


def main():
    """Função principal"""
    print_section_header("Pulling Prompts from LangSmith Prompt Hub")
    check_env_vars(["LANGSMITH_API_KEY"])
    pull_prompts_from_langsmith()
    print("Prompts pulled successfully!")


if __name__ == "__main__":
    sys.exit(main())
