import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ChannelService } from '../../services/channel.service';
import { Channel } from '../../models/types';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  activeTab: 'channels' | 'pipeline' = 'channels';
  channels: Channel[] = [];
  loading: boolean = false;
  error: string = '';

  constructor(
    private channelService: ChannelService,
    private fb: FormBuilder
  ) { }

  ngOnInit(): void {
    this.loadChannels();
  }

  loadChannels(): void {
    this.loading = true;
    this.channelService.listChannels().subscribe(
      (data) => {
        this.channels = data.channels;
        this.loading = false;
      },
      (err) => {
        this.error = 'Failed to load channels';
        this.loading = false;
        console.error(err);
      }
    );
  }

  setActiveTab(tab: 'channels' | 'pipeline'): void {
    this.activeTab = tab;
  }
}
