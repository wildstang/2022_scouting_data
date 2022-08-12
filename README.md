# 2022_scouting_data

WildRank scouting data collected during our 2022 Rapid React competitions.

## What is WildRank?

[WildRank](https://github.com/wildstang/wildrank) is our new scouting app for the 2022 season. 

### Application Versions

This repo contains data collected both with WildRank 1 during the official competition season, as well as, development versions of WildRank 2 during offseason competitions. The versions or Git hashes of the app used to collect the data can be found below. The data collect with version 1 should be compatible with any version 1 release of the app.

| Event                         | Version |
| ----------------------------- | ------- |
| Central Illinois Regional     | 1.1.0   |
| Midwest Regional              | 1.2.2   |
| Newton Division (Houston)     | 1.3.0   |
| Rock River Offseason*         | 0efe1ea |
| Mukwonago Robotics Offseason* | 278bb96 |

*partial testing data

## How do I read this data?

The best way is with WildRank where you can upload a zip archive of the results using the "Transfer Raw Data" page. Otherwise, the data is all in JSON, easily parsable with most programming languages. The results are all stored by match-team as key-value pairs. Cycles are stored as a list of recurring pairs.

## Data Integrity

This is raw data from our scouters. The quantitative data has not been modified, but qualitative data has been removed. This means there are known (and unknown) errors in the data, particularly at Newton. We chose not to correct our data, first because it would be too time consuming and second to offer us uncleaned data for future testing/learning purposes. If in the future this data is cleaned the cleaned data will be posted alongside the raw data here.

## Thanks

Thank you to all the scouters who contributed to this data. Our scouters spent countless hours in the stands and collected the vital data to achieve our two blue banners. We successfully scouted 1653 match-teams, that is 99.8% of qualification matches across our 3 official events.