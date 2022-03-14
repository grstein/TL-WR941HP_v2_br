# TL-WR941HP_v2_br

The backup dir has the separated files:

```
root@TL_WR941HP:/# cat /proc/mtd
dev:    size   erasesize  name
mtd0: 00010000 00010000 "u-boot"
mtd1: 006c0000 00010000 "rootfs"
mtd2: 00030000 00010000 "rootfs_data"
mtd3: 00110000 00010000 "kernel"
mtd4: 00010000 00010000 "mib0"
mtd5: 00010000 00010000 "art"
mtd6: 007d0000 00010000 "firmware"

root@TL_WR941HP:/# cat /proc/partitions 
major minor  #blocks  name

  31        0         64 mtdblock0
  31        1       6912 mtdblock1
  31        2        192 mtdblock2
  31        3       1088 mtdblock3
  31        4         64 mtdblock4
  31        5         64 mtdblock5
  31        6       8000 mtdblock6
```

There is also a one file complete backup called `full_backup.bin`