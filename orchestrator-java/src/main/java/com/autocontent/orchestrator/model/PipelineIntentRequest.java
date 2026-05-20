package com.autocontent.orchestrator.model;

public record PipelineIntentRequest(String prompt, String mode, Integer channelId, String sourceUrl) {}
