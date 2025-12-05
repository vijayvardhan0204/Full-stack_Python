<!-- Reasons to implement stacks using lists/arrays: -->

1. Memory Efficient: Array elements do not hold the next elements address like linked list nodes do.
2. Easier to implement and understand: Using arrays to implement stacks require less code than using linked lists, and for this reason it is typically easier to understand as well.

<!-- A reason for not using arrays to implement stacks: -->

1. Fixed size: An array occupies a fixed part of the memory. This means that it could take up more memory than needed, or if the array fills up, it cannot hold more elements.


<!-- A reason for using linked lists to implement stacks: -->

1. Dynamic size: The stack can grow and shrink dynamically, unlike with arrays.

<!-- Reasons for not using linked lists to implement stacks: -->

1. Extra memory: Each stack element must contain the address to the next element (the next linked list node).
2. Readability: The code might be harder to read and write for some because it is longer and more complex.

<!-- Common Stack Applications -->

Stacks are used in many real-world scenarios:

1. Undo/Redo operations in text editors
2. Browser history (back/forward)
3. Function call stack in programming
4. Expression evaluation
