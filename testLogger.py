class TestLogger:
    test_log_dst_screen = 1
    test_log_dst_file = 2
    test_log_dst_both = 3
    test_log_level_none = 3
    test_log_level_error = 2
    test_log_level_warning = 1
    test_log_level_info = 0

    def __init__(self, file_name="uninitialized", lg_lvl=0):
        self.test_log_level = lg_lvl
        if file_name != "uninitialized":
            self.test_log_file = open(file_name, "w+")
            self.test_log_file_open = True
        else:
            self.test_log_file = None
            self.test_log_file_open = False

    def set_test_log_level(self, new_level):
        self.test_log_level = new_level

    def close_test_log(self):
        if self.test_log_file:
            self.test_log_file.close()
        self.test_log_file_open = False

    def open_test_log(self, fname="invalid", level=test_log_level_info):
        if fname != "invalid":
            if self.test_log_file_open:
                self.test_log_file.close()
            self.test_log_file = open(fname, "w+")
            if self.test_log_file.writable():
                self.test_log_file_open = True
            self.test_log_level = level

    def test_log(self, log_str, str_level=test_log_level_info, dst_flags=test_log_dst_both):
        log_str = log_str + "\n"
        if str_level >= self.test_log_level:
            if dst_flags & self.test_log_dst_screen:
                print(log_str)
            if dst_flags & self.test_log_dst_file and self.test_log_file_open:
                self.test_log_file.write(log_str)

    def log_to_screen(self, log_str, str_level=0):
        self.test_log(log_str, str_level, self.test_log_dst_screen)

    def log_to_file(self, log_str, str_level=test_log_level_info):
        self.test_log(log_str, str_level, self.test_log_dst_file)

    def log_to_both(self, log_str, str_level=test_log_level_info):
        self.test_log(log_str, str_level, self.test_log_dst_both)
    # end of class TestLog
