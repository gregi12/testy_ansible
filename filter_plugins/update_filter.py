def parse_windows_update(data):
    updates = []
    lines = data.split('\r\n')
    for line in lines:
        parts = line.split()
        if len(parts) > 4 and parts[0] != 'ComputerName':
            update = {
                'name': ' '.join(parts[4:]),
                'kb': parts[2],
                'size': parts[3]
            }
            updates.append(update)
    return updates

class FilterModule(object):
    def filters(self):
        return {
            'parse_windows_update': parse_windows_update
        }
