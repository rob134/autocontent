import { Component, Output, EventEmitter } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ChannelService } from '../../services/channel.service';

@Component({
  selector: 'app-channel-form',
  templateUrl: './channel-form.component.html',
  styleUrls: ['./channel-form.component.css']
})
export class ChannelFormComponent {
  @Output() created = new EventEmitter<void>();

  form: FormGroup;
  loading: boolean = false;
  error: string = '';
  success: string = '';

  constructor(
    private fb: FormBuilder,
    private channelService: ChannelService
  ) {
    this.form = this.fb.group({
      name: ['', [Validators.required]],
      platform: ['youtube', [Validators.required]],
      mode: ['curated', [Validators.required]],
    });
  }

  onSubmit(): void {
    if (!this.form.valid) {
      this.error = 'Please fill in all required fields';
      return;
    }

    this.loading = true;
    this.error = '';
    this.success = '';

    this.channelService.createChannel(this.form.value).subscribe(
      (result) => {
        this.success = `Channel "${result.name}" created successfully!`;
        this.form.reset({ platform: 'youtube', mode: 'curated' });
        this.loading = false;
        this.created.emit();
        setTimeout(() => this.success = '', 3000);
      },
      (err) => {
        this.error = err.error?.detail || 'Failed to create channel';
        this.loading = false;
      }
    );
  }
}
