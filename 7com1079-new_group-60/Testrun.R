# call libraries
install.packages("tidyverse")
library(tidyverse)
library(ggplot2)
library(dplyr)
# read the csv file
covid <- read.csv("covid_impact_on_airport_traffic.csv")

#considering n number of entry
recent <- head(covid, n = 1160)

#removing date from yyyy/mm/dd
recentDate <- as.Date(recent$Date)

#assinging for graph
x <- recentDate
y <- recent$PercentOfBaseline

plot(x, y, main = "correlation between percentofbaseline and date", xlab = "month", ylab = "percentofbaseline", pch = 20, frame = TRUE)

#using linear model
model <- lm(y ~ x, data = covid)

abline(model, col = "black")

#saving the file as and png
pdf(file = "Rplot.pdf", onefile = TRUE)

png(file = "rplot.png")

dev.off()
