class SingleLinkedListNode(object):
    """A node in a singly linked list"""
    def __init__(self, value=None, nxt=None):
        self.value = value
        self.nxt = nxt

    def __repr__(self):
        return "{}->{}".format(self.value, repr(self.nxt))


class SingleLinkedList(object):

    debug_level_none = 0

    def __init__(self, dbg_lvl=0):
        self.begin = None
        self.end = None
        self.debug_level = dbg_lvl
        if self.debug_level > self.debug_level_none:
            self.debug("After constructor")

    def push(self, obj):
        """Appends a new value on the end of the list"""
        if obj:
            if self.begin is None:
                # is this the head of the list?
                self.begin = SingleLinkedListNode(obj, None)
                self.end = self.begin
            else:
                # find the end of the list
                nval = self.begin
                while nval.nxt is not None:
                    nval = nval.nxt
                nval.nxt = SingleLinkedListNode(obj, None)
                self.end = nval.nxt
        if self.debug_level > self.debug_level_none:
            if obj:
                dbg_str = "After push(" + obj + ")"
            else:
                dbg_str = "push(None) ignored"
            self.debug(dbg_str)

    def pop(self):
        """Removes the last item from the list and returns it"""
        return_value = None
        if self.begin:  # not an empty list
            if self.begin.nxt is None:    # only one element
                return_value = self.begin.value
                self.begin.value = None
                self.begin = None
                self.end = None
            else:
                nval = self.begin
                # search for 2nd to last element
                while nval.nxt.nxt is not None:
                    nval = nval.nxt
                return_value = nval.nxt.value
                nval.nxt.value = None   # erase value
                nval.nxt = None
                self.end = nval
        if self.debug_level > self.debug_level_none:
            if return_value:
                dbg_str = "pop() returning " + return_value
            else:
                dbg_str = "pop() from empty list returning None"
            self.debug(dbg_str)
        return return_value

    def shift(self, obj):
        """Adds an item to the front of the list"""
        if obj:
            # if the list is empty, put the item at the begin (head)
            # otherwise, crate a new object and make it the head
            if self.begin is None:
                self.begin = SingleLinkedListNode(obj)
                self.end = self.begin
                self.begin.nxt = None
            else:
                old_head = self.begin
                self.begin = SingleLinkedListNode(obj)
                self.begin.nxt = old_head
        if self.debug_level > self.debug_level_none:
            if obj:
                dbg_str = "shift(" + obj + ")"
            else:
                dbg_str = "shift(None) ignored"
            self.debug(dbg_str)

    def unshift(self):
        """Removes the first item from the list & returns it"""
        # if the list is empty, return None
        # if the list has one element, set the begin & end pointers to None
        # if the list has more than one element, set the begin pointer to begin->next
        return_value = None
        if self.begin is not None:
            return_value = self.begin.value
            old_head = self.begin
            self.begin = self.begin.nxt
            if self.begin is None:
                self.end = None
            old_head.value = None
            old_head.nxt = None
        if self.debug_level > self.debug_level_none:
            if return_value:
                dbg_str = "unshift() returning " + return_value
            else:
                dbg_str = "unshift() from empty list returning None"
            self.debug(dbg_str)
        return return_value

    def remove(self, obj):
        """Finds a matching item and removes it (not all matching items, just one)"""
        if obj is None:
            dbg_str = "remove(None) ignored"
        else:
            dbg_str = "remove(" + obj + ") from empty list"
            # if the list is not empty
            if self.begin is not None:
                # if it is the first object, the head pointer will need to be updated
                if self.begin.value == obj:     # remove the first object
                    # self.unshift()
                    old_head = self.begin   # remember where the head is
                    self.begin = self.begin.nxt
                    # if the list will be empty
                    if self.begin is None:
                        self.end = None
                    old_head.value = None   # erase the old head
                    old_head.nxt = None
                    dbg_str = "remove(" + obj + ") from start of list"
                else:
                    nval = self.begin
                    # while there is another node and it is not the searched for value
                    while nval.nxt and nval.nxt.value != obj:
                        nval = nval.nxt
                    if nval.nxt:
                        # if exited loop because of match
                        if nval.nxt == self.end:    # if we are removing end
                            self.end = nval
                        deleted_node = nval.nxt
                        nval.nxt = deleted_node.nxt
                        deleted_node.value = None
                        deleted_node.nxt = None
                        dbg_str = "remove(" + obj +") from list"
                    else:
                        dbg_str = "remove(" + obj +") not found in list"
        if self.debug_level > self.debug_level_none:
            self.debug(dbg_str)

    def first(self):
        """Returns a *reference* to the first item"""
        return id(self.begin)

    def last(self):
        """Returns a *reference* to the last item"""
        return id(self.end)

    def count(self):
        """Returns the number of elements in the list"""
        retVal = 0
        nval = self.begin
        while nval and nval.value:
            retVal += 1
            nval = nval.nxt
        return retVal

    def get(self, index):
        """Returns the value at [index] (None) if index is >= count"""
        if index < 0 or index >= self.count():
            return None
        elif self.begin is None:
            return None
        else:
            nval = self.begin
            while index:
                nval = nval.nxt
                index -= 1
            return nval.value

    def contains(self, obj):
        """Counts the number of occurrences of obj in list"""
        count = 0
        nde = self.begin
        while nde:
            if nde.value == obj:
                count += 1
            nde = nde.nxt
        return count

    def dump(self, msg=""):
        """Dumps the contents of the list"""
        print(msg, end="")
        print(" list contains {} elements from {} to {}: ".format(self.count(), id(self.begin), id(self.end)), end="")
        if self.begin:
            print("{}->{}".format(self.begin.value, self.begin.nxt))
        else:
            print()

    def debug(self, msg=""):
        if self.debug_level > self.debug_level_none:
            self.dump(msg)
    #   End of definition of singly linked list class


class DoubleLinkedListNode(object):

    def __init__(self, value=None, nxt=None, prv=None):
        self.value = value
        self.nxt = nxt
        self.prv = prv

    def __repr__(self):
        # don't do format(self.prv, self.value, repr(self.nxt))
        #  b/c the repr(self.nxt) will try to do a repr(self.prv), which is self.nxt, which is an infinite loop
        return "{}<-{}->{}".format(id(self.prv), self.value, repr(self.nxt))


class DoubleLinkedList(object):

    debug_level_none = 0

    def __init__(self, dbg_lvl=0):
        self.begin = None
        self.end = None
        self.debug_level = dbg_lvl

    def push(self, value):
        """Pushes one element into the list"""
        if self.end:  # not an empty list
            prv_end = self.end
            node = DoubleLinkedListNode(value, nxt=None, prv=self.end)
            self.end.nxt = node
            self.end = self.end.nxt
        else:
            self.begin = DoubleLinkedListNode(value, nxt=None, prv=None)
            self.end = self.begin

    def pop(self):
        """Returns (and deletes) the final element in the list"""
        return_value = None
        if self.end:    # is not an empty list
            return_value = self.end.value
            if self.end.prv: # there is an element that is previous
                p_old = self.end
                self.end = self.end.prv
                self.end.nxt = None
                # garbage collector should do this, but I will be pendantic
                p_old.value = None
                p_old.nxt = None
                p_old.prv = None
            else:   # deleted only element in list
                self.end = None
                self.begin = None
        return return_value

    def shift(self, value):
        """Adds an element to the beginning of the list"""
        if self.begin:
            #        begin
            # None  <-Bob-> ...
            self.begin.prv = DoubleLinkedListNode(value, nxt=self.begin, prv=None)
            #                                      begin
            # Bob points to None:           None  <-Bob-> ...
            # Alice points to Bob:  None <-Alice->  Bob-> ...
            self.begin.prv.nxt = self.begin
            #                                      begin
            # Bob points to Alice:  None <-Alice-><-Bob->
            #
            self.begin = self.begin.prv
            # begin
            # Alice-><-Bob-> ...
        else:
            # begin
            # None
            self.begin = DoubleLinkedListNode(value, nxt=None, prv=None)
            #       begin
            # None <-Bob-> None
            self.end = self.begin
        self.dump("After shift "+value+": ")

    def count(self):
        """Counts the number of elements in the list"""
        cnt = 0
        now = self.begin
        while now:
            cnt += 1
            now = now.nxt
        return cnt

    # dump does not qualify against self.debug_level b/c if it is being called the user wants to see
    def dump(self, msg=""):
        print(msg, end="")
        print(" list contains {} elements from {} to {}: ".format(self.count(), id(self.begin), id(self.end)), end="")
        p = self.begin
        while p:
            print("[{}<-{}->{}]".format(id(p.prv), p.value, id(p.nxt)), end=", ")
            p = p.nxt
        print()
