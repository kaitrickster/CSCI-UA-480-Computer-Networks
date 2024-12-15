To run the concatenate assignment, run the server first using:
python3 server.py 9001

Then run the client using:
python3 client.py 9001

A correct solution will have output that looks like this.

10-19-236-179:concatenate tem373$ python3 client.py 9001
sent: GaQGJAB1xY
received: CuE190z1pzGaQGJAB1xY

sent: yzyX9cU3UK
received: iwdkV0stp1yzyX9cU3UK

sent: ss4XK1RDGb
received: NydiJVapTsss4XK1RDGb

sent: wCnZ17LYY8
received: zjfEtbiJB0wCnZ17LYY8

sent: HXslDjSQ2k
received: Ed5rWwPloeHXslDjSQ2k

sent: SOPxnBX4vl
received: ltA4elcX9qSOPxnBX4vl

sent: 3TKBNzIkp2
received: g1Jl79Jvrp3TKBNzIkp2

sent: DeW9ZEMK0k
received: mMoyFW3Wd5DeW9ZEMK0k

sent: SDpBNzQs38
received: ZtFh8e1bRDSDpBNzQs38

sent: j9EWawlCSL
received: OC2741v6qmj9EWawlCSL

10-19-236-179:concatenate tem373$ python3 server.py 9001
received data GaQGJAB1xY; appended CuE190z1pz
received data yzyX9cU3UK; appended iwdkV0stp1
received data ss4XK1RDGb; appended NydiJVapTs
received data wCnZ17LYY8; appended zjfEtbiJB0
received data HXslDjSQ2k; appended Ed5rWwPloe
received data SOPxnBX4vl; appended ltA4elcX9q
received data 3TKBNzIkp2; appended g1Jl79Jvrp
received data DeW9ZEMK0k; appended mMoyFW3Wd5
received data SDpBNzQs38; appended ZtFh8e1bRD
received data j9EWawlCSL; appended OC2741v6qm
