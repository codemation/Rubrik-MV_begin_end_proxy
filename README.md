# Rubrik-MV_begin_end_proxy
Simple HTTP Proxy for triggering Rubrik Managed Volume begin|end snapshots from a HOST supporting TLSv1.2 Use Case:  To be used on non TLSv1.2 clients to start / end snapshots through more up to date hosts 

# Getting Started

Steps Before Use:
1. Create an credentials file, containing 'username:pw'. Method: echo -n 'admin:abcd1234' > ~/special_cdm_auth

2. Update auth.cfg within Rubrik-modify_share package/folder with credential file location. Method echo -n '~/special_cdm_auth' > auth.cfg

Requirements: 
    flask is required to run HTTP Server. Install with pip install flask.


Steps Before Use:
1. Create an credentials file, containing 'username:pw'. Method: echo -n 'admin:abcd1234' > ~/special_cdm_auth

2. Update auth.cfg within Rubrik-MV_begin_end_proxy package/folder with credential file location. Method echo -n '~/special_cdm_auth' > auth.cfg

Usage: 

    Proxy:
        python proxy.py
        defaults to 0.0.0.0:12345 for server
            or 
        python proxy.py <host_address> <port>
    
    Trigger Snapshot:
        python snapshot.py <"begin|end"> <proxy:port> <"cdm_ip"> <mv_id>

       Example:
            -- for MangedVolume:::5ecc5f58-085c-4835-9a00-3a9abd08b330 --
            python snapshot.py "begin" "localhost:12345" "10.35.36.165" "5ecc5f58-085c-4835-9a00-3a9abd08b330"
        Note: snapshot.py is not required to trigger backup, script will generate and print curl command used to trigger each request which can be used anywhere in local environment which has network connectivity to proxy.
