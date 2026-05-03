import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Channel } from '../models/types';

@Injectable({
  providedIn: 'root'
})
export class ChannelService {
  private apiUrl = 'http://localhost:8000/api/v1/channels';

  constructor(private http: HttpClient) { }

  createChannel(channel: { name: string; platform: string; mode: string }): Observable<Channel> {
    return this.http.post<Channel>(this.apiUrl, channel);
  }

  listChannels(): Observable<{ channels: Channel[]; total: number }> {
    return this.http.get<{ channels: Channel[]; total: number }>(this.apiUrl);
  }

  getChannel(id: number): Observable<Channel> {
    return this.http.get<Channel>(`${this.apiUrl}/${id}`);
  }

  updateChannel(id: number, update: any): Observable<Channel> {
    return this.http.patch<Channel>(`${this.apiUrl}/${id}`, update);
  }

  deleteChannel(id: number): Observable<any> {
    return this.http.delete(`${this.apiUrl}/${id}`);
  }
}
