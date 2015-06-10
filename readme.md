## Methodology

### Goal
The goal here, according to the Kaggle challenge was to predict the destination of a taxi given its initial trajectory.

### Cleaning

First off, we have to look at missing data. The good thing is that we mainly need trip ID, taxi ID, and the coordinates at a given time, and most of the data has this information.

Let's understand the data (some columns removed):
```
ROW       TRIP_ID                  CALL       MISS     ORIG   TAXI_ID
1710046  1404165960620000403       B          NaN       53     20000403
1710173  1404167765620000403       B          NaN       53     20000403
1710193  1404171239620000403       B          NaN       18     20000403
```

` TRIP_ID = TIMESTAMP + '6' + TAXI_ID `

...`

Each trip must follow a particular trajectory. Each trip however, can be of a different length, so if X1 and X2 are mapped to time [0,15] and [15,30], respectively, then different trips will have different numbers of X variables associated with them.

So we have something like this:

```
Y_init = X_0
Y(1) = Y_init + X_1
Y(2) = Y(1) + X(2)
...
Y(t) = Y(t-1) + X(t)
```

This can be simplified because we only need to predict the final destination, using the initial trajectory.


This depends on how we define the initial trajectory. 
