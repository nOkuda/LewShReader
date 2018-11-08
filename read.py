"""Parse Lewis and Short"""
from lxml import etree


def print_verb_pos_only(pos, endswith_int, entry, itype):
    """Print only when verb has pos tag marking it as verb but does not have
    conjugation number
    """
    if (pos is not None and pos.text.strip().startswith('v')) and not endswith_int:
        print(' '.join([a.text for a in entry.findall('orth')]))
        print('\t', itype)
        print('\t', pos.text)


def print_verb_segregated(pos, endswith_int, entry, itype):
    """Print all words, marking all non-verbs differently"""
    if (pos is not None and pos.text.strip().startswith('v')) or endswith_int:
        print(' '.join([a.text for a in entry.findall('orth')]))
        print('\t', itype)
        print('\t', pos.text)
    else:
        print('####', ' '.join([a.text for a in entry.findall('orth')]))
        print('####\t', itype)


def _main():
    # https://github.com/PerseusDL/lexica/issues/31
    parser = etree.XMLParser(no_network=False)
    tree = etree.parse('lat.ls.perseus-eng1.xml', parser)
    for div in tree.getroot().find('text').find('body').findall('div0'):
        for entry in div.findall('entryFree'):
            """
            # ignoring senses leads to problems
            orth = []
            itype = []
            for tmp in entry.iter():
                if tmp.tag == 'orth':
                    orth.append(tmp.text)
                elif tmp.tag == 'itype':
                    itype.append(tmp.text)
            if entry.get('key') == 'vincio':
                for child in entry.iter():
                    if child.tag == 'itype':
                        print(child)
            """
            pos = entry.find('pos')
            itype = ' '.join([a.text for a in entry.findall('itype') if a.text])
            endswith_int = False
            try:
                if itype:
                    int(itype.strip()[-1])
                    endswith_int = True
            except ValueError:
                pass
            print_verb_pos_only(pos, endswith_int, entry, itype)


if __name__ == '__main__':
    _main()
