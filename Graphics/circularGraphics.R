args <- commandArgs(trailingOnly = TRUE)

library(circlize)
library(migest)
library(dplyr)
library(arulesViz)
library(randomcoloR)

itemsetsMAXICLAVECLUSTER <- readLines(con = paste(args[1], sep=""))

itemsetsMAXICLAVECLUSTER <- strsplit(itemsetsMAXICLAVECLUSTER, ",")
head(itemsetsMAXICLAVECLUSTER, 1)


# rulesMAXICLAVECLUSTER <- apriori(itemsetsMAXICLAVECLUSTER, parameter=list(minlen=2, maxlen=2, support=0.45, confidence=0.8))
# rulesMAXICLAVECLUSTER
rulesMAXICLAVECLUSTER <- apriori(itemsetsMAXICLAVECLUSTER, parameter=list(minlen=2, maxlen=2, support=0.1, confidence=0.05))
rulesMAXICLAVECLUSTER

dataFrameMAXICLAVECLUSTER<- data.frame(
  lhs = labels(lhs(rulesMAXICLAVECLUSTER)),
  rhs = labels(rhs(rulesMAXICLAVECLUSTER)),
  rulesMAXICLAVECLUSTER@quality)

# rowsCluster= row.names(dataFrameMAXICLAVECLUSTER)
# rowsCluster
# coloresCluster=c()
# i=1
# for (name in rowsCluster) {
#   ifelse(name %in% c("{A}"),coloresCluster[i]<-"black",
#          ifelse(name %in% c("{B}"),coloresCluster[i]<-"yellow",
#                 ifelse(name %in% c("{C}"),coloresCluster[i]<-"purple",
#                        ifelse(name %in% c("{D}"),coloresCluster[i]<-"pink",
#                               ifelse(name %in% c("{E}"),coloresCluster[i]<-"red",
#                                      ifelse(name %in% c("{F}"),coloresCluster[i]<-"grey",
#                                             ifelse(name %in% c("{G}"),coloresCluster[i]<-"blue",
#                                                    ifelse(name %in% c("{H}"),coloresCluster[i]<-"green",
#                                                           ifelse(name %in% c("{I}"),coloresCluster[i]<-"brown",
#                                                                  coloresCluster[i]<-"orange"
#                                                           )))))))))
#   
#   i=i+1
# }
labels(rulesMAXICLAVECLUSTER)
dev.new(width=1000, height=8000)
#
widthImage <- strtoi(args[2])
widthImage <- widthImage*10

heightImage <- strtoi(args[3])
heightImage <- heightImage*10

jpeg(file=paste(args[5], sep=""),width=widthImage,height=heightImage, res=100)
plot(rulesMAXICLAVECLUSTER, method="graph",engine="igraph",cex=7,  control=list(max=length(rulesMAXICLAVECLUSTER)))
dev.off()

dev.new(width=500, height=400)
jpeg(file=paste(args[4], sep=""),width=widthImage,height=heightImage,res=600)

chordDiagram(as.data.frame(dataFrameMAXICLAVECLUSTER),transparency = 0.3, directional = FALSE)
dev.off()