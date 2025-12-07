from shared import get_manifest

def replace_at_position(s: str, pos: int, value: str):
    return s[:pos] + value + s[pos+1:]

if __name__ == '__main__':
    
    total_split_count = 0
    
    manifest = get_manifest(test_exec=False)

    beam_positions = { manifest[0].find('S') }

    for row in manifest[1:]:
        new_beam_positions = set()
        removable_positions = list()

        for position in beam_positions:
            
            if row[position] == '^':
                total_split_count += 1
                
                removable_positions.append(position)

                new_beam_positions.add(position-1)
                new_beam_positions.add(position+1)

        for position in removable_positions:
            beam_positions.remove(position)

        beam_positions.update(new_beam_positions)

    print('Total split count: ', total_split_count)
    

