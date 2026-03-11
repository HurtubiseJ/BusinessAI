from BusinessAI.services import ensureServices
from BusinessAI.agents import buildClaudeConfig
from .config import ENABLED_TOOLS
import subprocess

def main():

    print("Ensuring services...")
    ensureServices.ensureServices(ENABLED_TOOLS)

    cfg = buildClaudeConfig.buildClaudeConfig("db_agent", ENABLED_TOOLS)
    systemPromptPath = cfg['systemPrompt']

    print("Launching Claude CLI...")
    subprocess.run(
        ['claude', 'code', '--system-prompt-file', systemPromptPath]
    )

if __name__ == "__main__":
    main()