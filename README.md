# Rubrik-MV_begin_end_proxy
Simple HTTP Proxy for triggering Rubrik Managed Volume begin|end snapshots from a HOST supporting TLSv1.2 Use Case:  To be used on non TLSv1.2 clients to start / end snapshots through more up to date hosts 

# Getting Started

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

        Output:

        /Rubrik-MV_begin_end_proxy$ python snapshot.py "begin" "localhost:12345" "10.35.36.165" "5ecc5f58-085c-4835-9a00-3a9abd08b330"
            curl -v -X GET -d '{"cluster": "10.35.36.165", "manageVolumeId": "5ecc5f58-085c-4835-9a00-3a9abd08b330"}' http://localhost:12345/begin_snapshot
            *   Trying 127.0.0.1...
            * TCP_NODELAY set
            * Connected to localhost (127.0.0.1) port 12345 (#0)
            > GET /begin_snapshot HTTP/1.1
            > Host: localhost:12345
            > User-Agent: curl/7.58.0
            > Accept: */*
            > Content-Length: 85
            > Content-Type: application/x-www-form-urlencoded
            > 
            * upload completely sent off: 85 out of 85 bytes
            * HTTP 1.0, assume close after body
            < HTTP/1.0 0 OK
            < Content-Type: application/json
            < Content-Length: 77
            < Server: Werkzeug/0.15.5 Python/2.7.15+
            < Date: Wed, 28 Aug 2019 05:57:52 GMT
            < 
            {
            "message": "{\"snapshotId\":\"e69f2df5-9f02-438d-a098-ccfbbecd223e\"}"
            }
            * Closing connection 0