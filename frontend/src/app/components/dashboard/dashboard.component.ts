import { Component } from '@angular/core';
import { PipelineService } from '../../services/pipeline.service';

interface ChatMessage {
  role: 'user' | 'assistant';
  content: string;
  meta?: string[];
}

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent {
  prompt = '';
  loading = false;
  error = '';

  messages: ChatMessage[] = [
    {
      role: 'assistant',
      content: 'Olá! Descreva o tipo de vídeo que você quer. Eu organizo em 3 fluxos: buscar+editar, upload direto ou geração por API.',
      meta: [
        'Fluxo 1: Busca semântica + cortes estratégicos',
        'Fluxo 2: Upload próprio + distribuição automática',
        'Fluxo 3: Geração por API + pós-produção + postagem'
      ]
    }
  ];

  constructor(private pipelineService: PipelineService) {}

  sendPrompt(): void {
    const clean = this.prompt.trim();
    if (!clean || this.loading) return;

    this.messages.push({ role: 'user', content: clean });
    this.prompt = '';
    this.loading = true;
    this.error = '';

    this.pipelineService.planWithAssistant({ message: clean }).subscribe({
      next: (response) => {
        this.messages.push({
          role: 'assistant',
          content: `Entendi. Intenção detectada: ${response.intent}.\n${response.reasoning}`,
          meta: response.suggested_steps
        });
        this.loading = false;
      },
      error: () => {
        this.error = 'Falha ao consultar o assistente de pipeline.';
        this.loading = false;
      }
    });
  }
}
