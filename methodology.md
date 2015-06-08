## Methodology

### Cleaning

First off, we have to look at missing data. The good thing is that we mainly need trip ID, taxi ID, and the coordinates at a given time, and most of the data has this information.

Next, we need to group timestamps and coordinates with a particular trip. This complicates things a bit because our predictions are not a simple `Y = X1 + X2 + X3 ...`

Instead, each trip must follow a particular trajectory. Each trip however, can be of a different length, so if X1 and X2 are mapped to time [0,15] and [15,30], respectively, then different trips will have different numbers of X variables associated with them.

So we have something like this:

```
Y_init = X_0
Y(1) = Y_init + X_1
Y(2) = Y(1) + X(2)
...
Y(t) = Y(t-1) + X(t)
```

This can be simplified because we only need to predict the final destination, using the initial trajectory.


This depends on how we define the initial trajectory. Initially, we will use the first 30 seconds of the trip.

For example,
