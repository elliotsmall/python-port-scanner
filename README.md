# Multithreaded TCP Port Scanner (Python)
## This fast and lightweight TCP port scanner written in Python uses 'socket' and 'ThreadPoolExecutor' for high-speed multithreaded scanning. This tool can be used to scan a target IP across a wide range of ports to display which are open.

### Features
- Multithreaded Port Scanning for massive speed boost vs sequential scanning.
- Adjustable thread pool size.
- Adjustable timeouts.
- Scan any port range.

### Requirements
- Python 3.8 or newer.
- Standard library only (no additional downloads needed)

### How It Works
This scanner uses the Python socket library to attempt a TCP connection to each port within the range.
Instead of scanning ports one-by-one, it uses ThreadPoolExecutor to scan the many ports in parallel.

### Installation
'git clone https://github.com/elliotsmall/python-port-scanner'
'cd python-port-scanner'

Run:
'python3 port_scanner.py'

### Usage
'python3 port_scanner.py'

Input Your Settings:
target = YOUR TARGET IPv4
portStart = STARTING PORT
portEnd = FINAL PORT
maxThreads = # of workers

### How it works:
Unlike sequential scnaners that test each port one-by-one, my scanner:

1. Creates a thread pool with maxThreads workers (adjustable).
2. Creates a port-scan task for each port and stores it in futures.
3. Runs tasks in parallel, with each thread picking up the next task in the queue as soon as it is done executing.
4. Results get collected as soon as each thread finishes.

This multithreaded approach reduces a 1024-port scan from minutes to seconds.

## LEGAL NOTICE
This tool is meant for educational and authorized testing.
This program is not to be used on systems that:
- You do not own.
- You do not have explicit permissions from the owner.
- Are part of restricted networks.

