# Tool: notionApi
MCP Toolset for interacting with Notion. This tool is provided via running `notionApi` mcp service.

# When to use
- Updating documentation following codebase changes
- Persisting structured outputs to Notion
- Updating existing pages
- Reading knowledge stored in Notion
- Querying task or project databases
- Appending generated content

DO NOT use this tool for:
- Local file edits
- Git operations
- Temporary scratch notes

# Rules
Pages containing CHECKED property `CLAUDE ACCESS` are able to be read and modified. This includes databases on such pages. Created pages should check this property.