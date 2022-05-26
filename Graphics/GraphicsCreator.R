args <- commandArgs(trailingOnly = TRUE)

# args[1] = directoryToDataFile
# args[2] = width
# args[3] = height
# args[4] = support
# args[5] = confidence
# args[6] = circularDirectory
# args[7] = graphDirectory


library(circlize)
library(migest)
library(dplyr)
library(arulesViz)
library(randomcoloR)

itemsetsMAXICLAVECLUSTER <- readLines(con = paste(args[1], sep=""))

itemsetsMAXICLAVECLUSTER <- strsplit(itemsetsMAXICLAVECLUSTER, ",")
head(itemsetsMAXICLAVECLUSTER, 1)

# the values are transformed from string to double
supportValue <- as.double(args[4])
confidenceValue <- as.double(args[5])

rulesMAXICLAVECLUSTER <- apriori(itemsetsMAXICLAVECLUSTER, parameter=list(minlen=2, maxlen=2, support=supportValue, confidence=confidenceValue))
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

jpeg(file=paste(args[7], sep=""),width=widthImage,height=heightImage, res=100)
plot(rulesMAXICLAVECLUSTER, method="graph",engine="igraph",cex=7,  control=list(max=length(rulesMAXICLAVECLUSTER)))
dev.off()

dev.new(width=500, height=400)
jpeg(file=paste(args[6], sep=""),width=widthImage,height=heightImage,res=600)

chordDiagram(as.data.frame(dataFrameMAXICLAVECLUSTER),transparency = 0.3, directional = FALSE)
dev.off()