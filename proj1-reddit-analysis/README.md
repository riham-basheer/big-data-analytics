# Project 1: Large-Scale Reddit Comment Analysis

**Type:** Solo Project  
**Technologies:** Python, Hadoop Streaming, MapReduce, NLTK, Google Colab  

## Overview
Built a suite of MapReduce jobs to process and analyze a massive corpus of 53+ million Reddit comments (~31GB uncompressed). The goal was to extract meaningful patterns about user behavior, trending topics, and data quality issues from real-world social media data.

## Data
- 53,851,542 comments from various subreddits (Reddit public API)
- JSON format, one comment per line
- Compressed: 5.4 GB (bzip2) | Uncompressed: 31.6 GB

## What I Built

### Topic Analysis (Requirements 1 & 3)
- Wrote MapReduce jobs to identify most-discussed topics per subreddit and per user
- Discovered that specialized communities (e.g., r/medicalschool) have highly relevant domain jargon, while generic subreddits produce more noise
- Built a job to find topics with highest/lowest scores. Discovered low-scored topics included spam/ad-heavy comments — validating the approach

### Performance Optimization
- Encountered critical NLTK bottleneck when processing the full dataset
- **Solution:** Decomposed the job into a two-stage MapReduce pipeline and introduced a **heap queue** data structure for top-K topic tracking
- This dramatically reduced insertion-sort overhead and made full-dataset processing feasible

### Data Integrity Validation
- Programmatically verified dataset assumptions before trusting results:
  - "downvotes" field: universally zero across all 53M records
  - "replies" field: empty across all records
  - Conclusion: Reddit's public API tracks only an aggregate "score" (score = upvotes), not separate upvote/downvote counts
- This prevented a flawed "controversiality vs. replies" analysis that the project initially required

### Behavioral Insights
- **Bot Detection:** Identified that the most prolific "users" were bots (e.g., AutoModerator ranked #1) — a critical finding that reframes any user-behavior analysis
- **Temporal Patterns:** Analyzed commenting traffic by hour — found a 10 AM trough and 8 PM peak, aligning with real-world work/school schedules

## Key Lessons
- Scale amplifies computational inefficiencies — a library that works on samples may fail on full data
- Validating what's *missing* in the data is as important as analyzing what's there
- Sampling strategy (10 → 100K → 1M records) was essential for iterative development