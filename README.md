# Quantum-Evolutionary-Algorithm-Knapsack-Python-
This project is the 'Python' version of Classic Quantum Evolutionary Algorithm (QEA) which finds a solution for "Knapsack" problem. 
This implementation is designed based on the transaction paper called "Quantum-inspired evolutionary algorithm for a class of combinatorial optimization" by Kuk-Hyun Han and Jong-Hwan Kim. Paper link: https://ieeexplore.ieee.org/abstract/document/1134125
- Team members for original code which was on *MATLAB*:
1. Majid Beheshti Mohtasham
2. Jamshid Sabet Navokh
3. Mohammad Mobasher Kashani
4. Mohammad.H Tayarani

This *Python* version which is the conversion of MATLAB version to Python is performed by:
* Majid Behehshti Mohtasham

This code is implemented in *PyCharm 2017.3.3 Professional Edition*

The *MATLAB* version of this code is the *"basic"* type of QEA which employed in the following publications. For every paper the idea's code is implemented as well, to  compare with the basic QEA:
* [*"A statistical analyzing approach for Quantum Evolutionary Algorithms."* In 2011 19th Iranian Conference on Electrical Engineering, pp. 1-6. IEEE, 2011.](https://ieeexplore.ieee.org/abstract/document/5955671)
* [*"A novel initialization for quantum evolutionary algorithms based on spatial correlation in images for fractal image compression."* In Soft Computing in Industrial Applications, pp. 317-325. Springer, Berlin, Heidelberg, 2011.](https://link.springer.com/chapter/10.1007/978-3-642-20505-7_28)
* [*"A New Initialization Method and a New Update Operator for Quantum Evolutionary Algorithms in Solving Fractal Image Compression."* In International Conference on Innovative Computing Technology, pp. 401-413. Springer, Berlin, Heidelberg, 2011.](https://link.springer.com/chapter/10.1007/978-3-642-27337-7_38)
* [*"Improvement of the Performance of QEA Using the History of Search Process and Backbone Structure of Landscape."* In International Conference on Innovative Computing Technology, pp. 389-400. Springer, Berlin, Heidelberg, 2011.](https://link.springer.com/chapter/10.1007/978-3-642-27337-7_37)
* [*"A Simulated Annealing inspired update Gate for Quantum Evolutionary Algorithm."*](http://www.academia.edu/download/34535318/A_Simulated_Annealing_inspired_update_Gate_for_Quantum_Evolutionary_Algorithm1.pdf)
* [*"A New Two-Phase Hybrid Evolutionary Algorithm for Fractal Image Compression."*](http://www.academia.edu/download/34535307/2PhaseQEA.pdf)

For running we need:
* Python 3.6 (Anaconda3)
* Numpy
* Matplotlib
* Pandas
* Timeit
* String
* Math
* Inpute file which shoud be with *.txt* extension

List of related Matlab files:
* QEA.py
* Knapsack_quantum.py
* Knapsack_fitness.py
* Knapsack_observe.py
* Knapsack_repair.py

Input files:
* 100.txt (knapsack problem with 100 items)
* 250.txt (knapsack problem with 250 items)
* 500.txt (knapsack problem with 500 items)

Running:
- By running QEA.py function which is the main function of the algorithm the QEA begins. 
- Knapsack_quantum.py is the next important function of the algorithm which runs the QEA baed on the first configurations are done in the main file. 
- Knapsack_observe.py is the function for calculating the binary individuals from probabilities. 
- Knapsack_repair.py repairs the current solution.
- Knapsack_fitness.py produce the fitness based on the selected items. 
- isconvergence.py checks if the probabilities of the individuals are conveged or not.

Output :
- A figure which will be showed in the screen
- "The best answer" which shows the final answer of algorithm
- "Run Timew" which shows the running time of the algorithm

