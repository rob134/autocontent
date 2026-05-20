# AutoContent — Plano de ação (SaaS com IA em Python + Orquestração Java)

## Objetivo
Entregar 3 trilhas obrigatórias:
1. **Search & Edit**: minerar vídeos ranqueados por intenção/contexto do prompt e gerar cortes estratégicos.
2. **Upload Only**: subir vídeo existente com automação de agenda e publicação multi-rede.
3. **Generative Create**: gerar vídeo por APIs externas e publicar automaticamente.

## Arquitetura-alvo
- **Frontend (Angular)**: UX conversacional clean (estilo chat) com poucos cliques.
- **IA (Python/FastAPI)**: entendimento semântico, rankeamento, extração de highlights, metadata e geração de roteiro.
- **Orquestração (Java/Spring Boot)**: fila e estado de jobs, publicação de eventos em Kafka, coordenação assíncrona.
- **Mensageria (Kafka)**: tópicos `pipeline.intent`, `pipeline.step.completed`, `pipeline.publish.request`.
- **Execução escalável (Kubernetes)**: workers por tipo de etapa (discovery, clipping, generation, publish).

## Algoritmo MVP de mineração/ranqueamento (Search & Edit)
Score final por vídeo candidato:

`score = 0.35*relevancia_semantica + 0.25*engajamento_normalizado + 0.20*retencao_estimada + 0.10*recencia + 0.10*adequacao_nicho`

- **Relevância semântica**: embedding(prompt) x embedding(título+descrição+transcrição).
- **Engajamento normalizado**: views/hour, like ratio, comentário ratio (z-score por nicho).
- **Retenção estimada**: proxies por duração, watch-time disponível e padrões do canal.
- **Recência**: decaimento temporal com meia-vida por nicho.
- **Adequação ao nicho**: classificação do conteúdo por taxonomia interna.

## Segurança e chaves/API
- Este repositório **não deve** incluir segredos reais.
- Use `.env`/secret manager para chaves de YouTube, TikTok, Instagram, OpenAI, Gemini etc.
- Em produção: Kubernetes Secrets + rotação de credenciais.

## Como rodar localmente
```bash
docker compose up --build
```
Serviços:
- Frontend: http://localhost:4200
- Python API: http://localhost:8000/docs
- Java Orchestrator: http://localhost:8080
- Kafka: localhost:9092

## Caminho SaaS (próximos passos)
1. Multi-tenant (org_id em todas entidades + RBAC).
2. OAuth por plataforma e refresh token manager.
3. Billing + limites por plano.
4. Observabilidade (OpenTelemetry + Prometheus + Grafana).
5. Deploy GitOps em Kubernetes (HPA por fila e por tipo de worker).
