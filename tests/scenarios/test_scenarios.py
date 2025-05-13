"""
Test scenarios for Greg Level 1 Oncall Bot.
This file contains test queries and their expected responses for various oncall scenarios.
"""

# Test input queries
TEST_QUERIES = [
    "what's the ETA for app_hardware.hdm.fact_reader_events?",
    "what's the definition of TOTAL_TERMINAL_API_TRANSACTIONS?",
    "what's the cost for past 30 days for app_hardware.hdm.fact_reader_events?",
    "what's the highest cost for past 30 days under app_hardware tables?",
    "what're the consumers for app_hardware.hdm.fact_reader_events in past 90 days?",
    "what are affected downstream tables for app_hardware.hdm.fact_reader_events?",
    "are there any SLA misses for app_hardware tables today?",
    "what's the bottleneck in app_hardware.hdm pipelines?",
    "show me the lineage for app_hardware.hdm.fact_reader_events",
    "what's the data freshness of app_hardware.hdm.fact_reader_events?"
]

class TestResponses:
    """Contains example responses for different types of queries"""

    @staticmethod
    def eta_response():
        """Example response for ETA queries"""
        return """ETA Analysis for app_hardware.hdm.fact_reader_events:

⏰ Timing Information:
- Original ETA: 2025-05-09 15:00:00 UTC
- Current ETA: 2025-05-09 16:30:00 UTC
- Status: DELAYED

🔍 Delay Analysis:
- Reason: Upstream data delay in SUMMARY_READER_TARKIN_EVENTS

📊 Dependencies Status:
- SUMMARY_READER_TARKIN_EVENTS: delayed
- READER_METADATA: on_time

⚠️ Blocking Jobs:
- SENSOR__GET___APP_HARDWARE.ADHOC.SUMMARY_READER_TARKIN_EVENTS

🔄 Recent Updates:
- Last Update: 10 minutes ago
- Next Check: 5 minutes
"""

    @staticmethod
    def metric_definition_response():
        """Example response for metric definition queries"""
        return """📊 Definition of TOTAL_TERMINAL_API_TRANSACTIONS:

The total number of API transactions processed by a terminal device, including:
- Payment transactions
- Refund transactions
- Card read operations
- Peripheral interactions
- System health checks

💻 Implementation Logic:
```sql
SELECT 
    terminal_id,
    DATE_TRUNC('day', event_timestamp) as event_date,
    COUNT(DISTINCT transaction_id) as total_api_transactions,
    SUM(CASE WHEN event_type = 'payment' THEN 1 ELSE 0 END) as payment_count,
    SUM(CASE WHEN event_type = 'refund' THEN 1 ELSE 0 END) as refund_count,
    SUM(CASE WHEN event_type = 'card_read' THEN 1 ELSE 0 END) as card_read_count
FROM app_hardware.hdm.fact_terminal_events
WHERE event_timestamp >= DATEADD(day, -30, CURRENT_DATE())
GROUP BY 1, 2
```

📁 Location Information:
- File: app_hardware/sql/definitions/terminal_metrics.sql
- Repository: square/hardware-data-models

🔗 Related Tables:
- app_hardware.hdm.fact_terminal_events
- app_hardware.hdm.dim_terminal_metadata
- app_hardware.hdm.fact_terminal_daily_metrics

📚 Documentation:
- Metric Owner: Hardware Data Team
- Last Updated: 2025-04-01
- Confluence Link: https://square.atlassian.net/wiki/spaces/DATA/pages/terminal-metrics
"""

    @staticmethod
    def cost_analysis_response():
        """Example response for cost analysis queries"""
        return """Cost analysis for app_hardware.hdm.fact_reader_events over the past 30 days:

💰 Cost Breakdown:
- Compute Cost: $15,420.50
- Storage Cost: $2,340.75
- Total Cost: $17,761.25

📊 Usage Statistics:
- Total Queries: 12,450
- Data Scanned: 45.2 TB
- Average Query Cost: $1.42

📈 Cost Trend:
- Month-over-Month Change: +12%
- Main Driver: Increased query volume

👥 Top Consumers by Cost:
1. analytics_prod ($8,250.30)
2. bi_user ($5,120.45)
3. airflow_prod ($4,390.50)

💡 Top Recommendations for Cost Optimization:
1. Consider implementing clustering keys on frequently filtered columns
2. Review and optimize queries scanning large amounts of data
3. Evaluate warehouse sizing for common query patterns
"""

    @staticmethod
    def highest_cost_response():
        """Example response for highest cost queries"""
        return """Top costly tables under app_hardware for the past 30 days:

📊 1. app_hardware.hdm.fact_stand_events:
- Total Cost: $25,491.05
- Query Count: 15,680
- Data Scanned: 62.8 TB
- Main Users: analytics_prod, bi_user

📊 2. app_hardware.hdm.fact_reader_events:
- Total Cost: $17,761.25
- Query Count: 12,450
- Data Scanned: 45.2 TB
- Main Users: analytics_prod, airflow_prod

📊 3. app_hardware.hdm.fact_terminal_events:
- Total Cost: $12,340.80
- Query Count: 8,920
- Data Scanned: 32.1 TB
- Main Users: bi_user, data_science_prod

💡 Cost Saving Opportunities:
1. Implement auto-clustering on fact_stand_events
2. Review large queries from analytics_prod
3. Optimize warehouse selection for bi_user queries
"""

    @staticmethod
    def consumer_analysis_response():
        """Example response for consumer analysis queries"""
        return """Consumer analysis for app_hardware.hdm.fact_reader_events over the past 90 days:

👤 analytics_prod:
- Query Count: 5,420
- Data Scanned: 15.3 TB
- Common Warehouses: ANALYTICS_PROD_XL, ANALYTICS_PROD_L
- Peak Usage: 08:00-17:00 UTC
- Common Joins: dim_reader_metadata, fact_reader_daily_summary

👤 bi_user:
- Query Count: 3,250
- Data Scanned: 8.2 TB
- Common Warehouses: BI_PROD_L
- Peak Usage: 15:00-23:00 UTC
- Common Joins: fact_reader_hourly_metrics

👤 airflow_prod:
- Query Count: 2,800
- Data Scanned: 12.5 TB
- Common Warehouses: ETL_PROD_XL
- Peak Usage: 00:00-06:00 UTC
- Common Joins: fact_reader_performance

📈 Usage Trends:
- Growing Usage: analytics_prod (+15% MoM)
- Declining Usage: bi_user (-5% MoM)
- Stable Usage: airflow_prod
"""

    @staticmethod
    def downstream_impact_response():
        """Example response for downstream impact queries"""
        return """Downstream app_hardware tables affected by app_hardware.hdm.fact_reader_events:

📊 1. app_hardware.hdm.fact_reader_daily_summary:
- Impact Level: HIGH
- SLA: 17:00 UTC
- Usage: Critical for daily reporting
- Consumers: 25+ dashboards
- Alert Channel: #hardware-data-oncall

📊 2. app_hardware.hdm.fact_reader_hourly_metrics:
- Impact Level: HIGH
- SLA: Every hour
- Usage: Real-time monitoring
- Consumers: 10+ monitoring systems
- Alert Channel: #hardware-monitoring

📊 3. app_hardware.hdm.reader_performance_metrics:
- Impact Level: MEDIUM
- SLA: 18:00 UTC
- Usage: Weekly reporting
- Consumers: 5+ dashboards
- Alert Channel: #hardware-data-review

⚠️ Critical Dashboards Affected:
1. Reader Health Overview
2. Daily Performance Metrics
3. Hardware Operations Monitor
"""

    @staticmethod
    def sla_status_response():
        """Example response for SLA status queries"""
        return """SLA Status for app_hardware tables:

⚠️ Performance Tables (SLA: 17:00 UTC):
- fact_reader_performance (updated at 18:06 UTC)
- fact_stand_performance (updated at 18:12 UTC)
- fact_squid_performance (updated at 18:35 UTC)
Delay: ~1-1.5 hours late
Notifications sent to: #hardware-data-oncall and PagerDuty

❌ HDM Event Tank Tables (SLA: 12:00 UTC):
Various event tables including:
- fact_battery_events
- fact_connectivity_event
- fact_crash_event
- fact_firmware_update_event
- fact_generic_error_message_event
- fact_payment_event
- fact_peripheral_event
- fact_spe_firmware_event
- fact_squid_event
Delay: ~6 hours late
Notifications sent to: #hardware-data-review-alerts

🔍 Impact Analysis:
- Critical Dashboards Affected: 12
- Reports Delayed: 8
- Teams Notified: Hardware Ops, Data Team

👨‍💻 Oncall Actions Taken:
1. Incident created: INC-123456
2. Teams notified via PagerDuty
3. Status update posted in #hardware-data-oncall
"""

    @staticmethod
    def pipeline_bottleneck_response():
        """Example response for pipeline bottleneck queries"""
        return """Pipeline Bottleneck Analysis for app_hardware.hdm:

❌ Failed ETL Jobs (10 total):
Root Cause: app_hardware.hdm.fact_reader_events
Error: "Sensor has timed out; SENSOR__GET___APP_HARDWARE.ADHOC.SUMMARY_READER_TARKIN_EVENTS"

🔍 Investigation Links:
- Failed DAG: https://production-2--sqwaverunner.sqprod.co/dags/app_hardware_fact_transactions_unit_token_daily_v9_squarewave/grid
- Failed Squarewave job: https://squarewave.sqprod.co/#/jobs/5869/sql
- Monitoring Dashboard: https://grafana.sqprod.co/d/hardware-pipeline-health

📊 Affected Downstream Tables:
1. app_hardware.hdm.fact_reader_daily_summary (HIGH)
2. app_hardware.hdm.fact_reader_hourly_metrics (HIGH)
3. app_hardware.hdm.fact_reader_performance (MEDIUM)
4. app_hardware.hdm.fact_reader_status (MEDIUM)
5. app_hardware.hdm.dim_reader_metadata (LOW)
(and 5 more tables)

💡 Recommended Actions:
1. Check SUMMARY_READER_TARKIN_EVENTS sensor status
2. Verify upstream data availability
3. Review recent sensor configuration changes
4. Check for resource constraints

👥 Escalation Path:
1. Hardware Data Oncall
2. Platform Infrastructure Team
3. Hardware Systems Team
"""

    @staticmethod
    def lineage_response():
        """Example response for lineage queries"""
        return """Lineage for app_hardware.hdm.fact_reader_events:

📥 Upstream Dependencies:
1. app_hardware.adhoc.summary_reader_tarkin_events
   - Update Frequency: 15 min
   - SLA: 11:45 UTC
   - Owner: Hardware Systems Team

2. app_hardware.adhoc.reader_metadata
   - Update Frequency: 1 hour
   - SLA: 12:00 UTC
   - Owner: Device Management Team

📤 Downstream Dependencies:
1. app_hardware.hdm.fact_reader_daily_summary
   - SLA: 17:00 UTC
   - Critical: YES
   - Used by: 25+ dashboards

2. app_hardware.hdm.fact_reader_hourly_metrics
   - SLA: Hourly
   - Critical: YES
   - Used by: Real-time monitoring

🔄 Job Information:
- DAG: hardware_reader_events_pipeline
- Schedule: Every 15 minutes
- Average Runtime: 8 minutes
- Resource Class: high_memory

📊 Data Quality Checks:
1. Record count validation
2. Null check on key fields
3. Duplicate detection
4. Latency monitoring
"""

    @staticmethod
    def data_freshness_response():
        """Example response for data freshness queries"""
        return """Data Freshness Analysis for app_hardware.hdm.fact_reader_events:

⏰ Current Status:
- Last Update: 2025-05-12 02:45:00 UTC
- Usual Update Frequency: Every 15 minutes
- Current Latency: 52 minutes
- Status: DELAYED

📊 Recent Performance:
- Average Latency (24h): 12 minutes
- Maximum Latency (24h): 52 minutes
- Minimum Latency (24h): 8 minutes
- SLA Compliance (24h): 92%

🔍 Delay Analysis:
- Start Time: 2025-05-12 02:15:00 UTC
- Root Cause: Upstream data delay
- Affected System: SUMMARY_READER_TARKIN_EVENTS
- Impact Level: MEDIUM

📈 Historical Context:
- 7-day Average Latency: 11 minutes
- 30-day SLA Compliance: 98.5%
- Last Major Incident: 2025-05-01

⏱️ Recovery Plan:
1. Upstream job restart initiated
2. Expected recovery: ~30 minutes
3. Monitoring in place
"""


def get_response(query: str) -> str:
    """
    Returns appropriate response based on the query type.
    Args:
        query: The user's query string
    Returns:
        str: Formatted response string
    """
    query = query.lower()
    
    if "eta" in query:
        return TestResponses.eta_response()
    elif "definition" in query:
        return TestResponses.metric_definition_response()
    elif "cost" in query and "highest" not in query:
        return TestResponses.cost_analysis_response()
    elif "highest cost" in query:
        return TestResponses.highest_cost_response()
    elif "consumer" in query:
        return TestResponses.consumer_analysis_response()
    elif "downstream" in query:
        return TestResponses.downstream_impact_response()
    elif "sla" in query:
        return TestResponses.sla_status_response()
    elif "bottleneck" in query:
        return TestResponses.pipeline_bottleneck_response()
    elif "lineage" in query:
        return TestResponses.lineage_response()
    elif "freshness" in query:
        return TestResponses.data_freshness_response()
    
    return "I don't have enough information to answer that query. Please try rephrasing or provide more details."


class PipelineMCP:
    """MCP for handling ETL and pipeline analysis"""

    def get_response(self, query: str) -> str:
        """
        Returns response for pipeline-related queries
        Args:
            query: The user's query string
        Returns:
            str: Formatted response string
        """
        if "bottleneck" in query.lower() and "app_hardware.hdm" in query.lower():
            return TestResponses.pipeline_bottleneck_response()
        return "No pipeline issues found for the specified domain."