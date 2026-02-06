import os
import json
import subprocess

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

def get_config(toolName: str) -> str:
    path = os.path.join(BASE_DIR, 'tools', 'notionApi', 'mcp.json')

    if not os.path.exists(path):
        print("No config found for:", toolName)
        return None
    
    # load tool mcp.json
    with open(path, "r") as f:
        cfg = json.load(f)

    match toolName:
        case _:
            return cfg

def load_mcp_servers(tools: list[str]) -> dict:
    cfg = {}

    for tool in tools:
        cfg[tool] = get_config(tool)

    for name in cfg.keys():
        subprocess.run(
            ['claude', 'mcp', 'add-json', name, json.dumps(cfg[name])]
        )

    
    print("Current MCP Servers:")
    subprocess.run((
        'claude', 'mcp', 'list'
    ))

    return True

def load_tool_docs(tools: list[str]) -> list[str]:
    docs = []

    for tool in tools:
        path = os.path.join(BASE_DIR, 'tools', tool, 'tool.md')

        if not os.path.exists(path):
            print("Tool docs not found for: ", tool)
            continue

        with open(path, 'r') as f:
            docs.append(f.read())

    return "\n\n".join(docs)






