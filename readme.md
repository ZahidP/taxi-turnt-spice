## Methodology

### Goal
The goal here, according to the Kaggle challenge was to predict the destination of a taxi given its initial trajectory.

### Cleaning

First off, we have to look at missing data. The good thing is that we mainly need trip ID, taxi ID, and the coordinates at a given time, and most of the data has this information.

Let's look at the data (some columns removed):
```
ROW       TRIP_ID                  CALL       MISS     ORIG   TAXI_ID
1710046  1404165960620000403       B          NaN       53     20000403
1710173  1404167765620000403       B          NaN       53     20000403
1710193  1404171239620000403       B          NaN       18     20000403
```

```
POLYLINE                                              hour  
0  [[-8.618643, 41.141412], [-8.618499, 41.141376...  19.000000  
1  [[-8.639847, 41.159826], [-8.640351, 41.159871...  19.133333
```


Each trip must follow a particular trajectory. Each trip however, can be of a different length, so if X1 and X2 are mapped to time [0,15] and [15,30], respectively, then different trips will have different numbers of X variables associated with them.

So we have something like this:

```
Y_init = X_0
Y(1) = Y_init + X_1
Y(2) = Y(1) + X(2)
...
Y(t) = Y(t-1) + X(t)
```

We only need to predict the final destination, using the initial trajectory.


This depends on how we define the initial trajectory.

### Strategy A

1. Define positions, plus trajectories.
   - We will use a coordinate plus its X trajectory and Y trajectory.
   - Example: `Y_init` can be paired with the direction obtained from `Y(0) to Y(3)`
2. Define "zones" in which coordinates
   - For now we will need to break up the map into many zones in order to be able to classify locations accordingly
   - A coordinate pair cannot be treated independently ie. `[lat,lng] -> X_1 and X_2` or treated as continuous numerical variables
   - Longitude and latitude classify points across the entire world, but here we are only considering a city. So it might be best to define zones within Porto.
3. Define clusters
   - This can help with zone definition, prediction and hopefully other things as well.
   - The idea is to break up trips into logical clusters. They be trips to work, to a bar, morning trips, evening trips etc.
   - We can cluster initial trajectories, initial locations, or final locations.
