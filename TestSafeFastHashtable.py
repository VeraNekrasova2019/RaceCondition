import unittest
from threading import Thread

from FastHashtable import FastHashtable


class MyTestCase(unittest.TestCase):
    def test_addValuesToHashtable_expectingNodeCountIncrease(self):

        specimen = FastHashtable()

        specimen.add(1, 2)

        self.assertEqual(specimen.node_count, 1)

    def test_addIncorrectValueType_expectNotAdded(self):

        specimen = FastHashtable()

        result = specimen.add("1", "2")

        self.assertEqual(result, False)
        self.assertEqual(specimen.NodeCount, 0)

    def test_addElementsIntoThreads_ExpectIntegrity(self):
        def add_batch_to_hashtable(hashTable: FastHashtable, start_index: int, num_elements: int):
            for i in range(start_index, num_elements):
                hashTable.add(i, i * 10)

        specimen = FastHashtable()

        stream1 = Thread(target=add_batch_to_hashtable, name='1st_stack_processor', args=(specimen, 0, 10000))
        stream2 = Thread(target=add_batch_to_hashtable, name='2st_stack_processor', args=(specimen, 10000, 20000))

        stream1.start()
        stream2.start()

        stream1.join()
        stream2.join()

        self.assertEqual(specimen.node_count, 20000)

    def test_addElementsIntoThreads_ExpectIntegrityAndFast(self):
        def add_batch_to_hashtable(hashTable: FastHashtable, start_index: int, num_elements: int):
            for i in range(start_index, num_elements, 3):
                hashTable.add(i, i * 10)

        specimen = FastHashtable()

        stream1 = Thread(target=add_batch_to_hashtable, name='1st_stack_processor', args=(specimen, 0, 20000))
        stream2 = Thread(target=add_batch_to_hashtable, name='2st_stack_processor', args=(specimen, 1, 20000))
        stream3 = Thread(target=add_batch_to_hashtable, name='3st_stack_processor', args=(specimen, 2, 20000))

        stream1.start()
        stream2.start()
        stream3.start()

        stream1.join()
        stream2.join()
        stream3.join()

        self.assertEqual(specimen.node_count, 20000)