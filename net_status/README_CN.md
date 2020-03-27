# net_status

[English](./README_CN.md) | 中文

通过urls和dns，检查网络是否连接。
然后根据网络状态，执行命令。

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
