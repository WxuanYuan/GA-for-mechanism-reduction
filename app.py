import time
import numpy as np
import cantera as ct
from GAPar import GeneticAlgorithmForOptimization
import multiprocessing
import os


if __name__ == '__main__':
    current_directory = os.path.dirname(os.path.abspath(__file__))
    print(current_directory)
    multiprocessing.freeze_support()
    print("Program has started!")

    ga = GeneticAlgorithmForOptimization(root_path=current_directory)
    ga.run()
    print("Program has ended, this window will be closed in 10 seconds.")
    time.sleep(10)
