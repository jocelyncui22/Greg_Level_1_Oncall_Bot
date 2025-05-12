from abc import ABC, abstractmethod
from typing import Any, Dict, List

class BaseMCP(ABC):
    """Base class for all Micro-Control Programs (MCPs)"""
    
    @abstractmethod
    async def handle_alert(self, alert_data: Dict[str, Any]) -> Dict[str, Any]:
        """Handle incoming alerts"""
        pass
    
    @abstractmethod
    async def diagnose_issue(self, issue_data: Dict[str, Any]) -> Dict[str, Any]:
        """Diagnose reported issues"""
        pass
    
    @abstractmethod
    async def execute_action(self, action_data: Dict[str, Any]) -> Dict[str, Any]:
        """Execute remediation actions"""
        pass
    
    @abstractmethod
    async def get_status(self) -> Dict[str, Any]:
        """Get current status of the system"""
        pass

class SnowflakeMCP(BaseMCP):
    """Snowflake-specific MCP implementation"""
    
    async def handle_alert(self, alert_data: Dict[str, Any]) -> Dict[str, Any]:
        # Implementation for Snowflake alerts
        pass
    
    async def diagnose_issue(self, issue_data: Dict[str, Any]) -> Dict[str, Any]:
        # Implementation for Snowflake issues
        pass
    
    async def execute_action(self, action_data: Dict[str, Any]) -> Dict[str, Any]:
        # Implementation for Snowflake actions
        pass
    
    async def get_status(self) -> Dict[str, Any]:
        # Implementation for Snowflake status
        pass

class MCPRegistry:
    """Registry for managing multiple MCPs"""
    
    def __init__(self):
        self.mcps: Dict[str, BaseMCP] = {}
    
    def register_mcp(self, name: str, mcp: BaseMCP) -> None:
        """Register a new MCP"""
        self.mcps[name] = mcp
    
    def get_mcp(self, name: str) -> BaseMCP:
        """Get an MCP by name"""
        return self.mcps[name]
    
    def list_mcps(self) -> List[str]:
        """List all registered MCPs"""
        return list(self.mcps.keys())