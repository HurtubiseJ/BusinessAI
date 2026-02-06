# BusinessAI 
This repo give configuration to add specialized claude code instances. This repo is not intended to be modfied here. This repo is a **submodule** or **subrepo** that is added to exisiting repositories. 

# **IMPORTANT** ADD .env FILE in /services/notion/.env 
You will need to add a `.env` file in the /services/notion/ directory. 
I needs the key=value `NOTION_TOKEN=ntn_XXXX...` 

**SEE THIS LINK TO GET YOUR NOTION TOKEN**: https://github.com/mcp/makenotion/notion-mcp-server

# Submodule Commands
Here are a few important submodule commands to update this subrepo

## Pull changes
`root$ git submodule update --remote` Pulls current BuisnessAI code from remote. Update automatically.

**NOTE:** `git pull` alone will NOT update the submodule

## Push changes
If you need to make changes to this repo you will need to push to **BuinessAI/ MAIN REPO**. You cannot push changes via the main (non-submodule) git repo. 

`cd` into BuinessAI/ and git push there. 


# Dependencies
You must have docker installed on your computer. 
You need Claude Code CLI installed. (`root$ claude` should open the claude cli prompt). You may need to sign into Claude Code. 

And of course a version of python installed.

# Run
To run use the following commands ABOVE BuisnessAI/ repo.

EX:
/root
    /BuinessAI
    /SomeProject


root$ python3 -m BuinessAI.agents.data_agent.start

# Agents
To select a different agent change the agent name in the command above `...agent.<name>.start`
For example .agent.fronted_agent.start

