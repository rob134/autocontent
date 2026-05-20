package com.autocontent.orchestrator.service;

import com.autocontent.orchestrator.model.PipelineIntentRequest;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.stereotype.Service;

@Service
public class PipelineWorkers {
    private static final Logger log = LoggerFactory.getLogger(PipelineWorkers.class);
    private final KafkaTemplate<String, String> kafkaTemplate;

    public PipelineWorkers(KafkaTemplate<String, String> kafkaTemplate) {
        this.kafkaTemplate = kafkaTemplate;
    }

    @KafkaListener(topics = "pipeline.intent", groupId = "autocontent-discovery")
    public void discoveryWorker(PipelineIntentRequest request) {
        log.info("DISCOVERY worker received mode={} prompt={}", request.mode(), request.prompt());
        kafkaTemplate.send("pipeline.step.completed", "discovery", "ok");
    }

    @KafkaListener(topics = "pipeline.step.completed", groupId = "autocontent-compose")
    public void composeWorker(String event) {
        log.info("COMPOSE worker received event={}", event);
        kafkaTemplate.send("pipeline.publish.request", "publish", "ready");
    }

    @KafkaListener(topics = "pipeline.publish.request", groupId = "autocontent-publish")
    public void publishWorker(String event) {
        log.info("PUBLISH worker received event={}", event);
    }
}
