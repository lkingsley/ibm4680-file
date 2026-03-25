BLOCK_SIZE = 512


class KeyedFile:
    og_file_name = ''
    creation_date = ''
    blocks_qty = 0
    key_length = 0
    record_size = 0

    def print(self):
        print('OG file name:', self.og_file_name)
        print('Creation date:', self.creation_date)
        print('Blocks qty:', self.blocks_qty)
        print('Key length:', self.key_length)
        print('Record length:', self.record_size)
