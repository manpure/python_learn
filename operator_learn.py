from operator import itemgetter
from itertools import groupby

small_disk = []
medium_disk = []
large_disk = []

raidinfo = [{"device_id":"32","slot_number":"0","raw_size":279,"media_type":"HDD"},
{"device_id":"32","slot_number":"1","raw_size":579,"media_type":"HDD"},
{"device_id":"32","slot_number":"2","raw_size":279,"media_type":"HDD"},
{"device_id":"32","slot_number":"3","raw_size":579,"media_type":"HDD"},
{"device_id":"32","slot_number":"4","raw_size":579,"media_type":"HDD"}]

raidinfo.sort(key=itemgetter('raw_size'))
groups = groupby(raidinfo, itemgetter('raw_size'))

for i, (k, g) in enumerate(groups):
    for x in g:
        if i == 0:
            small_disk.append(x['slot_number'])
        elif i == 1:
            medium_disk.append(x['slot_number'])
        #elif i == 2:
        #    large_disk.append(x['slot_number'])

print(small_disk)
print(medium_disk)

#####output####
# ['0', '2']
# ['1', '3', '4']
