![img](./Images/Amazon_Prime_Video_logo.png)

# PrimeTime: An Amazon Prime Video - Content Based - Recommendation System

### Author:
- Jawwad Siddiqui:
[LinkedIn](https://www.linkedin.com/in/jsiddiqui85/) |
[GitHub](https://github.com/jsiddiqui85) |
[Medium](https://medium.com/@jsiddiqui85)

## Business Understanding 

In 2019 Amazon hired a lot of Data Scientists and Data Engineers to try an improve their recommendation algorithms in an attempt to provide twice as good recommendations for movies and TV shows on their Amazon Prime Video service.  Although, they were able to improve their recommendations, this new *collaborative filtering* approach still fell short of their expectations.  The collaborative approach deemed to recommend content based on how a user was interacting with the current content available (based on *user history* of movie and shows previously watched by *similar users*) but it failed to address recommending content based on similar movies and shows a user already watched or like to watch.  

As Amazon's computing resources grew, the company wanted to begin using algorithms to leverage all of this new data that they had collected on their users.  Recently, Amazon hired Data Engineers and Data Scientist's to test new technologies to recommend video products on their streaming service Amazon Prime Video.  Although the new approaches leveraging neural networks and other various types of machine learning appeared to be promising, none of them actually worked as they were expecting. In fact, many of these artificial intelligence approaches not only performed worse than the collaborative filtering but it seemed that the company's original approach of using human curation and lists found on Google performed better.

At this point, Amazon has decided to seek out Data Scientists who are willing to take a look inside the black box of machine learning to figure out the best approach for providing recommendations to their Amazon Prime Video subscribers.


## Overview


This project leverages the entire Amazon Prime Video database to provide a *content based filtering* recommendation system to their current subscribers.  Currently, Amazon Prime Video ranks third in content streaming services when compared to its competitors Netflix and Hulu.  Although they hold part of the streaming service market, they would like to readjust themselves in the market by retaining their current subscriber base by leveraging an improved recommendation system for their current subscribers.

In order to address the problem that Amazon has posed, I have used the following two content specific models to improve on Amazon's currently collaborative filtering algorithm:

    1. Cosine Similarity
    2. K-Nearest Neighbors 
    
Both of these algorithms (models) that I used are trained on the *entire dataset*.  They use movie features such as the movie title, content type (movie or show), movie release year, movie length (runtime), and each movie's IMDB score to provide a more curated recommendation experience for the Amazon Prime Video user.


## Data

This data was found and downloaded from **Kaggle.com** which was acquired and put together in May of 2022 containing data available in the United States market. 

The dataset includes over roughly **9,000** movie and show titles currently available to stream on Amazon Prime Video. In addition, there are over **124,000** credits of actors and directors.  Both movie/show titles and actors/director names are matched up using the <mark>JustWatch Movie ID</mark>.

Amazon Prime Video titles are distributed within 15 columns with information including:

- ID: The title ID on JustWatch.
- title: The name of the title.
- show type: TV show or movie.
- description: A brief description.
- release year: The release year.
- age certification: The age certification.
- runtime: The length of the episode (SHOW) or movie.
- genres: A list of genres.
- production countries: A list of countries that produced the title.
- seasons: Number of seasons if it's a SHOW.
- IMDB ID: The title ID on IMDB.
- IMDB Score: Score on IMDB.
- IMDB Votes: Votes on IMDB.
- TMDB Popularity: Popularity on TMDB.
- TMDB Score: Score on TMDB.

Actors and directors have a total of 5 columns including:

- person ID: The person ID on JustWatch.
- ID: The title ID on JustWatch.
- name: The actor or director's name.
- character name: The character name.
- role: ACTOR or DIRECTOR.

This Amazon Prime Video dataset can be downloaded [HERE](https://www.kaggle.com/datasets/victorsoeiro/amazon-prime-tv-shows-and-movies)

## Methods

My methodology follows building two recommendation systems based of off two content based filtering models: `Cosine Similarity` and `K-Nearest Neighbors`. After modeling, I built a function that takes in three **user-inputted** inputs that include the name of the movie, the number of recommendations the user would like, and whether the content is a movie or a show and then uses either model to provide its recommendations.

1. Cosine Similarity
- this model basis its recommendations off of the genres that were One Hot Encoded 

2. K-Nearest Neighbors
KNN appears to yield strong recommendations across multiple genres.  The final results appear to be showing similar results as the Cosine Similarity recommender system which suggests that both of these systems are working properly.

The following hyperparameter values were tested:

1. **metric**
    - manhattan
    - minkowski
    - euclidean
    - chebyshev


2. **algorithm**
    - brute
    - ball_tree
    - kd_tree
    - auto


3. **n_neighbors**
    - 3
    - 5
    - 7
    - 9
    - 11

**Please note:** Metric= 'manhattan', algorithm= 'brute', n_neighbors= 7 demonstrated to yield a wider variety of results compared to Cosine Similarity.  Other hyperparameter combinations did not add any value by showing almost identical results.

## Conclusions


Both of the recommendation systems appear to be performing quite well.  They are both able to provide a variety of recommendations that use the genre of a movie/show title as a basis of providing these recommendations.  I leveraged two models used particularly for a content based filtering recommendation system that included: **Cosine Similarity** and **K-Nearnest Neighbors**.  Given the number of results within the scope of the provided movie or show title, there is a strong relationship with the similarity and recommendations that are provided to that user.  


## Limitations

There are a few limitations with this project that include:

1. The data relies heavily on the original movie id that is available on JustWatch to provide its recommendations.  If a  movie id was not available  for a particular title, that movie would go unseen when calculating similarity scores, thus not providing a holistic recommendation.
2. Amazon Prime Video is still in the early phases of obtaining licenses and purchasing new content for their streaming service.  Therefore, having about 9,000 total movie and show titles is a very small number of titles to represent a strong recommendation system.  Having a much larger number of movie shows and titles would help to significantly improve their recommendation system.
3. Amazon likes to keep all of their data proprietary, therefore making it very difficult for data scientists such as myself to retrieve information regarding any of their services including Amazon Prime Video.  There are currently **no developer API's** for Amazon Prime, forcing people to only use publically available datasets.

## Next Steps

1.  Expanding the data by finding additional Amazon Prime Video datasets that are available to the public.
2.  Potentially using web scraping to gather additional data.
3.  Deploying the final model function to a mobile app, or at least making it available on a website for people to use.


## For More Information

Please review my full analysis available in my [Jupyter Notebook](PrimeTime_Main.ipynb) or [Presentation Deck](PrimeTime.pdf).

For additional questions, feel free to [contact me](mailto:jsiddiqui85@gmail.com).

## Repository Structure

```
├── data                                <- Source data .csv files
├── images                              <- Exported Notebook visualizations
├── Workspace                           <- Additional scratch work notebooks
├── PrimeTime.pdf                       <- PDF version of project presentation
├── PrimeTime_Main.ipynb                <- Technical and narrative documentation in Jupyter Notebook
└── README                              <- Top-level README for reviewers of this project
