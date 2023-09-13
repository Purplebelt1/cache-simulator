class read_item:
    def __init__(self, is_hit = 0, addr, replace_loc = None):
        self.is_hit = is_hit
        self.addr = int(addr)
        self.replace_loc = replace_loc

    def get_is_hit(self):
        return self.is_hit
    def get_addr(self):
        return self.addr
    def get_replace_loc(self):
        return self.replace_loc
    def set_is_hit(self, bit):
        self.is_hit = bit
        return self.is_hit
    def set_addr(self,addr):
        self.addr = addr
        return self.addr
    def set_replace_loc(self,location):
        self.replace_loc = location
        return self.replace_loc
