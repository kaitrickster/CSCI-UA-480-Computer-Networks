First start the relay by running:

python3 relay.py 9001

Then start the sender by running:

python3 sender.py 9001 <test_filename>

Then start the receiver by running:

python3 receiver.py 9001

Then start transmissions by pressing enter at the sender terminal.

You should see output like this for a correct solution. Only one test case is
show here. There are 200 strings in the testcases_asg1 file that can be used to
test the solution.

Anirudhs-MacBook-Air:relay anirudh$ python3 sender.py 9001 testcases_asg1
Press enter to start transmissions
sent: Tkaq1frQJqLwCKHzZrJALi1IDpYgkyq43S2Gvirusoufd5Jv5F64QaoG2ODIvZ8W8R9B74Gt04niHAIlQL8clF3X9bTHD1uxg8wTksnqQMgne4phlAxFdv46E12VGMWmJO3sbVj6xDLtPV6mYBfNRlwormStRbq3zHJVIbklCIUtAPuW0rJA6e5JD4nwElEElVQwJmt3

Anirudhs-MacBook-Air:relay anirudh$ python3 relay.py 9001
relayed: Tkaq1frQJqLwCKHzZrJALi1IDpYgkyq43S2Ggrootoufd5Jv5F64QaoG2ODIvZ8W8R9B74Gt04niHAIlQL8clF3X9bTHD1uxg8wTksnqQMgne4phlAxFdv46E12VGMWmJO3sbVj6xDLtPV6mYBfNRlhulkStRbq3zHJVIbklCIUtAPuW0rJA6e5JD4nwElEElVQwJmt3

Anirudhs-MacBook-Air:relay anirudh$ python3 receiver.py 9001
received: Tkaq1frQJqLwCKHzZrJALi1IDpYgkyq43S2Ggrootoufd5Jv5F64QaoG2ODIvZ8W8R9B74Gt04niHAIlQL8clF3X9bTHD1uxg8wTksnqQMgne4phlAxFdv46E12VGMWmJO3sbVj6xDLtPV6mYBfNRlhulkStRbq3zHJVIbklCIUtAPuW0rJA6e5JD4nwElEElVQwJmt3
