# Project 2: League of Legends Match Analytics

**Technologies:** Python, PySpark (Spark SQL, RDDs), Riot Games API  

## Overview
Simulated a real-world analytics lifecycle for one of the world's largest esports titles. Extracted raw match data from the Riot Games API, engineered features from deeply nested JSON, and delivered insights that could inform player strategy or developer decisions.

## What I Built

### Data Engineering Pipeline
- Pulled raw match data from the Riot Games API
- Normalized heavily nested JSON into analyzable tables:
  - Exploded the 10-player participant list into individual rows per match
  - Extracted and flattened team-level bans into a dedicated table
  - Implemented a local cache strategy to decouple development from live API calls

### Champion Meta Analysis
- Joined participant and ban datasets to compute the three pillars of champion strength:
  - **Pick rate** — how often a champion is selected
  - **Win rate** — how often a champion wins when picked
  - **Ban rate** — how often a champion is banned
- Extended this with a **best-lane-per-champion** analysis: grouped champion-lane pairs, aggregated wins, and selected the lane with highest win count per champion

### Champion Synergy Detection
- Designed a combinatorial algorithm to quantify champion pair synergy:
  - Grouped champions by (gameId, teamId) to get same-team compositions
  - Generated all unique 2-champion combinations per team
  - Calculated win rates per duo — surfacing which pairs overperform together
- Used a sorted-tuple approach to ensure order-independence and avoid duplicate pairings

### Item Analytics
- Transformed the 7-slot item inventory per participant into a flat structure via RDD operations
- Computed pick rates and win rates per item — revealing which items dominate the meta

## Key Lessons
- Thinking in Spark transformations is essential when facing deeply nested, list-heavy data
- The duo synergy algorithm required careful grouping-and-explode patterns to avoid Cartesian blowups
- Pre-trained encoders and transfer learning make research-quality models reproducible with limited resources