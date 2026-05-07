"""
Testes automatizados para validação de prompts.
"""
import pytest
import yaml
import sys
from pathlib import Path

# Adicionar src ao path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from utils import validate_prompt_structure

prompt_under_test = "prompts/bug_to_user_story_v2.yml"

def load_prompts(file_path: str):
    """Carrega prompts do arquivo YAML."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

class TestPrompts:
    def test_prompt_has_system_prompt(self):
        """Verifica se o campo 'system_prompt' existe e não está vazio."""
        prompt = load_prompts(prompt_under_test)  # Carrega o prompt para validação
        prompt_data = prompt.get("bug_to_user_story_v2", {})
        assert "system_prompt" in prompt_data
        assert prompt_data["system_prompt"] is not None and prompt_data["system_prompt"].strip() != ""

    def test_prompt_has_role_definition(self):
        """Verifica se o prompt define uma persona (ex: "Você é um Product Manager")."""
        prompt = load_prompts(prompt_under_test)
        prompt_data = prompt.get("bug_to_user_story_v2", {})
        assert "system_prompt" in prompt_data
        assert "Você é" in prompt_data["system_prompt"]

    def test_prompt_mentions_format(self):
        """Verifica se o prompt exige formato Markdown ou User Story padrão."""
        prompt = load_prompts(prompt_under_test)
        prompt_data = prompt.get("bug_to_user_story_v2", {})
        assert "system_prompt" in prompt_data
        assert "User Story Template" in prompt_data["system_prompt"]
        assert "Como [Ator]" in prompt_data["system_prompt"]

    def test_prompt_has_few_shot_examples(self):
        """Verifica se o prompt contém exemplos de entrada/saída (técnica Few-shot)."""
        prompt = load_prompts(prompt_under_test)
        prompt_data = prompt.get("bug_to_user_story_v2", {})
        assert "system_prompt" in prompt_data
        assert "Exemplos:" in prompt_data["system_prompt"]
        assert "Como um" in prompt_data["system_prompt"]

    def test_prompt_no_todos(self):
        """Garante que você não esqueceu nenhum `[TODO]` no texto."""
        prompt = load_prompts(prompt_under_test)
        prompt_data = prompt.get("bug_to_user_story_v2", {})
        assert "[TODO]" not in prompt_data["system_prompt"]

    def test_minimum_techniques(self):
        """Verifica (através dos metadados do yaml) se pelo menos 2 técnicas foram listadas."""
        prompt = load_prompts(prompt_under_test)
        prompt_data = prompt.get("bug_to_user_story_v2", {})
        assert "techniques" in prompt_data
        assert isinstance(prompt_data["techniques"], list)
        assert len(prompt_data["techniques"]) >= 2

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])