Recoverable Robustness Analysis of Power Distribution Systems
---------------------------------------------------------------------------------------------------------
Adaptation/Extension of the PySDAL library for simulating the power flow of a power distribution network.
Find details in this paper:
Fosso Olav B 2020 PyDSAL - Python Distribution System Analysis Library - IEEE POWERCON

To start the program and analyse the power loss for the IEEE-69 network please use DistFlow
python DistLoadFlow

The output is the active and reactive power loss of the example system. 

This program extension is an initial state and will be developed towards a network-based resilience analysis.


### What It Does:
- Initializes the IEEE 69-bus distribution system with predefined buses and lines.
- Simulates a disruption on a specific line.
- Runs a local search optimization to find the best configuration of the network.
- Outputs the results, including the number of connected buses and the status of priority nodes before and after optimization.

## Function Overview

### `test_single_disruption(RootList, BusList, LineList, disrupted_index)`

This function:
- Builds the initial graph based on the system configuration.
- Simulates a line disruption and adjusts the network switches defined in mask accordingly.
- Optimizes the network using a local search algorithm.
- Outputs the number of connected buses and priority nodes before and after optimization.

### generate_latex_table_with_optimization(LineList, RootList, BusList)

 Description:
 The `generate_latex_table_with_optimization` function generates a LaTeX    
 table that provides an optimized ranking of network lines based on a       
 simulated recoverable robustness performs a local search        
 optimization, simulating a disruption on each line one at a time, and then 
 sorts the results by the total aggregated score (in ascending order) and   
 by the line index.                                                         

 Table Columns:
 The generated LaTeX table includes the following columns:                  
 - **Line Index:** The index of the line being analyzed.                    
 - **Line FBus:** The "from" bus of the line.                               
 - **Line TBus:** The "to" bus of the line.                                 
 - **Number of Connected Priority Nodes:** The number of priority nodes     
   connected to the line.                                                   
 - **Total Number of Connected Nodes:** The total number of nodes connected 
   to the line.                                                             
 - **Aggregated Score:** A calculated score based on the formula:           
   `Aggregated Score = 5 * Number of Connected Priority Nodes +             
   (Total Connected Nodes - Number of Connected Priority Nodes)`            
   This score helps in prioritizing lines with higher importance based on   
   their connected nodes.                                                   

 Parameters:                                                                
 - `LineList` (list): A list containing all the lines in the network.       
 - `RootList` (list): A list containing the root buses of the network.      
 - `BusList` (list): A list containing all the buses in the network.        

 Returns:                                                                   
 - `str`: A string containing the LaTeX formatted table, which can be       
   directly used in LaTeX documents.                                        

 Example Usage:
 ```python                                                                  
 latex_table = generate_latex_table_with_optimization(LineList, RootList,   
 BusList)                                                                   
 print(latex_table)                                                         
 This function is particularly useful in power network analysis, where
 prioritization of lines based on their importance can significantly impact the network's resilience and optimization.

## Contributing

If you would like to contribute to this project, please fork the repository and use a feature branch. Pull requests are warmly welcome.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For any inquiries or issues, please contact emmerix@gmail.com
