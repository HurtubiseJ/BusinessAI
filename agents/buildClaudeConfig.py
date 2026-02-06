import os
import tempfile
from BusinessAI.tools.loadTools import load_tool_docs, load_mcp_servers

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

def buildClaudeConfig(agentName: str, tools: list[str]) -> dict:
    # Load agent system prompt
    with open(os.path.join(BASE_DIR, "agents", agentName, "system.md")) as f:
        prompt = f.read()

    # Load tool docs
    tool_docs = load_tool_docs(tools)

    systemPrompt = f"""
{prompt}

--- AVAILABLE TOOLS ---
{tool_docs}
"""
    load_mcp_servers(tools)

    tmpSystemPrompt = tempfile.NamedTemporaryFile(delete=False, suffix=".md")
    with open(tmpSystemPrompt.name, "w") as f:
        f.write(systemPrompt)

    return {
        "systemPrompt": tmpSystemPrompt.name
    }
