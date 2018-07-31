from testLogger import TestLogger   # for error levels


class TestLinkedList:
    """Tests operations on a linked list including """
    """tail operations push & pop, head operations shift & unshift, """
    """random operations get & remove, """
    """list management operations first, last & count"""

    class DefaultClass:
        """Create a dummy class so that tests without a class constructor crash in a predictable way"""
        def __init__(self):
            print("ERROR - TestLinkedList called without a class defined")
            raise TypeError

    # Operations on linked list can require up to 3 different algorithms (i.e. - remove)
    #  1. An empty list
    #  2. Only one element in the list
    #  3. More than one element
    # These permutations are all of the ways that 4 (1 more than 3) items can
    #   be used to increase or decrease the size of the list
    default_permutations = \
        [[0, 1, 2, 3], [0, 1, 3, 2], [0, 2, 1, 3], [0, 2, 3, 1], [0, 3, 1, 2], [0, 3, 2, 1],
         [1, 0, 2, 3], [1, 0, 3, 2], [1, 2, 0, 3], [1, 2, 3, 0], [1, 3, 0, 2], [1, 3, 2, 0],
         [2, 0, 1, 3], [2, 0, 3, 1], [2, 1, 0, 3], [2, 1, 3, 0], [2, 3, 0, 1], [2, 3, 1, 0],
         [3, 0, 1, 2], [3, 0, 2, 1], [3, 1, 0, 2], [3, 1, 2, 0], [3, 2, 0, 1], [3, 2, 1, 0]]

    # Default constructor
    def __init__(self, linked_list_class=None, logger=None, permutations=None):
        if linked_list_class:
            self.list_class = linked_list_class
        else:
            self.list_class = TestLinkedList.DefaultClass
        if logger:
            self.logger = logger
        else:
            self.logger = TestLinkedList.dummy_logger
        if permutations:
            self.test_removal_permutations = permutations
        else:
            self.test_removal_permutations = TestLinkedList.default_permutations
        self.num_permutations = len(self.test_removal_permutations)

    # Methods for specifying test inputs/outputs
    def test_linked_list_assign_type(self, linked_list_class=None):
        self.list_class = linked_list_class

    def test_linked_list_assign_logger(self, logger=None):
        self.logger = logger

    def test_linked_list_assign_permutations(self, permutations=None):
        if permutations is None:
            self.test_removal_permutations = TestLinkedList.default_permutations
        else:
            self.test_removal_permutations = permutations
        self.num_permutations = len(self.test_removal_permutations)

    # Helpers
    @staticmethod
    def int_to_ojb(value: int):
        if value:
            return "obj #"+str(value)
        else:
            return "obj value is None"

    @staticmethod
    def dummy_logger(msg, level):
        pass

    # Tests of each of the operations on a linked list
    def test_push(self):
        """Tests push() by placing things in the list then counting - not a true test"""

        test_push_error_count = 0
        self.logger("... Testing linked list push()", TestLogger.test_log_level_info)

        if self.list_class:
            # create the list to be tested
            UUT = self.list_class()
            # verify that an empty list has 0 elements
            if UUT.count() != 0:
                test_push_error_count += 1
                self.logger("... ERROR: supposed empty list .count() method does not return 0",
                            TestLogger.test_log_level_error)
            # verify that the count of objects is correct after each push (does not verify the object itself
            for i in range(1, 4):
                UUT.push(self.int_to_ojb(i))
                if UUT.count() != i:
                    test_push_error_count += 1
                    self.logger("... ERROR: push("+self.int_to_ojb(i)+") does not result in "+str(i)+" count()",
                                TestLogger.test_log_level_error)
        # done
        self.logger("... Testing linked list push() returning "+str(test_push_error_count)+" errors",
                    TestLogger.test_log_level_info)
        return test_push_error_count

    def test_pop(self):
        """Tests pop() by placing things in order in the list, then removing"""

        test_pop_error_count = 0
        self.logger("... Testing linked list pop()", TestLogger.test_log_level_info)

        # create the list to be tested
        if self.list_class:
            UUT = self.list_class()

            # push 4 things on to it
            for i in range(0, 4):
                pushed = "obj #"+str(i)
                UUT.push(pushed)

            # verify that the things in the list get popped in reverse order
            for i in range(3, -1, -1):
                popped = UUT.pop()
                if popped != "obj #"+str(i):
                    log_str = "... linked list pop() expected obj #"+str(i)+" but received "
                    if popped:
                        log_str += popped
                    else:
                        log_str += "None"
                    self.logger(log_str, TestLogger.test_log_level_error)

            # pop from an empty list, verify None is returned
            if UUT.pop():
                test_pop_error_count += 1
                self.logger("... linked list pop() from empty list did not return None", TestLogger.test_log_level_error)

        # done
        self.logger("... Testing linked list pop() returning "+str(test_pop_error_count)+" errors",
                    TestLogger.test_log_level_info)
        return test_pop_error_count

    def test_shift(self):
        test_shift_error_count = 0
        self.logger("... Testing linked list shift()", TestLogger.test_log_level_info)
        colors = self.list_class()
        colors.shift("Cadmium Orange")
        assert colors.count() == 1

        colors.shift("Carbazole Violet")
        assert colors.count() == 2

        colors.shift("Prussian Blue")
        assert colors.count() == 3
        assert colors.pop() == "Cadmium Orange"
        assert colors.count() == 2
        assert colors.pop() == "Carbazole Violet"
        assert colors.count() == 1
        assert colors.pop() == "Prussian Blue"
        assert colors.count() == 0
        assert colors.pop() is None
        return test_shift_error_count

    def test_unshift(self):
        test_unshift_error_count = 0
        self.logger("... Testing linked list unshift()", TestLogger.test_log_level_info)
        colors = self.list_class()
        colors.push("Viridian")
        colors.push("Sap Green")
        colors.push("Van Dyke")
        assert colors.unshift() == "Viridian"
        assert colors.unshift() == "Sap Green"
        assert colors.unshift() == "Van Dyke"
        assert colors.unshift() is None
        return test_unshift_error_count

    def test_contains(self):
        """Tests that the linked list .count(obj) method works"""
        test_contains_error_count = 0
        self.logger("... Testing lnked list contains(obj)", TestLogger.test_log_level_info)
        colors = self.list_class()
        if 0 != colors.contains("Phtalo_Blue"):
            test_contains_error_count += 1
            self.logger("Phtalo_Blue contained in empty list", TestLogger.test_log_level_error)
        for i in range(0, 4):
            color_count = colors.contains("Phtalo_Blue")
            if i != color_count:
                test_contains_error_count += 1
                error_str = """contains("Phtalo_Blue") should be """+str(i)+" but returned "+color_count
                self.logger(error_str, TestLogger.test_log_level_error)
            if 0 != colors.contains("Alazarin"):
                test_contains_error_count += 1
                self.logger("Alazarin contained in list when not pushed", TestLogger.test_log_level_error)
            colors.push("Phtalo_Blue")
        for i in range(0, 4):
            color_count = colors.contains("Alazarin")
            if i != color_count:
                test_contains_error_count += 1
                error_str = """contains("Alazarin") should be """+str(i)+" but returned "+color_count
                self.logger(error_str, TestLogger.test_log_level_error)
            if 4 != colors.contains("Phtalo_Blue"):
                test_contains_error_count += 1
                self.logger("Phtalo_Blue contains is not 4", TestLogger.test_log_level_error)
            colors.push("Alazarin")
        return test_contains_error_count

    def test_remove(self):
        error_count = 0
        self.logger("... Testing linked list remove(obj)", TestLogger.test_log_level_info)
        UUT = self.list_class()
        UUT.remove(None)    # this should have no effect
        del UUT
        test_strings = ["Zero", "One", "Two", "Three"]
        num_permutations = len(self.test_removal_permutations)
        out_string = "Number of test_removal_permutations is " + str(num_permutations)
        self.logger(out_string, TestLogger.test_log_level_error)
        for push_order in range(0, self.num_permutations):
            # out_string = "Pushing order #"+str(push_order)+" is "+str(self.test_removal_permutations[push_order])
            UUT = self.list_class()
            for remove_order in range(0, num_permutations):
                num_pushes = len(self.test_removal_permutations[push_order])
                out_string = "Pushing order #"+str(push_order)+" is "+str(self.test_removal_permutations[push_order])
                self.logger(out_string, TestLogger.test_log_level_info)
                for j in range(0, num_pushes):
                    UUT.push(test_strings[self.test_removal_permutations[push_order][j]])
                # test that all of the test objects are in the list
                for j in range(0, num_pushes):
                    if 1 != UUT.contains(test_strings[self.test_removal_permutations[push_order][j]]):
                        error_count += 1
                        out_string = "Pushed value not found: "+\
                                     test_strings[self.test_removal_permutations[push_order][j]]
                        self.logger(out_string, TestLogger.test_log_level_error)
                # remove the objects in a specified order, checking to make sure they are not there
                out_string = "Removing order #"+str(remove_order)+": "+str(self.test_removal_permutations[remove_order])
                self.logger(out_string)
                for j in range(0, num_pushes):
                    removal_object = test_strings[self.test_removal_permutations[remove_order][j]]
                    UUT.remove(removal_object)
                    if UUT.contains(removal_object):
                        error_count += 1
                        out_string = "Removed object still in list: " + removal_object
                        self.logger(out_string, TestLogger.test_log_level_error)
            del UUT
        # verify that it removes a list that has all of the same value obj
        UUT = self.list_class()
        for i in range(0, 4):
            UUT.push("Cyan")
        for i in range(3, -1, -1):
            UUT.remove("Cyan")
            num_elements = UUT.count()
            if i != num_elements:
                error_count += 1
                out_string = "Removed "+str(4-i)+" copies of Cyan but list contains "+str(num_elements)
                self.logger(out_string, TestLogger.test_log_level_error)
        del UUT
        return error_count

    def test_first_last(self):
        """Allows user to test first & last (return reference) by reading screen"""
        out_string = "... Testing first & last methods"
        self.logger(out_string, TestLogger.test_log_level_info)
        colors = self.list_class()
        print("colors.first() is ", colors.first())
        print("colors.last() is ", colors.last())
        for i in range(0, 4):
            colors.push(str(i))
            print("colors.first() is ", colors.first())
            print("colors.last() is ", colors.last())
        for i in range(0, 4):
            colors.pop()
            print("colors.first() is ", colors.first())
            print("colors.last() is ", colors.last())
        return 0

    def test_get(self):
        """Tests the get(index)"""
        test_get_error_count = 0
        out_string = "... Testing SingleLinkedList get"
        self.logger(out_string, TestLogger.test_log_level_info)
        colors = self.list_class()
        # Test empty list
        for i in range(-1, 2, 1):
            if colors.get(i) is not None:   # is not None for emphasis
                test_get_error_count += 1
                out_string = "colors.get("+str(i)+") from empty list did not return None"
                self.logger(out_string, TestLogger.test_log_level_error)
        # Test a list that only contains one object, Phtalo Blue
        colors.push("Phtalo Blue")
        if colors.get(0) != "Phtalo Blue":
            test_get_error_count += 1
            out_string = """colors.get(0) failed to return "Phtalo Blue" """
            self.logger(out_string, TestLogger.test_log_level_error)
        if colors.get(-1) is not None:  # is not None for emphasis
            test_get_error_count += 1
            out_string = """colors.get(-1) from list {"Phtalo Blue",None} did not return None """
            self.logger(out_string, TestLogger.test_log_level_error)
        if colors.get(1) is not None:   # is not None for emphasis
            test_get_error_count += 1
            out_string = """colors.get(1) from list {"Phtalo Blue",None} did not return None """
            self.logger(out_string, TestLogger.test_log_level_error)
        # Test list that contains two objects, Phtalo Blue and Alazarin
        colors.push("Alazarin")
        if colors.get(0) != "Phtalo Blue":
            test_get_error_count += 1
            out_string = """colors.get(0) failed to return "Phtalo Blue" """
            self.logger(out_string, TestLogger.test_log_level_error)
        if colors.get(1) != "Alazarin":
            test_get_error_count += 1
            out_string = """colors.get(1) failed to return "Alazarin" """
            self.logger(out_string, TestLogger.test_log_level_error)
        if colors.get(-1) is not None:  # is not None for emphasis
            test_get_error_count += 1
            out_string = """colors.get(-1) from list {"Phtalo Blue",None} did not return None """
            self.logger(out_string, TestLogger.test_log_level_error)
        if colors.get(2) is not None:   # is not None for emphasis
            test_get_error_count += 1
            out_string = """colors.get(1) from list {"Phtalo Blue",None} did not return None """
            self.logger(out_string, TestLogger.test_log_level_error)
        # Test a list with 3 objects Phtalo Blue, Alazarin, Cadmium Orange
        colors.push("Cadmium Orange")
        if colors.get(0) != "Phtalo Blue":
            test_get_error_count += 1
            out_string = """colors.get(0) failed to return "Phtalo Blue" """
            self.logger(out_string, TestLogger.test_log_level_error)
        if colors.get(1) != "Alazarin":
            test_get_error_count += 1
            out_string = """colors.get(1) failed to return "Alazarin" """
            self.logger(out_string, TestLogger.test_log_level_error)
        if colors.get(2) != "Cadmium Orange":
            test_get_error_count += 1
            out_string = """colors.get(2) failed to return "Cadmium Orange" """
            self.logger(out_string, TestLogger.test_log_level_error)
        if colors.get(-1) is not None:  # is not None for emphasis
            test_get_error_count += 1
            out_string = """colors.get(-1) from list {"Phtalo Blue","Alazarin","Cadmium Orange",None}"""+\
                         """"did not return None"""
            self.logger(out_string, TestLogger.test_log_level_error)
        if colors.get(3) is not None:   # is not None for emphasis
            test_get_error_count += 1
            out_string = """colors.get(3) from list {"Phtalo Blue","Alazarin","Cadmium Orange",None}"""+\
                         """did not return None"""
            self.logger(out_string, TestLogger.test_log_level_error)
        return test_get_error_count

    def test_all(self):
        """Runs all defined tests & returns the number of errors"""
        if self.list_class == self.DefaultClass:
            print("Could not run test on invalid class")
            raise TypeError
            return None
        else:
            master_error_count = 0
            master_error_count += self.test_push()
            master_error_count += self.test_pop()
            master_error_count += self.test_shift()
            master_error_count += self.test_unshift()
            master_error_count += self.test_contains()
            master_error_count += self.test_remove()
            master_error_count += self.test_first_last()
            master_error_count += self.test_get()
            return master_error_count
    # end of class TestLinkedList
