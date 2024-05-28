library(readr)
library(coda)

# sample 1
path1 <- "/mnt/docs/project/mcmc/simulation-techniques/gibbs-sampleing/bivariate-normal/sample1.csv"
sample1 <- read.csv(path1)
geweke.diag(sample1[2])
geweke.diag(sample1[3])

# sample 2
path2 <- "/mnt/docs/project/mcmc/simulation-techniques/gibbs-sampleing/bivariate-normal/sample2.csv"
sample2 <- read.csv(path2)
geweke.diag(sample2[2])
geweke.diag(sample2[3])

# sample 3
path3 <- "gibbs-sampleing/bivariate-normal/sample3.csv"
sample3 <- read.csv(path3)
geweke.diag(sample3[2])
geweke.diag(sample3[3])
