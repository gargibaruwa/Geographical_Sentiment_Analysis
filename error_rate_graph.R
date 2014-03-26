#graph
df_new <- data.frame(value = c(12,13,21,14,18,18,11,12,24),
                     Movies = c("KungFu Panda","KungFu Panda","KungFu Panda","Life of Pi","Life of Pi","Life of Pi","Endhiran","Endhiran","Endhiran"),
                     classifier = c("Naive Bayes","Recursive Neural Network","Decision Tree","Naive Bayes","Recursive Neural Network","Decision Tree","Naive Bayes","Recursive Neural Network","Decision Tree"))
library(ggplot2)
theme_set(theme_bw(base_size = 18))
myplot <- ggplot(df_new, aes(y = value, x = Movies, colour = classifier,group=classifier)) +
  geom_line(size=1.5) +
  coord_equal(1/3) +
  ylab("Error Rate") +
  ggtitle("Classifier Comparison")
myplot + theme_bw()
myplot + theme(panel.background = element_rect(fill='white'))
myplot + scale_y_continuous(breaks=c(10,12,14,16,18,20,22,24))

