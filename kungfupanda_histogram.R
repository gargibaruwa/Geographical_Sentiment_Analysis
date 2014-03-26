x <- data.frame(
  Class = c("Decision Tree","Decision Tree","Naive Bayes","Naive Bayes",
            "Neural Networks","Neural Networks"),
  Geography = c("Global","Local","Global","Local","Global","Local"),
  positive = c(79,88,74,84,72,87),
  negative = c(21,12,26,16,28,13)
)

mx <- melt(x, id.vars=1:2)
mx <- rename(mx, c("variable"="Polarity"))

theme_set(theme_gray(base_size = 18))
myplot <- ggplot(mx, aes(x=Geography, y=value, fill=Polarity)) + 
                geom_bar(stat="identity") + 
                facet_grid(~Class) +
                ylab("User Comments") +
                ggtitle("Classifier Sentiment Analysis")

myplot + theme_bw()
myplot + theme(panel.background = element_rect(fill='white', colour='black'))




x <- data.frame(
  Class = c("Actual Data","Actual Data"),
  Geography = c("Global","Local"),
  positive = c(68,78),
  negative = c(32,22)
)

mx <- melt(x, id.vars=1:2)
mx <- rename(mx, c("variable"="Polarity"))

theme_set(theme_gray(base_size = 18))
myplot <- ggplot(mx, aes(x=Geography, y=value, fill = Polarity)) + 
  geom_bar(stat="identity") + 
  facet_grid(~Class) +
  coord_equal(1/25) +
  ylab("User Comments") +
  ggtitle("Actual Data")

myplot + theme_bw()
myplot + theme(panel.background = element_rect(fill='white', colour='black'))



  
