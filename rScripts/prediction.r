library(tree)


train <- read.csv("/Users/zahidpanjwani/Desktop/Code/Kaggle/Taxi-Trajectory/datasets/df_train_2.csv")
test <- read.csv("/Users/zahidpanjwani/Desktop/Code/Kaggle/Taxi-Trajectory/datasets/df_test3.csv")

dostuff <- function(train2) {	
	train2 <- train[0:500,]
	train2$POLYLINE <- NULL
	train2$latSt <- NULL
	train2$lngStZn <- as.factor(train2$lngStZn)
	train2$latStZn <- as.factor(train2$latStZn)
	train2$finZn <- as.factor(train2$finZn)
	return(train2)
}

train2 <- dostuff(train2)
tr1 <- tree(finZn~DAY_TYPE+CALL_TYPE+hour+lngStZn+latStZn,data=train2,method="class")
plot(tr1)
text(tr1,cex=0.8)

test_data <- dostuff(test)
pr1 <- predict(tr1,test_data,type="class")
	
	
	




