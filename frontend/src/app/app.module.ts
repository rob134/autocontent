import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { ReactiveFormsModule, FormsModule } from '@angular/forms';

import { AppComponent } from './app.component';
import { DashboardComponent } from './components/dashboard/dashboard.component';
import { ChannelListComponent } from './components/channel-list/channel-list.component';
import { ChannelFormComponent } from './components/channel-form/channel-form.component';
import { PipelineRunnerComponent } from './components/pipeline-runner/pipeline-runner.component';
import { LogsViewerComponent } from './components/logs-viewer/logs-viewer.component';

@NgModule({
  declarations: [
    AppComponent,
    DashboardComponent,
    ChannelListComponent,
    ChannelFormComponent,
    PipelineRunnerComponent,
    LogsViewerComponent,
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    ReactiveFormsModule,
    FormsModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
