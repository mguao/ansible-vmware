#!/usr/bin/env python
''' this script will create the inventory file based on the  givin items in the  variables.yaml '''

import yaml

def main():
    ''' main  function '''
    slist = []
    fi = open('variables.yml','r')
    y = yaml.load(fi)
    for x in range(len(y['serverlist'])):
        slist.append(y['serverlist'][x]['networkip'])
    fi.close()

    inv = open('inventory','w')
    inv.write("[provision]")
    inv.write('\n')
    for item in slist:
        inv.write(item)
        inv.write('\n')
    inv.close()


if __name__ == "__main__":
    main()
