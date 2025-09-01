# labelfree-trebuchet (unfinished)

Applying label-free neural networks to the [Trebuchet dataset](https://ti.arc.nasa.gov/c/8/) from NASA's Prognostics repository.

Reference paper: [Label-Free Supervision of Neural Networks with Physics and Domain Knowledge](https://arxiv.org/pdf/1609.05566.pdf)

## Description

- Setup Python env: `uv sync`
- Download data with `bash get-data.sh`

## Status as of Aug 2025

The label-free supervision paper shows that real-world physics constraints can be baked into deep learning loss functions to skip using labels by instead forcing NNs to self-identify instances in the data that fit the physics-driven loss function. The NASA Trebuchet dataset is an image dataset of balls launched into the air with a trebuchet, with the position of the balls labelled through masks.

I was intrigued to replicate the label-free supervision paper on this dataset as it is very close to one of the experiments in the paper, where the authors tried to map the trajectory of a pillow thrown in the air, with the knowledge that objects in free fall have their height as a function of gravity in the form of $y = -\frac{1}{2}gt^2 + v_{0}t + y_{0}$.

This project got abandoned fairly quickly after I started it. Right now I'm just git committing files in this project properly as I clean out my hard drive. If I were to revisit this project in the future, note to self to pick up at loss function formulation as it's not correct yet
