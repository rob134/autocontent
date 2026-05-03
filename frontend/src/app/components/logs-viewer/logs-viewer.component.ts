import { Component, Input } from '@angular/core';
import { PipelineLog } from '../../models/types';

@Component({
  selector: 'app-logs-viewer',
  templateUrl: './logs-viewer.component.html',
  styleUrls: ['./logs-viewer.component.css']
})
export class LogsViewerComponent {
  @Input() logs: PipelineLog[] = [];

  getLogClass(level: string): string {
    return `log-${level.toLowerCase()}`;
  }

  getLogIcon(level: string): string {
    switch (level) {
      case 'ERROR': return '❌';
      case 'WARNING': return '⚠️';
      case 'INFO': return 'ℹ️';
      case 'DEBUG': return '🐛';
      default: return '•';
    }
  }
}
