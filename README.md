## MLB-pyMatchups
The goal of this project is to pull the Daily Matchups data from the MLB baseball savant website to make that data manipulatable in order to integrate further advanced statistics and prediction. 

#### Motivation
I've been in love with baseball my whole life and for a couple of years I had been playing MLB's Beat the Streak game while using their matchup data. As this MLB season started and 
I began to struggle in my fantasy baseball league I wanted to come up with a way of combining my love for programming and tech with my love for baseball.  I read up about the resources
available for statistical analysis and looked at other repos to get ideas flowing as to what I could make. Then I remembered the daily matchup data and found it on the baseball savant website,
then my goal was to make this data usable in a python program that would help me pull ahead in fantasy baseball. I had been trying to think of a project I could do that would help me dive deeper 
into machine learning and data analysis. Doing this project I aim to better my understanding of Python, programming, MLB analytics, and machine learning.

 
#### Phases
The development of this project has three main phases: 
   
    Phase 1: 
     -This phase consists of the initial scraping and publishing of the project to github. Finding a way to efficiently get the data from the baseball savant website to manipulate it in 
      python is this phase's primary goal. It is also important to write code and functions that will make it easy to customize and specify the data wanted by the developer. During this phase I am
      also thinking about the structure and organization of the project (classes, functions, outputs, etc.). 
    Phase 2: 
     - Phase 2 mainly deals with a more user friendly displaying of the data. My goals are to use packages such as numpy and mathplotlib to plot spraycharts and zone charts. I also want to identify what 
     data is most important to display in the tables and charts. This will help the user in analyzing specific pitcher vs batter comparisons and performance probabilities. Once the data is graphed and charted I aim to publish this project as a package for use by other developers in 
     their own personal projects. 
    
    Phase 3:
    - In phase 3 my main focus will be on applying machine learning and statistical anylisis to the data. I aim to develop machine learning using Tensorflow or OpenML to predict the probabilities
    of success in certain Pitcher vs Batter matchups and specific situations. In this phase is key to integrate my lifelong baseball knowledge with my programming and ML knowledge to efficiently
    predict outcomes. Machine learning is a concept I am extremely interested in and want to learn more about. Phase 3 will also require a lot of backtesting to analyze confidence levels and tweak 
    the program. These functionalities will also be added to the python package.


#### Features
This project allows you pull and sort data from the https://baseballsavant.mlb.com/daily_matchups site. Then you can also pull historical individual matchup or player data.

## Code Example
Currently main funcionality is available in the matchupScraper.py file. From there is that you can run the functions below to display the daily matchup data and carreer stats.

#### Installation
For now the best way to install and use the code is to directly clone the repository and then run your commands in the main matchupScraper.py file. 



#### Contribute

In progress. For now all help and ideas is appreciated, I am currently writing a contribute.MD. 

#### Credits
I got a lot of inspiration from other baseball analytics repositories on github such as pybaseball by jlbdc. 

## Future Updates

I am currently working on making the code more concise and usable by expanding functions and adding more organization. I am also working on the displaying of data to 
visualize spray charts, zone charts, hot zones, and etc.

## License
MIT © FranB57()
