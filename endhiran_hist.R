x <- data.frame(
  Class = c("Decision Tree","Decision Tree","Naive Bayes","Naive Bayes",
            "Neural Networks","Neural Networks"),
  Geography = c("Global","Local","Global","Local","Global","Local"),
  positive = c(35,89,42,83,40,82),
  negative = c(65,11,58,17,60,18)
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
  positive = c(47,77),
  negative = c(53,23)
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



