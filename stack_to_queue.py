"""
Stack to queue converter.
"""
from arrayqueue import ArrayQueue
from arraystack import ArrayStack


def stack_to_queue(stack: ArrayStack):
    """Convert stack to queue."""
    queue = ArrayQueue()
    # # Gotta reverse that stack so it would be easier to convert.
    # # Got our stack, but reversed.
    # # Now we are ready to convert.
    # # Now it is in order.
    # Still need read the questions carefully.
    while len(stack) != 0:
        queue.add(stack.pop())
    return queue


if __name__ == "__main__":
    queue = ArrayQueue()
    stack = ArrayStack()
    for i in range(12):
        queue.add(i)
        stack.push(i)
    print(queue)
    print(stack)
    print(stack_to_queue(stack))
