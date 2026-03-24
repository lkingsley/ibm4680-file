class KeyedFile:
    og_file_name = None
    creation_date = None
    blocks_qty = None
    key_length = None
    record_size = None

    def print(self):
        print('OG file name:', self.og_file_name)
        print('Creation date:', self.creation_date)
        print('Blocks qty:', self.blocks_qty)
        print('Key length:', self.key_length)
        print('Record length:', self.record_size)