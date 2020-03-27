# net_status

English | [中文](./README_CN.md)

Check network is connected through open urls and ping dns.
After that, execute command if network status is False or not

## Libraries

- argparse
- urllib

## Usage

```sh
-h, --help            show this help message and exit
-u, --url             url for checking network status
-d, --dns             dns for checking network status
-c, --command         execute command after this action
-f, --flag            execute command under certain circumstances (default: detect network is not connect and then do command, call -f, detect network is connect)
```
