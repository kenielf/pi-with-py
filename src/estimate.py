#!/usr/bin/env python 
import random  # Library necessary por using random numbers


def estimate_pi(sample_n):
    # Create the variables for counting numbers of points in total and inside the circle
    points_t = points_c = 0
    # Start looping and calculate the points, incrementing the appropriate variables
    for _ in range(sample_n):
        x, y = random.uniform(0,1), random.uniform(0, 1)
        distance = x**2 + y**2
        if distance <= 1:
            points_c += 1
        points_t += 1
    # Return the result of following expression
    return (4 * (points_c / points_t))


# Run the program
if __name__ == "__main__":
    print("Estimating π with 100.000 samples")
    print(estimate_pi(100_000))
