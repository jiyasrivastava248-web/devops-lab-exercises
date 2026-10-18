\# Exercise 6: Real-Time Operations Monitoring and Alerting



\## Objective

Build a real-time delivery monitoring system using Python, Prometheus, and Grafana, with alert rules and a Jenkins pipeline definition.



\## Project Structure

\- `delivery\_monitoring/delivery\_metrics.py` — generates simulated delivery metrics.

\- `delivery\_monitoring/Dockerfile` — defines the Docker image for the metrics application.

\- `delivery\_monitoring/prometheus.yml` — configures Prometheus scraping and alert rules.

\- `delivery\_monitoring/alert\_rules.yml` — defines delivery monitoring alerts.

\- `delivery\_monitoring/Jenkinsfile` — defines the Jenkins pipeline.



\## Metrics

\- `total\_deliveries`

\- `pending\_deliveries`

\- `on\_the\_way\_deliveries`

\- Average delivery time, calculated from the summary metrics.



\## Alert Rules

\- \*\*HighPendingDeliveries:\*\* triggers when pending deliveries exceed 10 for 15 seconds.

\- \*\*HighAverageDeliveryTime:\*\* triggers when average delivery time exceeds 30 seconds for 15 seconds.



\## Verification

\- Prometheus targets show the delivery service and Prometheus as UP.

\- Both delivery alert rules were observed in the FIRING state.

\- Grafana is connected to Prometheus.

\- The Grafana dashboard contains panels for Total Deliveries, Pending Deliveries, Deliveries on the Way, and Average Delivery Time.



\## Evidence

Add screenshots of:

1\. Prometheus targets showing both targets UP.

2\. Prometheus alerts showing the delivery alerts.

3\. Grafana dashboard showing all four metric panels.



\## Note

The Jenkinsfile is defined, but the Jenkins pipeline still needs to be run and verified.



