# Tool: notionApi
MCP Toolset for interacting with Notion pages, blocks, and databases.

This tool is provided via a running Notion MCP server.

The agent does NOT call the Notion REST API directly.
---

# WHEN TO USE THIS TOOL

Use notionApi when:

- Persisting structured outputs to Notion
- Updating existing pages
- Reading knowledge stored in Notion
- Querying task or project databases
- Appending generated content

DO NOT use this tool for:
- Local file edits
- Git operations
- Temporary scratch notes

---

# AVAILABLE MCP ACTIONS

The following actions are exposed by the Notion MCP server.

## notion-query-database
Retrieve pages from a database.

Use when:
- Searching structured records
- Looking up tasks, notes, or items

Inputs typically include:
- database_id
- filter
- sorts

---

## notion-create-page
Create a new page under a parent page or database.

Use when:
- Saving generated results
- Creating reports
- Adding new entries

Key inputs:
- parent
- properties
- children (optional blocks)

---

## notion-update-page
Modify properties on an existing page.

Use when:
- Updating status fields
- Changing titles
- Editing metadata

Required:
- page_id
- properties

Never delete or overwrite properties unless explicitly requested.

---

## notion-retrieve-page
Fetch metadata and properties for a page.

Use when:
- Confirming state before editing
- Reading structured values

---

## notion-retrieve-block-children
Read page content blocks.

Use when:
- Understanding context
- Continuing existing notes

---

## notion-append-block-children
Append new content blocks to an existing page.

Use when:
- Writing generated text
- Adding summaries
- Logging actions

Prefer appending instead of replacing content.

---

# DECISION RULES

1. If the task involves **saving or updating knowledge**, use notionApi.
2. If information might already exist, retrieve or query first.
3. Avoid duplicate page creation.
4. Prefer database queries over scanning individual pages.
5. Do not invent page IDs — only use IDs retrieved from Notion.

---

# OUTPUT STRUCTURE GUIDELINES

When writing blocks:

- Prefer paragraph blocks for normal text.
- Use heading blocks for sections.
- Keep content concise and structured.
- Avoid excessive formatting.

---

# SAFETY CONSTRAINTS

- Never delete pages or blocks unless explicitly instructed.
- Do not expose NOTION_TOKEN or authentication details.
- Assume workspace data is persistent and shared.

---

# CONNECTION INFO (REFERENCE)

Transport: MCP
Endpoint:
http://localhost:8800/mcp

Authentication is handled by the MCP server runtime.

The agent should assume the server is already running.

---

# EXAMPLE INTENT MAPPING

User says:
"Save this summary to Notion"

Agent plan:
1. notion-create-page
2. notion-append-block-children

---

User says:
"Mark task as done"

Agent plan:
1. notion-query-database
2. notion-update-page
