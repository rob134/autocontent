package com.autocontent.orchestrator.api;

import com.autocontent.orchestrator.model.PipelineIntentRequest;
import com.autocontent.orchestrator.service.OrchestrationService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/v1/orchestrator")
public class OrchestrationController {
    private final OrchestrationService service;

    public OrchestrationController(OrchestrationService service) {
        this.service = service;
    }

    @PostMapping("/enqueue")
    public ResponseEntity<String> enqueue(@RequestBody PipelineIntentRequest request) {
        service.enqueue(request);
        return ResponseEntity.accepted().body("queued");
    }
}
