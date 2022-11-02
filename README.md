# Simulation of a Battle Royale Game

This is a simple simulation to a game of battle royale with 100 players.

Open the Jupyter notebook for visualisation of results: [**CLICK HERE**](battle_royale_sim.ipynb)


## Logic of the simulation
The players are ranked from `PRO` to `BAD`. The pro players have better accuracy and higher K/D.

The game consists of 99 rounds. In each round 2 players are randomly chosen to fight.

Each round goes as follow:
- At the beginning of the round each player has 100% health bar.
  
- Loop:
    - A random generator decides which player starts. The player with higher K/D has more chance to be selected.
    - The chosen player gets 5 shots. A headshot counts as 20% damage, a body shot as 10% damage and a miss as 0% damage. A player with a higher accuracy, has better chance to score headshots. The damage is reflected on the other player's health bar.
    - Repeat the loop until one player health bar is complete.

- Add the states to the game.
