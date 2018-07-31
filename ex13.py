
from linkedLists import SingleLinkedList
from linkedLists import DoubleLinkedList
from linkedListsTests import TestLinkedList
from testLogger import TestLogger

# class TestLogger:
#     test_log_dst_screen = 1
#     test_log_dst_file = 2
#     test_log_dst_both = 3
#     test_log_level_error = 2
#     test_log_level_warning = 1
#     test_log_level_info = 0
#
#     def __init__(self, file_name="uninitialized", lg_lvl=0):
#         self.test_log_level = lg_lvl
#         if file_name != "uninitialized":
#             self.test_log_file = open(file_name, "w+")
#             self.test_log_file_open = True
#         else:
#             self.test_log_file = None
#             self.test_log_file_open = False
#
#     def set_test_log_level(self, new_level):
#         global test_log_level
#         self.test_log_level = new_level
#
#     def close_test_log(self):
#         if self.test_log_file:
#             self.test_log_file.close()
#         self.test_log_file_open = False
#
#     def open_test_log(self, fname="invalid", level=test_log_level_info):
#         if fname != "invalid":
#             if self.test_log_file_open:
#                 self.test_log_file.close()
#             self.test_log_file = open(fname, "w+")
#             if self.test_log_file.writable():
#                 self.test_log_file_open = True
#             self.test_log_level = level
#
#     def test_log(self, log_str, str_level=test_log_level_info, dst_flags=test_log_dst_both):
#         log_str = log_str + "\n"
#         if str_level >= self.test_log_level:
#             if dst_flags & self.test_log_dst_screen:
#                 print(log_str)
#             if dst_flags & self.test_log_dst_file and self.test_log_file_open:
#                 self.test_log_file.write(log_str)
#
#     def log_to_screen(self, log_str, str_level=0):
#         self.test_log(log_str, str_level, self.test_log_dst_screen)
#
#     def log_to_file(self, log_str, str_level=test_log_level_info):
#         self.test_log(log_str, str_level, self.test_log_dst_file)
#
#     def log_to_both(self, log_str, str_level=test_log_level_info):
#         self.test_log(log_str, str_level, self.test_log_dst_both)
#     # end of class TestLog
#
#
# class TestLinkedList:
#
#     class DefaultClass:
#         def __init__(self):
#             print("ERROR - TestLinkedList called without a class defined")
#             raise TypeError
#
#     default_permutations = \
#         [[0, 1, 2, 3], [0, 1, 3, 2], [0, 2, 1, 3], [0, 2, 3, 1], [0, 3, 1, 2], [0, 3, 2, 1],
#          [1, 0, 2, 3], [1, 0, 3, 2], [1, 2, 0, 3], [1, 2, 3, 0], [1, 3, 0, 2], [1, 3, 2, 0],
#          [2, 0, 1, 3], [2, 0, 3, 1], [2, 1, 0, 3], [2, 1, 3, 0], [2, 3, 0, 1], [2, 3, 1, 0],
#          [3, 0, 1, 2], [3, 0, 2, 1], [3, 1, 0, 2], [3, 1, 2, 0], [3, 2, 0, 1], [3, 2, 1, 0]]
#
#     def __init__(self, linked_list_class=None, logger=None, permutations=None):
#         if linked_list_class:
#             self.list_class = linked_list_class
#         else:
#             self.list_class = TestLinkedList.DefaultClass
#         self.logger = logger
#         if permutations:
#             self.test_removal_permutations = permutations
#         else:
#             self.test_removal_permutations = TestLinkedList.default_permutations
#         self.num_permutations = len(self.test_removal_permutations)
#
#     def test_linked_list_assign_type(self, linked_list_class=None):
#         self.list_class = linked_list_class
#
#     def test_linked_list_assign_logger(self, logger=None):
#         self.logger = logger
#
#     def test_linked_list_assign_permutations(self, permutations=None):
#         if permutations is None:
#             self.test_removal_permutations = TestLinkedList.default_permutations
#         else:
#             self.test_removal_permutations = permutations
#         self.num_permutations = len(self.test_removal_permutations)
#
#     def test_push(self, logger=None):
#         test_push_error_count = 0
#         if logger is not None:
#             logger("... Testing SingleLinkedList push()", TestLogger.test_log_level_info)
#         if self.list_class:
#             colors = self.list_class()
#             colors.push("Pthalo Blue")
#             assert colors.count() == 1
#             colors.push("Magenta")
#             assert colors.count() == 2
#             colors.push("Cobalt")
#             assert colors.count() == 3
#             return test_push_error_count
#
#     def test_pop(self, logger=None):
#         test_pop_error_count = 0
#         if logger:
#             logger("... Testing linked list's pop()", TestLogger.test_log_level_info)
#         UUT = self.list_class()
#         for i in range(0, 4):
#             pushed = "obj #"+str(i)
#             UUT.push(pushed)
#         for i in range(3, -1, -1):
#             popped = UUT.pop()
#             if popped != "obj #"+str(i):
#                 test_pop_error_count += 1
#                 if logger:
#                     log_str = "... linked list pop() expected obj #"+str(i)+" but received "
#                     if popped:
#                         log_str += popped
#                     else:
#                         log_str += "None"
#                     logger(log_str, TestLogger.test_log_level_error)
#         if UUT.pop():
#             test_pop_error_count += 1
#             if logger:
#                 logger("... linked list pop() from empty list did not return None", TestLogger.test_log_level_error)
#         if logger:
#             out_str = "... Testing linked list's pop() returning "+str(test_pop_error_count)+" errors"
#             logger(out_str, TestLogger.test_log_level_info)
#         return test_pop_error_count
#
#     def test_shift(self, logger=None):
#         test_shift_error_count = 0
#         if logger is not None:
#             logger("... Testing SingleLinkedList shift()", TestLogger.test_log_level_info)
#         colors = self.list_class()
#         colors.shift("Cadmium Orange")
#         assert colors.count() == 1
#
#         colors.shift("Carbazole Violet")
#         assert colors.count() == 2
#
#         colors.shift("Prussian Blue")
#         assert colors.count() == 3
#         assert colors.pop() == "Cadmium Orange"
#         assert colors.count() == 2
#         assert colors.pop() == "Carbazole Violet"
#         assert colors.count() == 1
#         assert colors.pop() == "Prussian Blue"
#         assert colors.count() == 0
#         assert colors.pop() is None
#         return test_shift_error_count
#
#     def test_unshift(self, logger=None):
#         test_unshift_error_count = 0
#         if logger is not None:
#             logger("... Testing SingleLinkedList unshift()", TestLogger.test_log_level_info)
#         colors = self.list_class()
#         colors.push("Viridian")
#         colors.push("Sap Green")
#         colors.push("Van Dyke")
#         assert colors.unshift() == "Viridian"
#         assert colors.unshift() == "Sap Green"
#         assert colors.unshift() == "Van Dyke"
#         assert colors.unshift() is None
#         return test_unshift_error_count
#
#     def test_contains(self, logger=None):
#         """Tests that the linked list .count(obj) method works"""
#         test_contains_error_count = 0
#         if logger is not None:
#             logger("... Testing SingleLinkedList contains(obj)", TestLogger.test_log_level_info)
#         colors = self.list_class()
#         if 0 != colors.contains("Phtalo_Blue"):
#             test_contains_error_count += 1
#             if logger:
#                 logger("Phtalo_Blue contained in empty list", TestLogger.test_log_level_error)
#         for i in range(0, 4):
#             color_count = colors.contains("Phtalo_Blue")
#             if i != color_count:
#                 test_contains_error_count += 1
#                 if logger:
#                     error_str = """contains("Phtalo_Blue") should be """+str(i)+" but returned "+color_count
#                     logger(error_str, TestLogger.test_log_level_error)
#             if 0 != colors.contains("Alazarin"):
#                 test_contains_error_count += 1
#                 if logger is not None:
#                     logger("Alazarin contained in list when not pushed", TestLogger.test_log_level_error)
#             colors.push("Phtalo_Blue")
#         for i in range(0, 4):
#             color_count = colors.contains("Alazarin")
#             if i != color_count:
#                 test_contains_error_count += 1
#                 if logger:
#                     error_str = """contains("Alazarin") should be """+str(i)+" but returned "+color_count
#                     logger(error_str, TestLogger.test_log_level_error)
#             if 4 != colors.contains("Phtalo_Blue"):
#                 test_contains_error_count += 1
#                 if logger:
#                     logger("Phtalo_Blue contains is not 4", TestLogger.test_log_level_error)
#             colors.push("Alazarin")
#         return test_contains_error_count
#
#     def test_remove(self, logger=None):
#         error_count = 0
#         if logger:
#             logger("... Testing Single LinkedList remove(obj)", TestLogger.test_log_level_info)
#         colors = self.list_class()
#         colors.remove(None)
#         test_strings = ["Zero", "One", "Two", "Three"]
#         num_permutations = len(self.test_removal_permutations)
#         if logger:
#             out_string = "Number of test_removal_permutations is " + str(num_permutations)
#             logger(out_string, TestLogger.test_log_level_error)
#         for push_order in range(0, self.num_permutations):
#             if logger:
#                 out_string = "Pushing order #"+str(push_order)+" is "+str(self.test_removal_permutations[push_order])
#                 logger(out_string, TestLogger.test_log_level_info)
#             for remove_order in range(0, num_permutations):
#                 num_pushes = len(self.test_removal_permutations[push_order])
#                 for j in range(0, num_pushes):
#                     colors.push(test_strings[self.test_removal_permutations[push_order][j]])
#                 # test that all of the test objects are in the list
#                 for j in range(0, num_pushes):
#                     if 1 != colors.contains(test_strings[self.test_removal_permutations[push_order][j]]):
#                         error_count += 1
#                         if logger:
#                             out_string = "Pushed value not found: " + test_strings[self.test_removal_permutations[push_order][j]]
#                             logger(out_string, TestLogger.test_log_level_error)
#                 # remove the objects in a specified order, checking to make sure they are not there
#                 if logger:
#                     out_string = "Removing order #"+str(remove_order)+": "+str(self.test_removal_permutations[remove_order])
#                     logger(out_string)
#                 for j in range(0, num_pushes):
#                     removal_object = test_strings[self.test_removal_permutations[remove_order][j]]
#                     colors.remove(removal_object)
#                     if colors.contains(removal_object):
#                         error_count += 1
#                         if logger:
#                             out_string = "Removed object still in list: " + removal_object
#                             logger(out_string, TestLogger.test_log_level_error)
#         # verify that it removes a list that has all of the same value obj
#         for i in range(0, 4):
#             colors.push("Cyan")
#         for i in range(3, -1, -1):
#             colors.remove("Cyan")
#             num_elements = colors.count()
#             if i != num_elements:
#                 error_count += 1
#                 if logger:
#                     out_string = "Removed "+str(4-i)+" copies of Cyan but list contains "+num_elements
#                     logger(out_string, TestLogger.test_log_level_error)
#         return error_count
#
#     def test_first_last(self, logger):
#         """Allows user to test first & last (return reference) by reading screen"""
#         if logger:
#             out_string = "... Testing first & last methods"
#             logger(out_string, TestLogger.test_log_level_info)
#         colors = self.list_class()
#         print("colors.first() is ", colors.first())
#         print("colors.last() is ", colors.last())
#         for i in range(0, 4):
#             colors.push(str(i))
#             print("colors.first() is ", colors.first())
#             print("colors.last() is ", colors.last())
#         for i in range(0, 4):
#             colors.pop()
#             print("colors.first() is ", colors.first())
#             print("colors.last() is ", colors.last())
#         return 0
#
#     def test_get(self, logger):
#         """Tests the get(index)"""
#         test_get_error_count = 0
#         if logger:
#             out_string = "... Testing SingleLinkedList get"
#             logger(out_string, TestLogger.test_log_level_info)
#         colors = self.list_class()
#         # Test empty list
#         for i in range(-1, 2, 1):
#             if colors.get(i) is not None:
#                 test_get_error_count += 1
#                 if logger:
#                     out_string = "colors.get("+str(i)+") from empty list did not return None"
#                     logger(out_string, TestLogger.test_log_level_error)
#         # Test a list that only contains one object, Phtalo Blue
#         colors.push("Phtalo Blue")
#         if colors.get(0) != "Phtalo Blue":
#             test_get_error_count += 1
#             if logger:
#                 out_string = """colors.get(0) failed to return "Phtalo Blue" """
#                 logger(out_string, TestLogger.test_log_level_error)
#         if colors.get(-1) is not None:
#             test_get_error_count += 1
#             if logger:
#                 out_string = """colors.get(-1) from list {"Phtalo Blue",None} did not return None """
#                 logger(out_string, TestLogger.test_log_level_error)
#         if colors.get(1) is not None:
#             test_get_error_count += 1
#             if logger:
#                 out_string = """colors.get(1) from list {"Phtalo Blue",None} did not return None """
#                 logger(out_string, TestLogger.test_log_level_error)
#         # Test list that contains two objects, Phtalo Blue and Alazarin
#         colors.push("Alazarin")
#         if colors.get(0) != "Phtalo Blue":
#             test_get_error_count += 1
#             if logger:
#                 out_string = """colors.get(0) failed to return "Phtalo Blue" """
#                 logger(out_string, TestLogger.test_log_level_error)
#         if colors.get(1) != "Alazarin":
#             test_get_error_count += 1
#             if logger:
#                 out_string = """colors.get(1) failed to return "Alazarin" """
#                 logger(out_string, TestLogger.test_log_level_error)
#         if colors.get(-1) is not None:
#             test_get_error_count += 1
#             if logger:
#                 out_string = """colors.get(-1) from list {"Phtalo Blue",None} did not return None """
#                 logger(out_string, TestLogger.test_log_level_error)
#         if colors.get(2) is not None:
#             test_get_error_count += 1
#             if logger:
#                 out_string = """colors.get(1) from list {"Phtalo Blue",None} did not return None """
#                 logger(out_string, TestLogger.test_log_level_error)
#         # Test a list with 3 objects Phtalo Blue, Alazarin, Cadmium Orange
#         colors.push("Cadmium Orange")
#         if colors.get(0) != "Phtalo Blue":
#             test_get_error_count += 1
#             if logger:
#                 out_string = """colors.get(0) failed to return "Phtalo Blue" """
#                 logger(out_string, TestLogger.test_log_level_error)
#         if colors.get(1) != "Alazarin":
#             test_get_error_count += 1
#             if logger:
#                 out_string = """colors.get(1) failed to return "Alazarin" """
#                 logger(out_string, TestLogger.test_log_level_error)
#         if colors.get(2) != "Cadmium Orange":
#             test_get_error_count += 1
#             if logger:
#                 out_string = """colors.get(2) failed to return "Cadmium Orange" """
#                 logger(out_string, TestLogger.test_log_level_error)
#         if colors.get(-1) is not None:
#             test_get_error_count += 1
#             if logger:
#                 out_string = """colors.get(-1) from list {"Phtalo Blue","Alazarin","Cadmium Orange",None}"""+\
#                              """did not return None"""
#                 logger(out_string, TestLogger.test_log_level_error)
#         if colors.get(3) is not None:
#             test_get_error_count += 1
#             if logger:
#                 out_string = """colors.get(3) from list {"Phtalo Blue","Alazarin","Cadmium Orange",None}"""+\
#                              """did not return None"""
#                 logger(out_string, TestLogger.test_log_level_error)
#         return test_get_error_count
#     # end of class TestLinkedList


master_error_count = 0
logger = TestLogger("SingleLinkedListTest.txt")
logger.log_to_both("Testing class SingleLinkedList", logger.test_log_level_always)
tester = TestLinkedList(SingleLinkedList, logger.test_log)
master_error_count += tester.test_push()
master_error_count += tester.test_pop()
master_error_count += tester.test_shift()
master_error_count += tester.test_unshift()
master_error_count += tester.test_contains()
master_error_count += tester.test_remove()
master_error_count += tester.test_first_last()
master_error_count += tester.test_get()
if master_error_count == 0:
    test_out_string = "SingleLinkedList TEST PASSED with "+str(master_error_count)+" errors"
else:
    test_out_string = "SingleLinkedList TEST FAILED with "+str(master_error_count)+" errors"
logger.log_to_both(test_out_string, logger.test_log_level_error)  # force it to be printed
logger.close_test_log()
del tester

master_error_count = 0
logger.open_test_log("DoubleLinkedListTest.txt")
logger.log_to_both("Testing class DoubleLinkedList", logger.test_log_level_always)
tester = TestLinkedList(DoubleLinkedList, logger.test_log)
master_error_count += tester.test_push()
master_error_count += tester.test_pop()
master_error_count += tester.test_shift()
if master_error_count == 0:
    test_out_string = "DoubleLinkedList TEST PASSED with "+str(master_error_count)+" errors"
else:
    test_out_string = "DoubleLinkedList TEST FAILED with "+str(master_error_count)+" errors"
logger.log_to_both(test_out_string, logger.test_log_level_error)  # force it to be printed
logger.close_test_log()

