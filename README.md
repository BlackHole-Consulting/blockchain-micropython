# Blockchain Micropython Library

A IOT microcontroller blockchain micropython library for EOS, ETH, BITCOIN. Esp32 controllers, St32 and others . For RTOS operating systems . ESP32, ESP8266, ST32 micro controllers .

* Require at least 1 MB SRAM or PSRAM

## Features

- Call to nodes to send request and receive data , get info get balance , get tx, get accounts ....

- Generate ECC keys

- ECDSA signature

- Push transactoin (Pending)


### Requeriments


### Installation

Use install , to install from 0

`install.sh`

or 

Copy file modules to your MicroPython ports

### Compile



```python

cd micropython/ports/esp32

make USER_C_MODULES=/YOURPATH/ports/esp32/boards/GENERIC/ucrypto/micropython.cmake BOARD=CHANGE_YOUR_BOARD  


```


### Flash


```python

cd build-YOURBOARD

esptool.py --chip esp32 -p /dev/ttyACM0 -b 460800 --before=default_reset --after=hard_reset write_flash --flash_mode dio --flash_freq 40m --flash_size 4MB 0x1000 bootloader/bootloader.bin 0x10000 micropython.bin 0x8000 partition_table/partition-table.bin


```

### Usage


* Install mpremote to connect by serial to your device

#### Generate ECC KEYS




```python

>>> import block

>>> block.genkeys()

(100993021156667751991690912130958668616676362468173674328997328032060127345282, 62203629151545849038293504441196077946057605346371203245067596528369427053776, 68608029864182071235580165887815523170041665266793571008314538354569768684678, 'P256')



```


#### Blockchain query ( EOS private block)

```python

mpremote cp block.py requests.py :

mp remote


>>> import block

block.get_info()

HTTP/1.1 200 OK
access-control-allow-origin: *
content-length: 839
content-type: application/json
server: WebSocket++/0.7.0
connection: close

{"server_version":"26a4d285","chain_id":"8b6404a00556c4a1ed0257869dbd41c9ba23349590f39eb90fec0eb9382469dd","head_block_num":2016452,"last_irreversible_block_num":2016451,"last_irreversible_block_id":"001ec4c37801042fdfa0e9cb9273a581b2d166348eb33e3413c5aa7bbef27f64","head_block_id":"001ec4c41773e88922737d74b2438ca542d4bb78aa89a19092dac619589e1472","head_block_time":"2022-12-31T16:42:35.000","head_block_producer":"eosio","virtual_block_cpu_limit":100000000,"virtual_block_net_limit":1048576000,"block_cpu_limit":99900,"block_net_limit":1048576,"server_version_string":"v2.1.0","fork_db_head_block_num":2016452,"fork_db_head_block_id":"001ec4c41773e88922737d74b2438ca542d4bb78aa89a19092dac619589e1472","server_full_version_string":"v2.1.0-26a4d285d0be1052d962149e431eb81500782991","last_irreversible_block_time":"2022-12-31T16:42:34.500"}


```



#### Sign ECDSA 

```python


>>> block.sign("this is a test",100993021156667751991690912130958668616676362468173674328997328032060127345282,)

(107541375824991968821595279068801704738865834089565096653364975660063223096427, 87231512473538947533684998172244028284436404688771902937498298656736416974198)


```

## Push Transaction


```python

cooming soon

>>> block.push(from, to, amount, token, meta, private_key)

executed transaction: f1cdf230e847a8fe582ec615364b7fdbe52f5b462efaad052c107bad90f14d3b  152 bytes  1411 us
#   eosio.token <= eosio.token::transfer        {"from":"eosio","to":"black","quantity":"12.5000 BLACK","memo":"This is the money I owe you"}
#         eosio <= eosio.token::transfer        {"from":"eosio","to":"black","quantity":"12.5000 BLACK","memo":"This is the money I owe you"}
#         black <= eosio.token::transfer        {"from":"eosio","to":"black","quantity":"12.5000 BLACK","memo":"This is the money I owe you"}


```

### Todo List

Please feel free to add issues .


Push transaction BTC

Push Transacion ETH

Network peers 

BTC, ETHEREUM explorer requests

Console interface 


## Contributors

Feel free to pull request your forks !!

### Authors

Hecathomb

Citrix

### Libraries from projects 

* ucrypto library https://github.com/dmazzella/ucrypto


### License 

This is a MIT Free library .

