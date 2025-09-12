## 1. Model Performance Metrics

### 1.1 Core Classification/Regression Metrics

**Classification Metrics:**
- **Accuracy**: Overall correctness ratio - `correct_predictions / total_predictions`
- **Precision**: True positives ratio - `TP / (TP + FP)` - measures false positive control
- **Recall (Sensitivity)**: True positive rate - `TP / (TP + FN)` - measures false negative control
- **F1 Score**: Harmonic mean of precision and recall - `2 * (precision * recall) / (precision + recall)`
- **AUC-ROC**: Area under ROC curve - measures discriminative ability across thresholds
- **Log-loss**: Cross-entropy loss - `−(1/N) * Σ[y*log(p) + (1−y)*log(1−p)]`

**Regression Metrics:**
- **MAE**: Mean Absolute Error - `(1/N) * Σ|y_true - y_pred|`
- **MSE**: Mean Squared Error - `(1/N) * Σ(y_true - y_pred)²`
- **RMSE**: Root Mean Squared Error - `√MSE`
- **R²**: Coefficient of determination - `1 - (SS_res / SS_tot)`

**Implementation Strategy:**
```python
# Example metric calculation structure
def calculate_metrics(y_true, y_pred, y_prob=None):
    metrics = {
        'timestamp': datetime.utcnow(),
        'model_version': os.environ.get('MODEL_VERSION'),
        'deployment_id': os.environ.get('DEPLOYMENT_ID'),
        'accuracy': accuracy_score(y_true, y_pred),
        'precision': precision_score(y_true, y_pred, average='weighted'),
        'recall': recall_score(y_true, y_pred, average='weighted'),
        'f1_score': f1_score(y_true, y_pred, average='weighted')
    }
    if y_prob is not None:
        metrics['auc_roc'] = roc_auc_score(y_true, y_prob)
        metrics['log_loss'] = log_loss(y_true, y_prob)
    return metrics
```

### 1.2 Operational Performance Metrics

**Latency Metrics:**
- **Prediction Latency**: Time from request receipt to response (p50, p95, p99 percentiles)
- **Queue Wait Time**: Time requests spend in processing queue
- **Model Inference Time**: Pure model computation time
- **End-to-End Latency**: Total request processing time including preprocessing/postprocessing

**Throughput & Reliability:**
- **Requests per Second (RPS)**: Current and peak throughput capacity
- **Error Rate**: Percentage of failed requests (4xx, 5xx responses)
- **Success Rate**: Percentage of successful predictions
- **Model Uptime**: Availability percentage over time windows

**Docker Container Metrics:**
```yaml
# Example Docker health check configuration
healthcheck:
  test: ["CMD", "curl", "-f", "http://localhost:8080/health"]
  interval: 30s
  timeout: 10s
  retries: 3
  start_period: 60s
```

### 1.3 Model Calibration Metrics

**Confidence Distribution Analysis:**
- **Prediction Confidence Histogram**: Distribution of model confidence scores
- **Calibration Curve**: Reliability diagram comparing predicted vs actual probabilities
- **Expected Calibration Error (ECE)**: Average difference between confidence and accuracy across bins
- **Brier Score**: Mean squared difference between predicted probabilities and binary outcomes

**Uncertainty Quantification:**
- **Epistemic Uncertainty**: Model uncertainty due to lack of knowledge
- **Aleatoric Uncertainty**: Data uncertainty inherent to the problem
- **Prediction Intervals**: Confidence bounds around predictions (for regression)

## 2. Data Quality & Drift Metrics

### 2.1 Input Data Integrity

**Schema Validation:**
- **Column Presence**: Verify all expected features are present
- **Data Type Validation**: Ensure numeric/categorical/datetime types match expectations
- **Value Range Checks**: Validate numeric features within expected bounds
- **Categorical Value Validation**: Confirm categorical features contain only valid values

**Data Quality Indicators:**
- **Missing Value Rate**: Percentage of null/NaN values per feature
- **Data Completeness**: Ratio of complete records to total records
- **Duplicate Record Rate**: Percentage of duplicate entries
- **Outlier Detection Rate**: Percentage of values beyond statistical thresholds (e.g., >3σ)

**Implementation Example:**
```python
def validate_data_quality(df, schema_config):
    quality_metrics = {
        'timestamp': datetime.utcnow(),
        'total_records': len(df),
        'complete_records': len(df.dropna()),
        'completeness_rate': len(df.dropna()) / len(df)
    }
    
    for column, config in schema_config.items():
        quality_metrics[f'{column}_missing_rate'] = df[column].isnull().mean()
        quality_metrics[f'{column}_type_valid'] = df[column].dtype == config['expected_type']
        
        if config['type'] == 'numeric':
            quality_metrics[f'{column}_outlier_rate'] = calculate_outlier_rate(df[column])
    
    return quality_metrics
```

### 2.2 Data Drift Detection

**Statistical Drift Tests:**

**Population Stability Index (PSI):**
- Measures distribution shift between training and production data
- PSI = Σ[(% Production - % Training) × ln(% Production / % Training)]
- Thresholds: <0.1 (no drift), 0.1-0.25 (moderate), >0.25 (significant drift)

**Kolmogorov-Smirnov (KS) Test:**
- Non-parametric test for comparing continuous distributions
- Tests null hypothesis that samples come from same distribution
- Use p-value < 0.05 as drift threshold

**Chi-Square Test:**
- For categorical features comparing frequency distributions
- Tests independence between training and production distributions
- Significant drift when p-value < 0.05

**KL Divergence:**
- Measures information divergence between probability distributions
- KL(P||Q) = Σ P(x) × log(P(x)/Q(x))
- Higher values indicate more drift

**Implementation Framework:**
```python
class DriftDetector:
    def __init__(self, reference_data, feature_types):
        self.reference_data = reference_data
        self.feature_types = feature_types
        
    def detect_drift(self, current_data):
        drift_results = {}
        
        for feature in self.reference_data.columns:
            if self.feature_types[feature] == 'numeric':
                # KS test for continuous features
                ks_stat, p_value = ks_2samp(
                    self.reference_data[feature], 
                    current_data[feature]
                )
                drift_results[f'{feature}_ks_statistic'] = ks_stat
                drift_results[f'{feature}_ks_pvalue'] = p_value
                drift_results[f'{feature}_drift_detected'] = p_value < 0.05
                
                # PSI calculation
                psi_score = calculate_psi(
                    self.reference_data[feature], 
                    current_data[feature]
                )
                drift_results[f'{feature}_psi'] = psi_score
                
            else:  # categorical
                # Chi-square test
                chi2_stat, p_value = chi2_contingency_test(
                    self.reference_data[feature], 
                    current_data[feature]
                )
                drift_results[f'{feature}_chi2_statistic'] = chi2_stat
                drift_results[f'{feature}_chi2_pvalue'] = p_value
                
        return drift_results
```

### 2.3 Concept Drift Detection

**Performance-Based Detection:**
- **Sliding Window Accuracy**: Monitor accuracy over recent time windows
- **Performance Degradation Rate**: Rate of performance decline over time
- **Comparative Performance**: Current performance vs baseline/training performance

**Target Distribution Shift:**
- **Target Variable Distribution**: Monitor changes in target variable frequency
- **Prediction Distribution**: Track changes in model output distribution
- **Residual Analysis**: Analyze prediction error patterns over time

**Early Warning Indicators:**
- **Feature Importance Drift**: Changes in which features drive predictions
- **Prediction Confidence Decline**: Decreasing average prediction confidence
- **Error Pattern Changes**: Shifts in types of errors being made

## 3. System & Infrastructure Metrics

### 3.1 Resource Utilization Monitoring

**CPU & Memory Metrics:**
- **CPU Utilization**: Percentage usage across cores (average, max, p95)
- **Memory Usage**: RAM consumption (current, peak, available)
- **Memory Efficiency**: Memory usage per prediction request
- **Garbage Collection**: Frequency and duration of GC events (for languages like Python/Java)

**GPU Metrics (if applicable):**
- **GPU Utilization**: Compute and memory utilization percentages
- **GPU Memory Usage**: VRAM consumption and availability
- **GPU Temperature**: Thermal monitoring for performance throttling
- **CUDA/OpenCL Errors**: GPU computation error tracking

**Storage I/O:**
- **Disk Read/Write**: I/O operations per second and throughput
- **Disk Space**: Available storage and growth rate
- **Model Loading Time**: Time to load model artifacts from storage
- **Data Access Latency**: Time to retrieve input data

### 3.2 Container Health & Networking

**Docker Container Metrics:**
```yaml
# Docker Compose monitoring setup
version: '3.8'
services:
  ml-model:
    image: my-ml-model:latest
    deploy:
      resources:
        limits:
          memory: 4G
          cpus: '2'
        reservations:
          memory: 2G
          cpus: '1'
    healthcheck:
      test: ["CMD", "python", "health_check.py"]
      interval: 30s
      timeout: 10s
      retries: 3
    logging:
      driver: "json-file"
      options:
        max-size: "100m"
        max-file: "3"
```

**Network Performance:**
- **API Response Time**: HTTP request processing time distribution
- **Request Queue Length**: Number of pending requests
- **Connection Pool**: Active/idle connections and connection errors
- **Retry Rate**: Percentage of requests requiring retries
- **Timeout Rate**: Requests exceeding time limits

**Container Health Status:**
- **Container Restart Count**: Frequency of container restarts
- **Exit Code Tracking**: Monitoring for abnormal terminations
- **Resource Limit Violations**: Memory/CPU limit exceeded events
- **Port Accessibility**: Network port availability and responsiveness

### 3.3 Application-Level Logging

**Structured Logging Implementation:**
```python
import logging
import json
from datetime import datetime

class MLLogger:
    def __init__(self):
        self.logger = logging.getLogger('ml_model')
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)
    
    def log_prediction(self, request_id, features, prediction, confidence, latency):
        log_data = {
            'event_type': 'prediction',
            'request_id': request_id,
            'timestamp': datetime.utcnow().isoformat(),
            'model_version': os.environ.get('MODEL_VERSION'),
            'prediction': prediction,
            'confidence': confidence,
            'latency_ms': latency,
            'feature_count': len(features)
        }
        self.logger.info(json.dumps(log_data))
    
    def log_error(self, request_id, error_type, error_message):
        log_data = {
            'event_type': 'error',
            'request_id': request_id,
            'timestamp': datetime.utcnow().isoformat(),
            'error_type': error_type,
            'error_message': error_message
        }
        self.logger.error(json.dumps(log_data))
```