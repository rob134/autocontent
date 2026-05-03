export interface Channel {
  id: number;
  name: string;
  platform: string;
  mode: 'curated' | 'avatar' | 'ads';
  is_active: boolean;
  created_at: string;
  updated_at: string;
}

export interface Pipeline {
  id: number;
  channel_id: number;
  status: 'pending' | 'running' | 'completed' | 'failed';
  mode: 'curated' | 'avatar' | 'ads';
  content_keyword?: string;
  generated_title?: string;
  generated_description?: string;
  error_message?: string;
  created_at: string;
}

export interface PipelineLog {
  id: number;
  step: string;
  level: 'INFO' | 'WARNING' | 'ERROR' | 'DEBUG';
  message: string;
  created_at: string;
}
