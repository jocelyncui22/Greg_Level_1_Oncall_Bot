"""Specialized MCPs for different types of queries"""

from typing import Dict, Any
import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from tests.scenarios.test_scenarios import TestResponses

class DataOpsMCP:
    """MCP for handling data operations and SLA monitoring"""

    def get_response(self, query: str) -> str:
        """Process data operations related queries"""
        query = query.lower()
        
        # Handle SLA queries
        if "sla" in query and "app_hardware" in query:
            return TestResponses.sla_status_response()
            
        # Handle cost queries
        if "cost" in query:
            if "highest" in query:
                return TestResponses.highest_cost_response()
            return TestResponses.cost_analysis_response()
            
        # Handle consumer analysis
        if "consumer" in query:
            return TestResponses.consumer_analysis_response()
            
        # Handle data freshness
        if "freshness" in query:
            return TestResponses.data_freshness_response()
            
        # Handle metric definitions
        if "definition" in query:
            return TestResponses.metric_definition_response()
            
        # Handle lineage queries
        if "lineage" in query:
            return TestResponses.lineage_response()
            
        return "No data operations issues found for the specified domain."


class PipelineMCP:
    """MCP for handling ETL and pipeline analysis"""

    def get_response(self, query: str) -> str:
        """Process pipeline related queries"""
        query = query.lower()
        
        # Handle bottleneck queries
        if "bottleneck" in query and "app_hardware.hdm" in query:
            return TestResponses.pipeline_bottleneck_response()
            
        # Handle ETA queries
        if "eta" in query:
            return TestResponses.eta_response()
            
        # Handle downstream impact queries
        if "downstream" in query or "affected" in query:
            return TestResponses.downstream_impact_response()
            
        return "No pipeline issues found for the specified domain."


class MetricsMCP:
    """MCP for handling metrics and definitions"""

    def get_response(self, query: str) -> str:
        """Process metrics related queries"""
        query = query.lower()
        
        if "definition" in query:
            return TestResponses.metric_definition_response()
            
        return "No metric information found for the specified query."