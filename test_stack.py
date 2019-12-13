from threading import Thread
from unittest import TestCase

from Stack import Stack


class TestStack(TestCase):
    def test_pushAndPopCorrectValues_ExpectGettingThemBack(self):
        """
        Lets try some python unit testing, shall we?
        """
        # arrange
        specimen = Stack()

        # act
        specimen.push(1, 10)
        specimen.push(2, 20)
        specimen.push(3, 30)

        # assert
        output = specimen.pop()
        self.assertEqual(output.key, 3)
        self.assertEqual(output.value, 30)

        output = specimen.pop()
        self.assertEqual(output.key, 2)
        self.assertEqual(output.value, 20)

        output = specimen.pop()
        self.assertEqual(output.key, 1)
        self.assertEqual(output.value, 10)

    def test_PushIncorrectValues_ExpectConversion(self):
        """
        Its called defensive programming - assume someone will use your code in a wrong manner
        """

        # arrange
        specimen = Stack()

        # act
        result = specimen.push("1", "10")

        self.assertEqual(result, False)

    def test_InsertNodesInThreads_ExpectIntegrityMaintained(self):

        def add_batch_to_stack(stack: Stack, start_index: int, num_elements: int):
            for i in range(start_index, num_elements):
                stack.push(i, i * 10)

        # arrange
        specimen = Stack()

        stream1 = Thread(target=add_batch_to_stack, name='1st_stack_processor', args=(specimen, 0, 1000))
        stream2 = Thread(target=add_batch_to_stack, name='2st_stack_processor', args=(specimen, 1000, 2000))

        # act
        stream1.start()
        stream2.start()

        stream1.join()
        stream2.join()

        # assert
        self.assertEquals(specimen.NodeCount, 2000)

    def test_PopNodesInThreads_ExpectIntegrityMaintained(self):

        def add_batch_to_stack(stack: Stack, start_index: int, num_elements: int):
            for i in range(start_index, num_elements):
                stack.push(i, i * 10)

        def pop_batch_from_stack(stack: Stack, start_index: int, num_elements: int):
            for i in range(start_index, num_elements):
                stack.pop()

        # arrange
        specimen = Stack()

        elements_count = 20000

        add_batch_to_stack(specimen, 0, elements_count)

        stream1 = Thread(target=pop_batch_from_stack, name='1st_stack_processor', args=(specimen, 0, int(elements_count/2)))
        stream2 = Thread(target=pop_batch_from_stack, name='2st_stack_processor', args=(specimen, int(elements_count/2),
                                                                                        int(elements_count)))

        # act
        stream1.start()
        stream2.start()

        stream1.join()
        stream2.join()

        # assert
        self.assertEquals(specimen.NodeCount, 0)