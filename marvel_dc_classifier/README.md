# Classifying Reddit Posts to Marvel/DC Movie Subreddits & Sentiment Analysis

## Problem Statement
We are employees of a marketing agency hired by a toy company to perform market research on Reddit to build a classifier model that classifies posts from Marvel vs DC movies subreddits in order to

- Build a classifier model that can be applied to other platforms (e.g. Twitter, Facebook) with text data to determine public interest in either movie franchise
- Find popular heroes and keywords for each franchise to identify product and marketing opportunities (using sentiment analysis)

The success of the classifier model will be evaluated using the accuracy metric i.e. is the model able to correctly label a post as coming from the Marvel/DC subreddit? Similarly, sentiment analysis will be evaluated using accuracy i.e. is the model able to correctly identify a post as having positive, neutral or negative sentiment? This can help us identify the most discussed heroes and keywords (a sign of popularity) and whether the discussions around these heroes and topics are positive, neutral or negative to identify product and marketing opportunities to boost revenue for our customer, the toy company.

## Data Source
5,000 posts each from r/marvelstudios and r/DC_Cinematic

## Conclusion and Findings
We managed to build a model that is able to classify Reddit posts as Marvel/DC content with pretty good accuracy (~90%)!

This model can be used to classify data from other non-Reddit sources as Marvel/DC and possible applications include:
- Determining popularity/public interest in each brand on other platforms with text data such as Twitter or Facebook in order to do market sizing analysis and estimate revenue potential on potential customers by platform or demographic
- Other downstream analysis e.g. sentiment analysis

Key findings from sentiment analysis include:
- Popular characters to develop toys and marketing initivatives for, e.g.
    - Marvel: Ms Marvel, Spiderman, Iron Man, Captain America
    - DC: Batman, Joker
- Key actors/characters to avoid due to negative sentiment
    - Although the most popular characters tend to appear under top words with positive AND negative sentiment, some phrases/actors/characters under the negative sentiment lists should be avoided altogether due to legal issues/controversy
