from pydantic import BaseSettings
from typing import Dict, Any, Optional

class Settings(BaseSettings):
    # App Configuration
    APP_NAME: str = "Greg"
    APP_VERSION: str = "0.1.0"
    DEBUG: bool = False
    
    # Snowflake Configuration
    SNOWFLAKE_ACCOUNT: str
    SNOWFLAKE_USER: str
    SNOWFLAKE_PASSWORD: str
    SNOWFLAKE_WAREHOUSE: str
    SNOWFLAKE_DATABASE: str
    
    # Alert Configuration
    ALERT_THRESHOLD: Dict[str, Any] = {
        "critical": 90,
        "warning": 70,
        "info": 50
    }
    
    # Notification Configuration
    SLACK_WEBHOOK_URL: Optional[str] = None
    PAGERDUTY_API_KEY: Optional[str] = None
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()