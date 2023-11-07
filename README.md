<img src="https://github.com/MSRudolph/NeutroGen/blob/main/figures/name_shadow.png" width="800">

# NeutroGen
This is the GitHub repository for team **NeutroGen** during "The Blaise Pascal [re]Generative Quantum Challenge".

Our project enables neutral atom quantum computers for generative modeling, with a novel application in combinatorial optimization **without training the quantum model on the quantum computer**.

## The Approach: Spectral Graph Theory
<img src="https://github.com/MSRudolph/NeutroGen/blob/main/figures/schematic.png" width="800">

Given data with inherent structure, we apply classical pre-processing to extract the most vital information. Using a spectral graph theory approach [1], we find an embedding for the neutral atoms in 2D or 3D. The resulting layout has enhanced capabilities to learn from the available data. But here is the catch, our algorithm works even **without training**. This reduces the quantum resources required for practical application by orders of magnitude and solves the challenge of applying neutral atoms for problems that aren't inherently 2D or 3D.


## Our Example: Windfarm Optimization
The challenge is to place windmills on a field such that they are exposed to the largest wind velocities, but are neither too close to each other, nor too far apart. We frame this task as a combinatorial optimization problem.

**Find the Jupyter notebook for the example [here](./demo.ipynb).**

**The brief demo video of our v1 prototype can be found [here](https://youtu.be/_z96CCOOskE).**

First, we draw 20 random samples and evaluate their cost. Alternatively, we can utilize the optimization history of a conventional optimizer whose solution we want to improve. The samples are converted into a training data distribution via a Softmax function that assigns a higher probability to better-performing samples [2].

<img src="https://github.com/MSRudolph/NeutroGen/blob/main/figures/correlation_graph.png" width="400">

Then we extract the correlation inside the data and score pairs of data bits by the probability that they both are "1" at the same time. Our spectral graph theoretical approach will place atoms close together if the Rydberg blockade can naturally be leveraged to suppress unwanted "11". In other words, we find high-quality atom embeddings based on previous observations and their cost value.

<img src="https://github.com/MSRudolph/NeutroGen/blob/main/figures/final_positions.png" width="400">

Finally, we implement a standard adiabatic protocol with global interactions and generate samples from the final state. Even without training the generative model, we observe frequent high-quality samples and significantly outperforms exhaustive search. Any training of the model on a neutral atom quantum computer can improve the quality of the results from here.

<img src="https://github.com/MSRudolph/NeutroGen/blob/main/figures/comparison_training_data.png" width="400">
<img src="https://github.com/MSRudolph/NeutroGen/blob/main/figures/comparison_exhaustive.png" width="400">


## Relevant Literature
[1] Atithi Acharya, Manuel Rudolph, Jing Chen, Jacob Miller, and Alejandro Perdomo-Ortiz. "Qubit seriation: Improving data-model alignment using spectral ordering." arXiv preprint arXiv:2211.15978 (2022).

[2] Javier Alcazar, Mohammad Ghazi Vakili, Can B. Kalayci, and Alejandro Perdomo-Ortiz. "Geo: Enhancing combinatorial optimization with classical and quantum generative models." arXiv preprint arXiv:2101.06250 (2021).




