# Greg - Level 1 Oncall Bot

Greg is an automated bot designed to reduce the operational burden on data engineers, MLEs, and data scientists during oncall rotations. This prototype aims to handle common Level 1 oncall tasks through multiple integrated MCPs (Micro-Control Programs).

## Overview

Greg serves as a first-line responder for common oncall issues, automating routine tasks and providing intelligent responses to typical problems. By leveraging multiple MCPs, Greg can:

- Handle common data pipeline issues
- Respond to basic alerts and monitoring
- Provide initial diagnosis of system problems
- Execute standard recovery procedures
- Escalate complex issues to human oncall engineers when necessary

## Project Structure

```
Greg_Level_1_Oncall_Bot/
├── src/
│   ├── mcps/           # Different MCP implementations
│   ├── utils/          # Utility functions and helpers
│   ├── config/         # Configuration management
│   └── handlers/       # Event and alert handlers
├── tests/
│   ├── unit/          # Unit tests
│   └── integration/   # Integration tests
├── docs/              # Documentation
├── requirements.txt   # Python dependencies
├── setup.py          # Package setup
├── .env.example      # Example environment variables
└── README.md         # Project documentation
```

## MCPs (Micro-Control Programs)

The following MCPs are integrated into Greg:

1. Snowflake MCP
   - Query execution and monitoring
   - Performance analysis
   - Error handling

2. Developer MCP
   - Code deployment checks
   - Basic debugging tools
   - Log analysis

3. Codesearch MCP
   - Code repository search
   - Issue investigation
   - Documentation lookup

## Setup and Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Greg_Level_1_Oncall_Bot.git
cd Greg_Level_1_Oncall_Bot
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Copy and configure environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

## Usage

[Usage instructions will be added as the prototype develops]

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

[License information to be added]

## Contact

[Contact information to be added]