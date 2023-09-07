## Example of output

#### Run performed with following parameters:
```python  
DEVICE_CHOSEN = {
        "Apple iPhone11": 1,
    }

AVG_NUMBER_OF_DEVICES = 15
AVG_PERMANENCE_TIME = 60*60 # seconds
REAL_MINUTES = 1

PERIOD = 60 # seconds
```
#### The files descriptions are:
 - __out_file_counts.csv__ contains data about the number of devices present at the corresponding time
 - ___out_file_probe_ids.txt__ contains a list of ids corresponding to the devices that emitted the probes (in order of probe generation)
 - __out_file.pcap__ contains the pcap with the generated packets
 - __out_file.txt__ contains the history of the simulation with details about the birth and death of each device