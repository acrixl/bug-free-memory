
linux memory report


Shared or *unknown* line show how many RAM shared or lost, if you see (Good) then it ok
if you see (WTF?) then some memory is used for unknown reason by kernel modules
for example ZFS on linux can use memory for caching purpose (or not caching?) and this memory not accounted under cache+buffers
