import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Pipeline, PipelineLog } from '../models/types';

@Injectable({
  providedIn: 'root'
})
export class PipelineService {
  private apiUrl = 'http://localhost:8000/api/v1/pipeline';

  constructor(private http: HttpClient) { }

  runPipeline(request: {
    channel_id: number;
    mode: string;
    content_keyword?: string;
    source_url?: string;
  }): Observable<Pipeline> {
    return this.http.post<Pipeline>(`${this.apiUrl}/run`, request);
  }

  getPipeline(id: number): Observable<any> {
    return this.http.get<any>(`${this.apiUrl}/${id}`);
  }

  getPipelineLogs(id: number): Observable<{ pipeline_id: number; logs: PipelineLog[] }> {
    return this.http.get<{ pipeline_id: number; logs: PipelineLog[] }>(
      `http://localhost:8000/api/v1/logs/${id}`
    );
  }
}
