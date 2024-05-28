# install packages
# install.packages(c("coda", "readr"))

# import packages
library(readr)
library(coda)

# sample 1
path1 <- "/mnt/docs/project/mcmc/simulation-techniques/Metropolis-Hastings algorithm/example-1/sample1.csv"
sample1 <- read.csv(path1)
geweke.diag(sample1[2])

# sample 2
path2 <- "/mnt/docs/project/mcmc/simulation-techniques/Metropolis-Hastings algorithm/example-1/sample2.csv"
sample2 <- read.csv(path2)
geweke.diag(sample2[2])

# sample 3
path3 <- "/mnt/docs/project/mcmc/simulation-techniques/Metropolis-Hastings algorithm/example-1/sample3.csv"
sample3 <- read.csv(path3)
geweke.diag(sample3[2])

# sample 4
path4 <- "/mnt/docs/project/mcmc/simulation-techniques/Metropolis-Hastings algorithm/example-1/sample4.csv"
sample4 <- read.csv(path4)
geweke.diag(sample4[2])

# sample 5
path5 <- "/mnt/docs/project/mcmc/simulation-techniques/Metropolis-Hastings algorithm/example-1/sample5.csv"
sample5 <- read.csv(path5)
geweke.diag(sample5[2])

# sample 6
path6 <- "/mnt/docs/project/mcmc/simulation-techniques/Metropolis-Hastings algorithm/example-1/sample6.csv"
sample6 <- read.csv(path6)
geweke.diag(sample6[2])
