# Blockchain Micropython Library

A IOT microcontroller blockchain micropython library for EOS, ETH, BITCOIN. Esp32 controllers, St32 and others . For RTOS operating systems . ESP32, ESP8266, ST32 micro controllers .

### Requeriments


### Installation

Use install , to install from 0

`install.sh`

or 

Copy file modules yo your MicroPython ports

Compile



```

cd micropython/ports/esp32

make USER_C_MODULES=/home/raziel/projects/micropython/ports/esp32/boards/GENERIC/ucrypto/micropython.cmake BOARD=CHANGE_YOUR_BOARD  


```


Flash


```

cd build-YOURBOARD

esptool.py --chip esp32 -p /dev/ttyACM0 -b 460800 --before=default_reset --after=hard_reset write_flash --flash_mode dio --flash_freq 40m --flash_size 4MB 0x1000 bootloader/bootloader.bin 0x10000 micropython.bin 0x8000 partition_table/partition-table.bin


```

### Usage


* Install mpremote to connect by serial to your device


```

mpremote cp block.py requests.py :

mp remote


>>> import block

block.get_info()

Address Info:  ('65.21.202.125', 8888)
HTTP/1.1 200 OK
access-control-allow-origin: *
content-length: 839
content-type: application/json
server: WebSocket++/0.7.0
connection: close

{"server_version":"26a4d285","chain_id":"8b6404a00556c4a1ed0257869dbd41c9ba23349590f39eb90fec0eb9382469dd","head_block_num":2016452,"last_irreversible_block_num":2016451,"last_irreversible_block_id":"001ec4c37801042fdfa0e9cb9273a581b2d166348eb33e3413c5aa7bbef27f64","head_block_id":"001ec4c41773e88922737d74b2438ca542d4bb78aa89a19092dac619589e1472","head_block_time":"2022-12-31T16:42:35.000","head_block_producer":"eosio","virtual_block_cpu_limit":100000000,"virtual_block_net_limit":1048576000,"block_cpu_limit":99900,"block_net_limit":1048576,"server_version_string":"v2.1.0","fork_db_head_block_num":2016452,"fork_db_head_block_id":"001ec4c41773e88922737d74b2438ca542d4bb78aa89a19092dac619589e1472","server_full_version_string":"v2.1.0-26a4d285d0be1052d962149e431eb81500782991","last_irreversible_block_time":"2022-12-31T16:42:34.500"}

>>> private_key, public_key = block.genKeys("ECC")

>>> print("private_key:", private_key)
private_key: 8913420357290673623742686101793348185289342836937776373606618472580075926985



```

![image](https://user-images.githubusercontent.com/60758685/210151486-36d3f31b-c916-4391-adaa-4194f619b40e.png)


### Authors

Hecathomb

Citrix

### Libraries from projects 

* ucrypto library https://github.com/dmazzella/ucrypto

* pythonecdsa https://github.com/starkbank/ecdsa-python


### License 

This is a MIT Free library .

