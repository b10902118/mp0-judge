# mp0-judge v0.0
## Intro
A script that run a test for your ```mp0.c``` with a directory structure of 20 file/dirs whose name length is 10. 
## Usage
1. put "test.c", "testgen.c" under user/ and "gentest.py" under xv6/ \
2. ```python gentest.py``` will generate new ```grade-mp0.py``` and ```test.c``` (included by testgen.c), and then run a docker exec ```make grade```\
3. Since this script uses ```sudo``` to run docker, you may be asked to type your password. 
