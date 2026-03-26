BLOCK_SIZE = 512


class KeyedFile:
    og_file_name = ''
    creation_date = ''
    blocks_qty = 0
    key_length = 0
    record_size = 0

    def to_string(self):
        result = 'OG file name: %s\n' \
        'Creation date: %s\n' \
        'Blocks qty: %d\n' \
        'Key length: %d\n' \
        'Record length: %d' % (
            self.og_file_name,
            self.creation_date,
            self.blocks_qty,
            self.key_length,
            self.record_size)
        print(result)
