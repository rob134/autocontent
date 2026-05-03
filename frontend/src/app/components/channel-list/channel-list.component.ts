import { Component, Input, Output, EventEmitter } from '@angular/core';
import { Channel } from '../../models/types';

@Component({
  selector: 'app-channel-list',
  templateUrl: './channel-list.component.html',
  styleUrls: ['./channel-list.component.css']
})
export class ChannelListComponent {
  @Input() channels: Channel[] = [];
  @Output() refresh = new EventEmitter<void>();

  onRefresh(): void {
    this.refresh.emit();
  }
}
