# import library
library(readr)
library(coda)

# z score
path <- "/mnt/docs/project/mcmc/simulation-techniques/Metropolis-Hastings algorithm/example-2/sample-of-sigma.csv"
sample <- read.csv(path)
geweke.diag(sample[2])
