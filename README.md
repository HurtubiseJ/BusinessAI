# BusinessAI 
This repo give configuration to add specialized claude code instances. DO NOT modify this repo.

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

