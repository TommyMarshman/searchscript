mport xml.etree.ElementTree as ET
import sys
import subprocess
import glob
import os



dir = './58268_3cand/'
for file in glob.iglob(os.path.join(dir, '*/*.xml')):
   with open(file) as f:
      #data = etree.parse(f)
      tree = ET.parse(f)
      root = tree.getroot()

      for search in root.findall('search_parameters'):
        print search.tag, search.attrib
      for node in search.getiterator():
          if node.tag == 'dm_pulse_width':
              dm_pulse_width = float(node.text)
              print dm_pulse_width

      for cand in root.findall('candidates/candidate'):
        print cand.tag, cand.attrib
        for node in cand.getiterator():
             if node.tag == 'period':
                 period = float(node.text)
             elif node.tag == 'dm':
                 dm = float(node.text)
             elif node.tag == 'snr':
                 snr = float(node.text)

        print 'p= {0} dm= {1} dpw= {2} snr= {3}'.format(period, dm, dm_pulse_width, snr)
