import numpy as np
from random import random
import matplotlib.pyplot as plt
from Operations import *
from IEEE69BusDist import *
from DistribObjects import *
from DistribObjects import Bus, Line
from LocalSearchSimple import local_search_with_mask, objective_weighted_sum


# Buses and loads
Bus1 = Bus(1, 0, 0,priority=1) # high priority bus, generator
Bus2= Bus(2, 0,	0)
Bus3 = Bus(3, 0, 0)
Bus4 = Bus(4, 0, 0)
Bus5 = Bus(5, 0, 0)
Bus6 = Bus(6, 0.0026,	0.0022)
Bus7 = Bus(7, 0.0404,	0.03)
Bus8 = Bus(8, 0.075,	0.054)
Bus9 = Bus(9, 0.03,	0.022)
Bus10 = Bus(10, 0.028,	0.019)
Bus11 = Bus(11, 0.145,	0.104)
Bus12 = Bus(12, 0.145,	0.104)
Bus13 = Bus(13, 0.008,	0.0055)
Bus14 = Bus(14, 0.008,	0.0055)
Bus15 = Bus(15, 0,	0)
Bus16 = Bus(16, 0.0455,	0.03)
Bus17 = Bus(17, 0.06,	0.035)
Bus18 = Bus(18, 0.06,	0.035)
Bus19 = Bus(19, 0,	0)
Bus20 = Bus(20, 0.001,	0.0006)
Bus21 = Bus(21, 0.114,	0.081)
Bus22 = Bus(22, 0.0053,	0.0035)
Bus23 = Bus(23, 0,	0)
Bus24 = Bus(24, 0.028,	0.02)
Bus25 = Bus(25, 0,	0)
Bus26 = Bus(26, 0.014,	0.01)
Bus27 = Bus(27, 0.014,	0.01)
Bus28 = Bus(28, 0.026,	0.0186)
Bus29 = Bus(29, 0.026,	0.0186)
Bus30 = Bus(30, 0,	0)
Bus31 = Bus(31, 0,	0)
Bus32 = Bus(32, 0,	0, priority=1) # high priority bus
Bus33 = Bus(33, 0.014,	0.01)
Bus34 = Bus(34, 0.0195,	0.014)
Bus35= Bus(35, 0.006,	0.004)
Bus36 = Bus(36, 0.026,	0.01855)
Bus37 = Bus(37, 0.026,	0.01855)
Bus38 = Bus(38, 0, 0)
Bus39 = Bus(39, 0.024,	0.017)
Bus40 = Bus(40, 0.024,	0.017)
Bus41 = Bus(41, 0.0012,	0.001)
Bus42 = Bus(42, 0.0,	0.0)
Bus43 = Bus(43, 0.006,	0.0043)
Bus44 = Bus(44, 0.0,	0.0)
Bus45 = Bus(45, 0.03922,	0.0263)
Bus46 = Bus(46, 0.03922,	0.0263)
Bus47 = Bus(47, 0.00,	0.00)
Bus48 = Bus(48, 0.079,	0.0564)
Bus49 = Bus(49, 0.3847,	0.2745)
Bus50 = Bus(50, 0.384,	0.2745)
Bus51 = Bus(51, 0.0405,	0.0283)
Bus52 = Bus(52, 0.0036,	0.0027)
Bus53 = Bus(53, 0.00435,	0.0035)
Bus54 = Bus(54, 0.0264,	0.019)
Bus55 = Bus(55, 0.024,	0.0172)
Bus56 = Bus(56, 0,	0)
Bus57 = Bus(57, 0,	0)
Bus58 = Bus(58, 0,	0) # high priority bus
Bus59 = Bus(59, 0.1,	0.072, iloss = 0)
Bus60 = Bus(60, 0,	0)
Bus61 = Bus(61, 1.244,	0.888, iloss = 0)
#Bus61 = Bus(61, 1.244,	-0.4353, vset=0.0)
Bus62 = Bus(62, 0.032,	0.023)
Bus63 = Bus(63, 0,	0)
Bus64 = Bus(64, 0.227,	0.162)
Bus65 = Bus(65, 0.059,	0.042, iloss = 0)
#Bus65 = Bus(65, -1.4,	0.042)
Bus66 = Bus(66, 0.018,	0.013)
Bus67 = Bus(67, 0.018,	0.013)
Bus68 = Bus(68, 0.028,	0.02, priority=1)
Bus69 = Bus(69, 0.028,	0.02)


BusList = [Bus1, Bus2, Bus3, Bus4, Bus5, Bus6, Bus7, Bus8, Bus9, Bus10,
           Bus11, Bus12, Bus13, Bus14, Bus15, Bus16, Bus17, Bus18, Bus19, Bus20,
           Bus21, Bus22, Bus23, Bus24, Bus25, Bus26, Bus27, Bus28, Bus29, Bus30, Bus31, Bus32, Bus33,
           Bus34, Bus35, Bus36, Bus37, Bus38, Bus39, Bus40, Bus41, Bus42, Bus43,
           Bus44, Bus45, Bus46, Bus47, Bus48, Bus49, Bus50, Bus51, Bus52, Bus53,
           Bus54, Bus55, Bus56, Bus57, Bus58, Bus59, Bus60, Bus61, Bus62, Bus63, Bus64, Bus65, Bus66,
           Bus67, Bus68, Bus69]

# Lines, connections and impedances
L1 = Line(1,	2,	3.11963E-06,	7.4871E-06)
L2 = Line(2,	3,	3.11963E-06,	7.4871E-06)
L3 = Line(3,	4,	9.35888E-06,	2.24613E-05)
L4 = Line(4,	5,	0.000156605,	0.000183434)
L5 = Line(5,	6,	0.002283567,	0.001162997)
L6 = Line(6,	7,	0.002377779,	0.001211039)
L7 = Line(7,	8,	0.000575259,	0.000293245)
L8 = Line(8,	9,	0.000307595,	0.000156605)
L9 = Line(9,	10,	0.005109948,	0.001688966)
L10 = Line(10,	11,	0.001167988,	0.000431132)
L11 = Line(11, 12, 0.004438605,	0.001466848)
L12 = Line(12, 13, 0.00642643,	0.002121346)
L13 = Line(13, 14, 0.00651378,	0.002152542)
L14 = Line(14, 15, 0.00660113,	0.002181243, ibstat=1)
L15 = Line(15, 16, 0.001226637,	0.000405551, ibstat=1)
L16 = Line(16, 17, 0.002335976,	0.00077242)
L17 = Line(17, 18, 2.93245E-05,	9.9828E-06)
L18 = Line(18,	19,	0.002043979,	0.000675711)
L19 = Line(19, 20, 0.001313987,	0.000430508)
L20 = Line(20, 21, 0.002131329,	0.000704412)
L21 = Line(21, 22, 8.73495E-05,	2.87006E-05)
L22 = Line(22,	23,	0.000992665,	0.000328185)
L23 = Line(23, 24, 0.002160653,	0.000714394)
L24 = Line(24, 25, 0.004671953,	0.001712675)
L25 = Line(25,	26,	0.001927305,	0.000637028)
L26 = Line(26, 27, 0.001080639,	0.000356885)
L27 = Line(3,	28,	2.74527E-05,	6.73839E-05)
L28 = Line(28, 29, 0.000399312,	0.000976443)
L29 = Line(29, 30, 0.002481975,	0.000820462)
L30 = Line(30, 31, 0.000437996,	0.000144751)
L31 = Line(31, 32, 0.002189978,	0.000723753)
L32 = Line(32, 33, 0.005234733,	0.001756974)
L33 = Line(33,	34,	0.010656644,	0.003522682)
L34 = Line(34,	35,	0.009196659,	0.002915603)
L35 = Line(3,	36,	2.74527E-05,	6.73839E-05, ibstat = 1)
L36 = Line(36,	37,	0.000399312,	0.000976443)
L37 = Line(37,	38,	0.000656993,	0.000767428)
L38 = Line(38,	39,	0.000189673,	0.000221493, ibstat = 1)
L39 = Line(39,	40,	1.12307E-05,	1.31024E-05, ibstat=1)
L40 = Line(40,	41,	0.004544048,	0.00530898)
L41 = Line(41,	42,	0.001934168,	0.002260481)
L42 = Line(42,  43,	0.000255809,	0.000298236)
L43 = Line(43,	44,	5.74011E-05,	7.23753E-05)
L44 = Line(44,	45,	0.000679455,	0.000856649)
L45 = Line(45,	46,	5.61533E-06,	7.4871E-06)
L46 = Line(4,	47,	2.12135E-05,	5.24097E-05)
L47 = Line(47,	48,	0.00053096,	0.001299636)
L48 = Line(48,	49,	0.001808135,	0.004424254)
L49 = Line(49,	50,	0.000512867,	0.001254714)
L50 = Line(8,	51,	0.000579003,	0.000295117)
L51 = Line(51,	52,	0.002070808,	0.000695053)
L52 = Line(9,	53,	0.00108563,	0.000552798, ibstat=1)
L53 = Line(53,	54,	0.001266568,	0.000645139)
L54 = Line(54,	55,	0.001773196,	0.00090282, ibstat = 1)
L55 = Line(55,	56,	0.001755102,	0.000894085)
L56 = Line(56,	57,	0.009920412,	0.003329889)
L57 = Line(57,	58,	0.004889702,	0.001640924)
L58 = Line(58,	59,	0.001897981,	0.000627669, ibstat=1)
L59 = Line(59,	60,	0.002408976,	0.00073124)
L60 = Line(60,	61,	0.003166421,	0.001612847)
L61 = Line(61,	62,	0.000607703,	0.000309467, ibstat=1)
L62 = Line(62,	63,	0.000904692,	0.000460457)
L63 = Line(63,	64,	0.004432989,	0.002257986)
L64 = Line(64,	65,	0.006495062,	0.003308052)
L65 = Line(11,	66,	0.001255338,	0.000381218)
L66 = Line(66,	67,	2.93245E-05,	8.73495E-06)
L67 = Line(12,	68,	0.004613304,	0.001524873)
L68 = Line(68,	69,	2.93245E-05,	9.9828E-06)
LL69 = Line(11, 43,	0.0,	1.0E-08, ibstat=0)
LL70 = Line(13, 21,	0.0,	1.0E-08, ibstat=0)
LL71 = Line(15, 41,	0.0,	1.0E-08, ibstat=0)
LL72 = Line(50, 59,	0.0,	1.0E-08, ibstat=0)
LL73 = Line(27, 65,	0.0,	1.0E-08, ibstat=0)

LineList = [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10,
            L11, L12, L13, L14, L15, L16, L17, L18, L19, L20,
            L21, L22, L23, L24, L25, L26, L27, L28, L29, L30, L31, L32,
            L33, L34, L35, L36, L37, L38, L39, L40, L41, L42,
            L43, L44, L45, L46, L47, L48, L49, L50, L51, L52,
            L53, L54, L55, L56, L57, L58, L59, L60, L61, L62, L63, L64,
            L65, L66, L67, L68, LL69, LL70, LL71, LL72, LL73]

RootList = [Bus1]

# Create an example of a bit vector with length 69 and mostly ones
def test_single_disruption(RootList, BusList, LineList, disrupted_index):
    """
    Function to test the effect of a single line disruption and optimize the network configuration.

    Parameters:
    - RootList: List of root buses.
    - BusList: List of all buses in the network.
    - LineList: List of all lines in the network.
    - disrupted_index: Index of the line that is disrupted (1-based index).

    Outputs:
    - Prints the initial and optimized network status including connected buses and priority nodes.
    """

    # Set priorities for buses
    set_priorities(BusList)

    # Build the graph from the initial setup
    graph69 = build_graph(RootList, BusList, LineList)

    # Count the number of connected buses initially
    connected_count = count_connected(graph69)
    print(f"Total connected buses initially: {connected_count}")

    # Count priority 1 and priority 2 nodes initially
    priority_count = count_priorities(graph69)
    print(f"Priority 1 nodes initially: {priority_count[1]}")
    print(f"Priority 2 nodes initially: {priority_count[2]}")

    # ---------------------- Create Bit Vector ----------------------

    # Initialize a bit vector based on the initial line statuses
    bit_vector_69 = [line.ibstat for line in LineList]

    # Output the indices of the initially open switches
    open_switches = [i for i, x in enumerate(bit_vector_69) if x == 0]
    print("Initial open switches:", open_switches)

    # Rebuild the graph with the bit vector applied (initial state)
    graph69 = build_graph(RootList, BusList, LineList, bit_vector_69)

    # Count the connected buses with the current bit vector
    connected_count = count_connected(graph69)
    print(f"Total connected buses after applying bit vector: {connected_count}")

    # Recalculate priorities after applying the bit vector
    priority_count = count_priorities(graph69)
    print(f"Priority 1 nodes: {priority_count[1]}")
    print(f"Priority 2 nodes: {priority_count[2]}")

    # ---------------------- Local Search Optimization ----------------------

    # Create a mask to allow changes only where switches are initially open
    mask = [0] * len(LineList)
    for i in range(len(LineList)):
        if LineList[i].ibstat == 0:
            mask[i] = 1

    # Mark the specified line as disrupted
    LineList[disrupted_index - 1].disrupted = 1
    print(f"Disrupted line index: {disrupted_index}")
    print(f"From bus: {LineList[disrupted_index - 1].fbus}, To bus: {LineList[disrupted_index - 1].tbus}")

    # Perform local search to optimize the network configuration
    optimized_vector, optimized_objective = local_search_with_mask(bit_vector_69, mask, RootList, BusList, LineList)

    # ---------------------- Output the Optimized Results ----------------------

    # Output the optimized bit vector and its objective function value
    print("Optimized bit vector:", optimized_vector)
    print("Length of optimized bit vector:", len(optimized_vector))
    print("Number of closed switches (sum of optimized bit vector):", sum(optimized_vector))
    print("Optimized objective function value:", optimized_objective)

    # Rebuild the graph with the optimized bit vector
    graph69 = build_graph(RootList, BusList, LineList, optimized_vector)

    # Count the connected buses after optimization
    connected_count = count_connected(graph69)
    print(f"Total connected buses after optimization: {connected_count}")

    # Count priority 1 and priority 2 nodes after optimization
    priority_count = count_priorities(graph69)
    print(f"Priority 1 nodes after optimization: {priority_count[1]}")
    print(f"Priority 2 nodes after optimization: {priority_count[2]}")


# Define your RootList, BusList, and LineList here
RootList = [BusList[0]]  # Example setup for the root
disrupted_index = 27  # Example disrupted line index

# Call the test function
#test_single_disruption(RootList, BusList, LineList, disrupted_index)


def generate_latex_table_with_optimization(LineList, RootList, BusList):
    """
    Generates a LaTeX table for the specified lines in the list after running local search optimization,
    simulating a disruption on each line one at a time, and sorting by the total score (lowest first)
    and then by line index.

    Columns:
    - Line Index
    - Line FBus
    - Line TBus
    - Number of Connected Priority Nodes
    - Total Number of Connected Nodes
    - Aggregated Score (5 * Connected Priority Nodes + (Total Connected Nodes - Connected Priority Nodes))

    Parameters:
    - LineList: List of all lines in the network.
    - RootList: List of root buses.
    - BusList: List of all buses in the network.

    Returns:
    - A string containing the LaTeX table.
    """

    results = []

    # Iterate over each line in LineList, simulating a disruption for each
    for i, line in enumerate(LineList):
        # Reset the disruption status for all lines
        for l in LineList:
            l.disrupted = 0

        # Mark the current line as disrupted
        LineList[i].disrupted = 1

        # Initialize the bit vector based on the initial ibstat values
        bit_vector_69 = [line.ibstat for line in LineList]

        # Create a mask to allow changes only where switches are initially open
        mask = [0] * len(LineList)
        for j in range(len(LineList)):
            if LineList[j].ibstat == 0:
                mask[j] = 1

        # Perform local search to optimize the network configuration
        optimized_vector, optimized_objective = local_search_with_mask(bit_vector_69, mask, RootList, BusList, LineList)

        # Reinitialize the switches based on the optimized vector
        for j in range(len(LineList)):
            LineList[j].ibstat = optimized_vector[j]

        # Build the graph with the optimized vector applied
        graph = build_graph(RootList, BusList, LineList, optimized_vector)
        connected_count = count_connected(graph)
        priority_count = count_priorities(graph)

        connected_priority_nodes = priority_count[2]
        aggregated_score = 4 * connected_priority_nodes + connected_count

        # Store the result in a list for sorting later
        results.append((i + 1, line.fbus, line.tbus, connected_priority_nodes, connected_count, aggregated_score))

    # Sort results by aggregated score (ascending) and then by line index (ascending)
    results.sort(key=lambda x: (x[5], x[0]))

    # Header for the LaTeX table
    table = (
        "\\begin{table}[ht]\n"
        "\\centering\n"
        "\\begin{tabular}{|c|c|c|c|c|c|}\n"
        "\\hline\n"
        "Line Index & FBus & TBus & Connected Priority Nodes & Total Connected Nodes & Aggregated Score \\\\\n"
        "\\hline\n"
    )

    # Populate the LaTeX table with sorted results
    for result in results:
        table += f"{result[0]} & {result[1]} & {result[2]} & {result[3]} & {result[4]} & {result[5]} \\\\\n"

    # Footer for the LaTeX table
    table += (
        "\\hline\n"
        "\\end{tabular}\n"
        "\\caption{Network Analysis for Each Line After Optimization (Sorted by Score)}\n"
        "\\label{tab:network_analysis_optimized_sorted}\n"
        "\\end{table}\n"
    )

    return table


# Example usage
latex_table = generate_latex_table_with_optimization(LineList, RootList, BusList)
print(latex_table)
