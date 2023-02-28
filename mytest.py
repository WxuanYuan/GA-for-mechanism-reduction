import time
import numpy as np
import cantera as ct
from GAPar import GeneticAlgorithmForOptimization, GeneticAlgorithmForReduction
import multiprocessing
import os
from Data.gas import GasForOptimization, GasForReduction


def reactants_and_products(reaction):
    return list(reaction.products.keys()) + list(reaction.reactants.keys())


if __name__ == '__main__':
    current_directory = os.path.dirname(os.path.abspath(__file__))
    print(current_directory)
    multiprocessing.freeze_support()
    print("Program has started!")

    # ga = GeneticAlgorithmForOptimization(root_path=current_directory, parallel=True)
    # ga.generated_yaml_file(0)

    #########################################

    ga = GeneticAlgorithmForReduction(root_path=current_directory, parallel=False)
    # ga.generated_yaml_file(0)
    # ga.visualize("Reduction", 50)
    # ga.makeGrid("Reduction", 50)
    ga.run()
    print("Program has ended, this window will be closed in 10 seconds.")
    time.sleep(10)
