"""Greg AI agent that processes messages and coordinates with MCPs"""

from typing import Dict, Any, List
import json
from datetime import datetime
import re
from src.mcps.specialized_mcps import DataOpsMCP, PipelineMCP, MetricsMCP


class GregAI:
    """Greg AI agent that processes messages and coordinates with MCPs"""

    def __init__(self):
        # Initialize all MCPs
        self.mcps = {
            "dataops": DataOpsMCP(),
            "pipeline": PipelineMCP(),
            "metrics": MetricsMCP()
        }

    def process_message(self, message: Dict[str, Any]) -> str:
        """Process incoming message and determine appropriate response"""
        text = message["text"].lower()
        responses = []

        # Check for specific query types and route to appropriate MCP
        if any(word in text for word in ["sla", "cost", "consumer", "freshness"]):
            responses.append(self.mcps["dataops"].get_response(text))

        if any(word in text for word in ["pipeline", "bottleneck", "eta", "downstream"]):
            responses.append(self.mcps["pipeline"].get_response(text))

        if any(word in text for word in ["definition", "metric"]):
            responses.append(self.mcps["metrics"].get_response(text))

        # If no specific matches, try each MCP
        if not responses:
            for mcp in self.mcps.values():
                response = mcp.get_response(text)
                if response and "No" not in response[:3]:  # Check if it's not a "No issues found" type response
                    responses.append(response)

        return self._format_response(responses, text)

    def _format_response(self, responses: List[str], original_query: str) -> str:
        """Format the final response with context and multiple MCP inputs"""
        if not responses:
            return (
                "I apologize, but I couldn't find relevant information for your query. "
                "Could you please rephrase or provide more details? You can ask about:\n"
                "- ETA for tables\n"
                "- Table definitions\n"
                "- Cost analysis\n"
                "- Consumer analysis\n"
                "- Downstream impact\n"
                "- SLA status\n"
                "- Pipeline bottlenecks\n"
                "- Data freshness"
            )

        # Remove any duplicate responses
        unique_responses = list(dict.fromkeys(responses))
        
        # Format the response
        if len(unique_responses) == 1:
            return unique_responses[0]
        
        response_parts = ["Here's what I found from multiple sources:\n"]
        for i, response in enumerate(unique_responses, 1):
            response_parts.append(f"\n{i}. {response}\n")
            
        return "\n".join(response_parts)