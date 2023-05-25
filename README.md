# DSA-Python

We are going to see Data Structures and Algorithms paralally and I will use Python language for code implementations.

## Algorithms:

A sequence of finite steps to perform some tasks.

Example : Multiplications of two numbers

Properties of Algorithms:

1. It should terminate after finite amount of times.
2. Produce atleast one output
3. Independent of any programing languages.
4. The output should be deterministic


Steps to construct an Algorithm:

1. Problem definition
2. Design a Algorithm
    a. Divide and Conqure
    b. Greedy Algorithm
    c. Dynamic Programing and many more
3. Draw a flow chart
4. Testing Phase
5. Implementation
6. Analysis


We encountered an issue with our --- client regarding the retrieval of address-related details. Currently, the client does not provide updated address information if the current address has expired. However, there is one mandatory address that we must retrieve, which complicates the process as it requires scanning all previous day partitions. To address this challenge, we have developed a logic that effectively fetches the required address information.

To further optimize this process, we have converted the logic into a Materialized View (MV) and integrated it with the existing Pre DWL table logic. As a result, we have successfully achieved the desired outcome without impacting the existing logics and framework. This enhancement ensures seamless integration and minimal disruption to our operations.
