
for m in 1:9 {
  dname<-paste("~/significant_locations/gps data/00",m,"/Trajectory",sep="")
  setwd(dname)
  # Get all the files in a folder
  files <- list.files(pattern="*.plt")
  
  # Make coord and plots directory
  # dir.create("plots")
  # dir.create("coord")
  
  # Loop through all the files and apply the function
  count<-1
  len = length(files)
  for(i in 1:len) {
    x = read.csv(files[i],skip=6)
    y = data.frame(x[1],x[2],x[7])
  #   file_name<-paste("GPS-000",i,sep="-")
  #   png(paste("plots/",file_name, ".png", sep=""), width=454, height=360, units="px")
  #   plot(y, main=file_name, xlab="Latitude", ylab="Longitude")
  #   dev.off()
    write.table(y, paste("coord/",i,".txt", sep=""), sep=",", row.names=FALSE, col.names=FALSE)
  }
}

# file.exists("../gps data/010/Trajectory/coord/")

dname<-paste("../gps data/010/Trajectory",sep="")
setwd(dname)
# Get all the files in a folder
files <- list.files(pattern="*.plt")

count<-1
len = length(files)
for(i in 1:len) {
  x = read.csv(files[i],skip=6)
  y = data.frame(x[1],x[2],x[7])
  write.table(y, paste("coord/",i,".txt", sep=""), sep=",", row.names=FALSE, col.names=FALSE)
}