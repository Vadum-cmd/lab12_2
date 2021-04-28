"""
Queue to stack converter.
"""
from arrayqueue import ArrayQueue
from arraystack import ArrayStack


def queue_to_stack(queue: ArrayQueue):
    """Convert queue to stack."""
    result_stack = ArrayStack()
    temp_stack = ArrayStack()
    # # Queue is a FIFO, so all we need is to pop first el from Queue
    # # and push it into our new Stack.
    # Okay, I really need to read questions carefully.
    while len(queue) != 0:
        temp_stack.push(queue.pop())
    while len(temp_stack) != 0:
        result_stack.push(temp_stack.pop())
    return result_stack


if __name__ == '__main__':
    queue = ArrayQueue()
    stack = ArrayStack()
    for i in range(12):
        queue.add(i)
        stack.push(i)
    print(queue)
    print(stack)
    print(queue_to_stack(queue))
