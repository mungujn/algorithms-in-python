import unittest
from Chapter4Quicksort import quicksort, countItemsInList, add, removeFirstElement, findMaximumNumber
from Chapter6Search import search, getGraph
from DijkstrasAlgorithm import Dijkstras


class MyTestCase(unittest.TestCase):
    def test_dijkstras(self):
        algorithm = Dijkstras()
        algorithm.findShortestPath()
        print algorithm.printShortestPath("start", "fin")

    def test_breadthFirstSearch(self):
        graph = getGraph()
        last_character_in_name = 'm'
        found = search(graph, last_character_in_name)
        self.assertEquals(found, True)
        last_character_in_name = 'x'
        found = search(graph, last_character_in_name)
        self.assertEquals(found, False)

    def test_quicksort(self):
        items = [5, 3, 8, 20, 55]
        sorted_items = quicksort(items)
        self.assertEquals(sorted_items[0], 3)

    def test_countItemsInList(self):
        items = [1,2,3,4]
        no_of_items = countItemsInList(items)
        self.assertEqual(no_of_items, 4)

    def test_add(self):
        items = [2,4,6]
        sum = add(items)
        self.assertEquals(sum, 12)

    def test_removeFirstElement(self):
        old_list = [2,4,6]
        new_list  = removeFirstElement(old_list)
        self.assertEquals(new_list[0], 4)

    def test_findMaximumNumber(self):
        items = [1, 2, 3, 4]
        maximum = findMaximumNumber(items)
        self.assertEquals(maximum, 4)



if __name__ == '__main__':
    unittest.main()
