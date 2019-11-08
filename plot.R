#!/usr/bin/env Rscript
library(ggplot2)
args <- commandArgs(trailingOnly=TRUE)
exp <- read.table(args[1])
pdf(args[2])
ggplot(exp, aes(factor(V2), V3,)) + geom_boxplot(width=0.5) + scale_y_log10() + theme_classic() + facet_wrap(~V1, scales='free')
dev.off()
