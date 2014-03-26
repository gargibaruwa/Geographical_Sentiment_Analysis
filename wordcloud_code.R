#give the directory path which contains the file containing the adjectives from movie_reviews corpus that was created from python script
#the directory should contain only this file and no other file
movie_review <- Corpus(DirSource("C:/Users/Gargi/Desktop/COURSES/Data mining/PROJECT/Final DM Project/wordcloud"))



#movie_review <- tm_map(movie_review, stripWhitespace)

movie_review <- tm_map(movie_review, tolower)

movie_review <- tm_map(movie_review, removeWords, stopwords("english"))

movie_review <- tm_map(movie_review, stemDocument)

movie_review <- tm_map(movie_review, removeNumbers)

movie_review <- tm_map(movie_review, removePunctuation)

#wordcloud(movie_review, scale=c(5,0.5), min.freq=5, max.words=100, random.order=FALSE, rot.per=0.35, use.r.layout=FALSE, colors=brewer.pal(8, "Dark2"))



png("wordcloud_packages.png", width=1280,height=800, res=100)
wordcloud(movie_review, scale=c(5,0.5),min.freq=3, use.r.layout=FALSE,
          max.words=Inf, random.order=FALSE, rot.per=0.35, 
          colors=brewer.pal(8, "Dark2"))
dev.off()

