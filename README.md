# NeutroGen
This is the GitHub repository for team **NeutroGen** during "The Blaise Pasqal [re]Generative Quantum Challenge".

Our project enables neutral atom quantum computers for generative modeling, with a novel application in combinatorial optimization **without training the quantum model on the quantum computer**.

## The Approach: Spectral Graph Theory
<img src="https://github.com/MSRudolph/NeutroGen/blob/main/figures/schematic.png" width="800">

Given data with inherent structure, we apply classical pre-processing to extract the most vital information. Using a spectral graph theory approach, we find an embedding for the neutral atoms in 2D or 3D. The resulting layout has enhanced capabilities to learn from the available data. But here is the catch, our algorithm works even **without training**. This reduces the quantum resources required for practical application by orders of magnitude.


## Our Example: Windfarm Optimization
The challange is to place windmills on a field such that they are exposed to the largest wind velocities, but are neither too close to each other, nor too far apart. We frame this task as a combinatorial optimization problem.



