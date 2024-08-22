Resilience analysis of Power Distribution Systems
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

## Contributing

If you would like to contribute to this project, please fork the repository and use a feature branch. Pull requests are warmly welcome.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For any inquiries or issues, please contact emmerix@gmail.com
