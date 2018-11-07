"""Parse Lewis and Short"""
from lxml import etree


def _main():
    # https://github.com/PerseusDL/lexica/issues/31
    parser = etree.XMLParser(no_network=False)
    tree = etree.parse('lat.ls.perseus-eng1.xml', parser)
    for div in tree.getroot().find('text').find('body').findall('div0'):
        for entry in div.findall('entryFree'):
            print(' '.join([a.text for a in entry.findall('orth')]))
            print('\t',
                ' '.join([a.text for a in entry.findall('itype') if a.text]))


if __name__ == '__main__':
    _main()
