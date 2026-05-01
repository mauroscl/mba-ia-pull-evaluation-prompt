# Pull, Otimização e Avaliação de Prompts com LangChain e LangSmith

## 📋 Visão Geral

Este projeto implementa um pipeline completo de otimização de prompts utilizando LangChain e LangSmith. O objetivo é transformar prompts de baixa qualidade (v1) em prompts otimizados (v2) que atendem critérios rigorosos de qualidade através de métricas customizadas.

**Objetivo Final:** Atingir score mínimo de **0.9 (90%)** em TODAS as métricas de avaliação.

---

## 🎯 Fluxo do Projeto

```
1. Pull Prompts (v1) → 2. Análise → 3. Refatoração (v2) → 4. Push → 5. Avaliação → 6. Iteração
   (LangSmith)         (Baixa Q.)    (Otimização)      (LS)      (Métricas)      (até 0.9)
```

---

## 🔧 Técnicas Aplicadas (Fase 2)

### Descrição das Técnicas Utilizadas

| Técnica | Descrição | Por Quê? | Exemplo Aplicado |
|---------|-----------|---------|------------------|
| **Few-Shot Learning** | [DESCREVER: Incluir 2-3 exemplos claros de entrada/saída no prompt] | [JUSTIFICAR: Melhora drasticamente a compreensão do modelo sobre o padrão esperado] | [LINK/DESCRIÇÃO dos exemplos adicionados ao v2] |
| **[TÉCNICA 2]** | [Chain of Thought / Tree of Thought / Skeleton of Thought / ReAct / Role Prompting] | [JUSTIFICAR: Por que escolheu esta técnica específica?] | [EXEMPLO: Como aplicou no prompt?] |
| **[TÉCNICA 3 - OPCIONAL]** | [Se aplicável, adicione uma 3ª técnica] | [JUSTIFICAR] | [EXEMPLO] |

### Detalhamento das Técnicas

#### 1. **Few-Shot Learning (OBRIGATÓRIO)**

**O que foi feito:**
- [TODO: Descrever os exemplos que você adicionou]
- Número de exemplos: [X]
- Cobertura de cenários: [Simples / Médio / Complexo]

**Exemplos adicionados no prompt v2:**
```yaml
# [TODO: Adicionar exemplos específicos do arquivo bug_to_user_story_v2.yml]
```

**Impacto esperado:** Clareza no formato esperado, redução de ambiguidade

---

#### 2. **[TÉCNICA ADICIONAL - Ex: Chain of Thought]**

**O que foi feito:**
- [TODO: Descrever como aplicou a técnica]
- Instruções adicionadas: [CITAR TRECHOS]

**Como foi aplicado:**
```yaml
# [TODO: Exemplos do prompt v2]
```

**Impacto esperado:** [EXPLICAR O IMPACTO]

---

### Comparativo: v1 vs v2

#### Prompt v1 (Baixa Qualidade)
```yaml
# [TODO: Incluir trecho do arquivo prompts/bug_to_user_story_v1.yml]
```

**Problemas identificados:**
- [ ] Falta de especificidade nas instruções
- [ ] Ausência de exemplos (Few-shot)
- [ ] Persona não definida
- [ ] Sem estrutura clara de saída
- [ ] Não menciona tratamento de edge cases

---

#### Prompt v2 (Otimizado)
```yaml
# [TODO: Incluir trecho do arquivo prompts/bug_to_user_story_v2.yml]
```

**Melhorias implementadas:**
- ✅ Instruções claras e específicas
- ✅ Exemplos de entrada/saída (Few-shot)
- ✅ Persona bem definida (Role Prompting)
- ✅ Estrutura explícita de saída
- ✅ Tratamento de edge cases documentado
- ✅ [TODO: Adicione outras melhorias específicas]

---

## 📊 Resultados Finais

### Métricas de Avaliação

#### Avaliação Prompt v1 (Baseline)
```
Prompt: {seu_username}/bug_to_user_story_v1
==================================================
Métricas Derivadas:
  - Helpfulness: [TODO: 0.XX] ✗
  - Correctness: [TODO: 0.XX] ✗

Métricas Base:
  - F1-Score: [TODO: 0.XX] ✗
  - Clarity: [TODO: 0.XX] ✗
  - Precision: [TODO: 0.XX] ✗

❌ STATUS: REPROVADO
```

---

#### Avaliação Prompt v2 (Otimizado)
```
Prompt: {seu_username}/bug_to_user_story_v2
==================================================
Métricas Derivadas:
  - Helpfulness: [TODO: ≥0.90] ✅
  - Correctness: [TODO: ≥0.90] ✅

Métricas Base:
  - F1-Score: [TODO: ≥0.90] ✅
  - Clarity: [TODO: ≥0.90] ✅
  - Precision: [TODO: ≥0.90] ✅

✅ STATUS: APROVADO - Todas as métricas >= 0.9
```

**Iterações realizadas:** [TODO: Número de iterações até atingir 0.9 em todas]

---

### Tabela Comparativa

| Métrica | v1 | v2 | Melhoria | Status |
|---------|-----|------|---------|--------|
| Helpfulness | [TODO] | [TODO] | [TODO: +X%] | ❌/✅ |
| Correctness | [TODO] | [TODO] | [TODO: +X%] | ❌/✅ |
| F1-Score | [TODO] | [TODO] | [TODO: +X%] | ❌/✅ |
| Clarity | [TODO] | [TODO] | [TODO: +X%] | ❌/✅ |
| Precision | [TODO] | [TODO] | [TODO: +X%] | ❌/✅ |
| **MÉDIA** | [TODO] | [TODO] | [TODO: +X%] | ❌/✅ |

---

### Dashboard LangSmith

**Link público do dashboard:** [TODO: Adicione o link público do seu LangSmith com as avaliações]

**Screenshots de evidência:**

1. **Visão geral das avaliações (v2):**
   - [TODO: Adicione screenshot mostrando os scores ≥ 0.9]

2. **Dataset com 15 exemplos:**
   - [TODO: Adicione screenshot do dataset bug_to_user_story.jsonl no LangSmith]

3. **Tracing detalhado (exemplo 1):**
   - [TODO: Adicione screenshot do tracing de 1 execução bem-sucedida]

4. **Tracing detalhado (exemplo 2):**
   - [TODO: Adicione screenshot do tracing de outra execução]

5. **Tracing detalhado (exemplo 3):**
   - [TODO: Adicione screenshot do tracing de uma terceira execução]

---

## 🚀 Como Executar

### Pré-requisitos

- **Python 3.9+** instalado
- **Git** instalado
- Conta no **LangSmith** (https://smith.langchain.com)
- API Keys:
  - OpenAI: https://platform.openai.com/api-keys (OU)
  - Google Gemini: https://aistudio.google.com/app/apikey

### 1. Clonar o Repositório

```bash
git clone https://github.com/{seu_username}/mba-ia-pull-evaluation-prompt.git
cd mba-ia-pull-evaluation-prompt
```

### 2. Criar e Ativar Ambiente Virtual

```bash
# Criar ambiente virtual
python3 -m venv venv

# Ativar (Linux/macOS)
source venv/bin/activate

# Ativar (Windows)
venv\Scripts\activate
```

### 3. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar Variáveis de Ambiente

Crie um arquivo `.env` baseado em `.env.example`:

```bash
cp .env.example .env
```

Edite `.env` e adicione suas credenciais:

```env
# LangSmith
LANGSMITH_API_KEY=your_langsmith_api_key
LANGSMITH_PROJECT=your_project_name
LANGSMITH_ENDPOINT=https://api.smith.langchain.com

# OpenAI (escolha uma opção)
OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL_RESPONSE=gpt-4o-mini
OPENAI_MODEL_EVAL=gpt-4o

# OU Google Gemini
GOOGLE_API_KEY=your_google_api_key
GEMINI_MODEL=gemini-2.5-flash
```

### 5. Executar o Pipeline Completo

#### Passo 1: Pull dos Prompts Iniciais

```bash
python src/pull_prompts.py
```

**Saída esperada:**
- Arquivo `prompts/bug_to_user_story_v1.yml` sincronizado do LangSmith

#### Passo 2: Refatorar o Prompt (Manual)

Edite o arquivo `prompts/bug_to_user_story_v2.yml` com suas otimizações:

```bash
# Abra o arquivo com seu editor
code prompts/bug_to_user_story_v2.yml
```

**Checklist de otimização:**
- ✅ Few-Shot Learning: Mínimo 2-3 exemplos
- ✅ Persona definida (Role Prompting)
- ✅ Instruções específicas e claras
- ✅ Estrutura de saída explícita
- ✅ Tratamento de edge cases

#### Passo 3: Fazer Push dos Prompts Otimizados

```bash
python src/push_prompts.py
```

**Saída esperada:**
```
✅ Prompt enviado para LangSmith: {seu_username}/bug_to_user_story_v2
📍 URL: https://smith.langchain.com/hub/{seu_username}/bug_to_user_story_v2
```

#### Passo 4: Avaliar os Prompts

```bash
python src/evaluate.py
```

**Saída esperada:**
```
Executando avaliação dos prompts...
==================================================
Prompt: {seu_username}/bug_to_user_story_v2
==================================================

Métricas Derivadas:
  - Helpfulness: 0.94 ✓
  - Correctness: 0.96 ✓

Métricas Base:
  - F1-Score: 0.93 ✓
  - Clarity: 0.95 ✓
  - Precision: 0.92 ✓

✅ STATUS: APROVADO - Todas as métricas >= 0.9
```

### 6. Executar Testes de Validação

```bash
# Rodar todos os testes
pytest tests/test_prompts.py -v

# Rodar teste específico
pytest tests/test_prompts.py::test_prompt_has_few_shot_examples -v
```

**Testes implementados:**
- `test_prompt_has_system_prompt`: Verifica se o system prompt existe e não está vazio
- `test_prompt_has_role_definition`: Verifica se a persona está definida
- `test_prompt_mentions_format`: Verifica se o formato de saída está especificado
- `test_prompt_has_few_shot_examples`: Verifica se há exemplos (Few-shot)
- `test_prompt_no_todos`: Garante que não há `[TODO]` deixados no arquivo
- `test_minimum_techniques`: Verifica se pelo menos 2 técnicas estão listadas nos metadados

---

## 📁 Estrutura do Projeto

```
mba-ia-pull-evaluation-prompt/
│
├── README.md                          # Este arquivo
├── .env.example                       # Template de variáveis de ambiente
├── requirements.txt                   # Dependências Python
│
├── prompts/
│   ├── bug_to_user_story_v1.yml       # Prompt inicial (baixa qualidade)
│   ├── bug_to_user_story_v2.yml       # Prompt otimizado (implementar)
│   └── original_bug_to_user_story_v1.yml  # Backup do original
│
├── datasets/
│   └── bug_to_user_story.jsonl        # 15 exemplos de bugs para avaliação
│
├── src/
│   ├── __init__.py
│   ├── pull_prompts.py                # Script para fazer pull do LangSmith
│   ├── push_prompts.py                # Script para fazer push ao LangSmith
│   ├── evaluate.py                    # Pipeline de avaliação
│   ├── metrics.py                     # Implementação das 5 métricas
│   └── utils.py                       # Funções auxiliares
│
└── tests/
    ├── __init__.py
    └── test_prompts.py                # Testes de validação (implementar)
```

---

## 🔄 Processo Iterativo

Se as métricas não atingirem 0.9 em todas as dimensões:

### Iteração N

1. **Analisar falhas:**
   ```bash
   # Verifique no dashboard do LangSmith qual métrica falhou
   # Use o Tracing para entender o problema
   ```

2. **Editar e melhorar:**
   ```bash
   # Edite prompts/bug_to_user_story_v2.yml
   code prompts/bug_to_user_story_v2.yml
   ```

3. **Fazer novo push:**
   ```bash
   python src/push_prompts.py
   ```

4. **Reavaliar:**
   ```bash
   python src/evaluate.py
   ```

5. **Repetir** até atingir 0.9 em todas as métricas

**Dica:** Chain of Thought (CoT) costuma ser muito efetivo para tarefas de análise e raciocínio complexo como conversão de bugs para user stories.

---

## 📚 Recursos Úteis

- **LangSmith Docs:** https://docs.smith.langchain.com/
- **Prompt Engineering Guide:** https://www.promptingguide.ai/
- **LangChain Hub:** https://smith.langchain.com/hub
- **OpenAI API:** https://platform.openai.com/docs
- **Google Gemini API:** https://ai.google.dev/

---

## ✅ Checklist de Entrega

- [ ] Repositório é um fork público no GitHub
- [ ] Arquivo `prompts/bug_to_user_story_v2.yml` completamente preenchido
- [ ] Script `src/pull_prompts.py` implementado e funcional
- [ ] Script `src/push_prompts.py` implementado e funcional
- [ ] Testes em `tests/test_prompts.py` todos passando
- [ ] README.md preenchido com:
  - [ ] Técnicas aplicadas com justificativa
  - [ ] Comparativo v1 vs v2
  - [ ] Link público do LangSmith
  - [ ] Screenshots das avaliações (≥ 0.9)
  - [ ] Instruções de execução
- [ ] Todas as 5 métricas ≥ 0.9
- [ ] Link público do prompt v2 no LangSmith

---

## 🎓 Notas Adicionais

- **Não altere** `src/evaluate.py`, `src/metrics.py`, `src/utils.py` ou `datasets/`
- **Documente seu processo** - a jornada é tão importante quanto o resultado
- **Itere com propósito** - analise as métricas antes de cada mudança
- **Use o Tracing do LangSmith** como ferramenta de debug principal
- **Few-Shot Learning é obrigatório** - mínimo 2-3 exemplos bem estruturados

---

## 📧 Suporte

Para dúvidas, consulte a documentação do LangSmith ou a seção "Dicas Finais" no DESAFIO.md.

---

**Data de última atualização:** [TODO: Adicione a data]
**Status:** [TODO: Em andamento / Concluído]
