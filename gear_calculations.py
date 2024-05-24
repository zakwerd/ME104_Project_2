import sys
import os
import math

"""
This code is meant to help with gear calculations for project 2.

"""

# Global Vars
FORCE = 22.5
fos = 1.5
MIN_TEETH = 18
MAX_TEETH = 96
MIN_PITCH = 24
MAX_PITCH = 72

# Material Values For Hardened Steel
HS_Se = 100000  # PSI
HS_Density = 0.289  # lbs/inch cubed

# Material Values for 303 Stainless Steel
SS_Se = 50000
SS_Density = 0.289

def radius(N, P):
    r = N / (2 * P)
    return r

def torque(r):
    t = FORCE * r
    return t

def min_width_hs(t, p, N):
    w = (16 * t * fos/HS_Se) * (p ** 2) / (N * ((N - 11) ** (1/8)))
    return w

def min_mass_hs(t, N):
    return (4 * math.pi * t * (HS_Density / HS_Se) * (N ** (7/8)))

def min_width_ss(t, p, N):
    return (16 * t * fos/SS_Se) * (p ** 2) / (N * ((N - 11) ** (1/8)))

def min_mass_ss(t, N):
    return 4 * math.pi * t * (SS_Density / SS_Se) * (N ** (7/8))

def find_min_masses():
    # List to store tuples of (mass, input1, input2)
    results = []
    
    teeth_range = range(MIN_TEETH, MAX_TEETH)
    pitch_range = range(MIN_PITCH,MAX_PITCH)
    
    # Nested for-loops to find all possible masses
    for N in range(MIN_TEETH, MAX_TEETH, 2):
        for P in pitch_range:
            r = radius(N, P)
            torq = torque(r)

            mass = min_mass_hs(torq, N)
            results.append((mass, N, P))

    
    # Sort results by mass (smallest to largest)
    results.sort()

    # Write the results to masses.txt
    count = 0
    with open('masses.txt', 'w') as file:
        for mass, N, P in results:
            count += 1
            file.write(f"{count}. Mass: {mass}, Teeth: {N}, Pitch: {P}, Material: Hardened Steel\n")


def main():
    # Your main code goes here
    find_min_masses()

if __name__ == "__main__":
    main()
