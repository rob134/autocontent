import { Component, Input } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Channel, Pipeline, PipelineLog } from '../../models/types';
import { PipelineService } from '../../services/pipeline.service';

@Component({
  selector: 'app-pipeline-runner',
  templateUrl: './pipeline-runner.component.html',
  styleUrls: ['./pipeline-runner.component.css']
})
export class PipelineRunnerComponent {
  @Input() channels: Channel[] = [];

  form: FormGroup;
  loading: boolean = false;
  currentPipeline: Pipeline | null = null;
  logs: PipelineLog[] = [];
  error: string = '';

  constructor(
    private fb: FormBuilder,
    private pipelineService: PipelineService
  ) {
    this.form = this.fb.group({
      channel_id: ['', [Validators.required]],
      mode: ['curated', [Validators.required]],
      content_keyword: [''],
    });
  }

  onSubmit(): void {
    if (!this.form.valid) {
      this.error = 'Please select a channel';
      return;
    }

    this.loading = true;
    this.error = '';
    this.logs = [];

    this.pipelineService.runPipeline(this.form.value).subscribe(
      (pipeline) => {
        this.currentPipeline = pipeline;
        this.fetchLogs();
      },
      (err) => {
        this.error = err.error?.detail || 'Failed to run pipeline';
        this.loading = false;
      }
    );
  }

  fetchLogs(): void {
    if (!this.currentPipeline) return;

    this.pipelineService.getPipelineLogs(this.currentPipeline.id).subscribe(
      (data) => {
        this.logs = data.logs;

        // Poll for updates if still running
        if (this.currentPipeline?.status === 'running') {
          setTimeout(() => this.fetchPipelineStatus(), 2000);
        } else {
          this.loading = false;
        }
      },
      (err) => {
        console.error('Failed to fetch logs', err);
      }
    );
  }

  fetchPipelineStatus(): void {
    if (!this.currentPipeline) return;

    this.pipelineService.getPipeline(this.currentPipeline.id).subscribe(
      (pipeline) => {
        this.currentPipeline = pipeline;
        this.fetchLogs();
      },
      (err) => {
        console.error('Failed to fetch pipeline status', err);
      }
    );
  }
}
