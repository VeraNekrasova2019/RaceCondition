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

        stream1 = Thread(target=add_batch_to_stack, name='1st_stack_processor', args=(specimen, 1, 100001))
        stream2 = Thread(target=add_batch_to_stack, name='2st_stack_processor', args=(specimen, 100001, 200001))

        # act
        stream1.start()
        stream2.start()

        stream1.join()
        stream2.join()

        # assert
        self.assertEquals(specimen.NodeCount, 200000)

    def test_PopNodesInThreads_ExpectIntegrityMaintained(self):

        def add_batch_to_stack(stack: Stack, start_index: int, num_elements: int):
            for i in range(start_index, num_elements):
                stack.push(i, i * 10)

        def pop_batch_from_stack(stack: Stack, start_index: int, num_elements: int):
            for i in range(start_index, num_elements):
                stack.pop()

        # arrange
        specimen = Stack()

        elements_count_insert = 20000
        elements_count1 = 10000
        elements_count2 = 10001
        add_batch_to_stack(specimen, 1, elements_count_insert)

        stream1 = Thread(target=pop_batch_from_stack, name='1st_stack_processor', args=(specimen, 1, elements_count1))
        stream2 = Thread(target=pop_batch_from_stack, name='2st_stack_processor', args=(specimen, 1, elements_count2))

        # act
        stream1.start()
        stream2.start()

        stream1.join()
        stream2.join()

        # assert
        self.assertEquals(specimen.NodeCount, 0)
