def snap(op, proxy, cdm, id):
    request = 'GET'
    path = ' -d '+ "'" + '{"cluster": "%s", "manageVolumeId": "%s"}'%(cdm, id) + "' " + 'http://%s/%s_snapshot'%(proxy,op)
    curl = 'curl -v -X {request}{path}'.format(
        request = request,
        path = path
    )
    import os
    print(curl)
    os.system(curl)

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 5:
        print(
"""
#################### MV Proxy ##########################################
#
#   Usage:  
#    
#   python3 snapshot.py <"begin|end"> <proxy:port> <"cdm_ip"> <mv_id>
#
#   Example:
#       ## for MangedVolume:::5ecc5f58-085c-4835-9a00-3a9abd08b330 ##
#       python3 snapshot.py "begin" "localhost:12345" "10.35.36.165" "5ecc5f58-085c-4835-9a00-3a9abd08b330"
# """
            )
    else:
        args = sys.argv[1:]
        snap(*args)