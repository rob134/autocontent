package com.autocontent.orchestrator.service;

import com.autocontent.orchestrator.model.PipelineIntentRequest;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.stereotype.Service;

@Service
public class OrchestrationService {
    private final KafkaTemplate<String, PipelineIntentRequest> kafkaTemplate;

    public OrchestrationService(KafkaTemplate<String, PipelineIntentRequest> kafkaTemplate) {
        this.kafkaTemplate = kafkaTemplate;
    }

    public void enqueue(PipelineIntentRequest request) {
        kafkaTemplate.send("pipeline.intent", request.mode(), request);
    }
}
