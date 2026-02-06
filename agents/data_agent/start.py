from BusinessAI.services import ensureServices
from BusinessAI.agents import buildClaudeConfig
from .config import ENABLED_TOOLS
import subprocess

def main():

    # makes sure MCP services are running
    print("Ensuring services...")
    ensureServices.ensureServices(ENABLED_TOOLS)

    # creates and returns path to system prompt based on selected agent
    print("Building configuration...")
    cfg = buildClaudeConfig.buildClaudeConfig("data_agent", ENABLED_TOOLS)
    systemPromptPath = cfg['systemPrompt']

    print("Launching Claude CLI...")
    subprocess.run(
        ['claude', 'code', '--system-prompt-file', systemPromptPath]
    )

if __name__ == "__main__":
    main()