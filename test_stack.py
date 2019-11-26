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

        def add_batch_to_stack(stack: Stack, start_key: int, num_elements: int):
            for i in range(start_key, num_elements):
                stack.push(i, i*10)


        # arrange
        specimen = Stack()

        stream1 = Thread(target=add_batch_to_stack, name='1st_stack_processor', args=(specimen, 1, 10000))
        stream2 = Thread(target=add_batch_to_stack, name='2nd_stack_processor', args=(specimen, 11000, 10000))

        # act
        stream1.start()
        stream2.start()

        stream1.join()
        stream1.join()

        # assert
        self.assertEquals(specimen.NodeCount, 20000)
