import geneManipulators
mutatedgeen=geneManipulators.gene_mutator('ccccccccccccccccagaggagagtgagagac', 3, 2, 1)
geneManipulators.gene_translator(mutatedgeen)
geneManipulators.mutation_type('ccccccccccccccccagaggagagtgagagac', mutatedgeen)
print(mutatedgeen)
print(geneManipulators.gene_translator('ccccccccccccccccagaggagagtgagagac'))