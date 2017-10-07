# telegram-stalker

Simple python 3 script to log online/offline statuses, as well as counts of messages exchanged between parties since last status change, without you being seen online. I have created it mostly as workaround for annoying telegram-cli message timestamp bug in telegram-cli ([#614](https://github.com/vysheng/tg/issues/614))

Here is it in action:

![screenshot from 2017-09-24 22-09-28](https://user-images.githubusercontent.com/496233/30786436-b07a1a88-a175-11e7-919c-2a6f1268ecbb.png)

## Requirements
[telegram-cli](https://github.com/vysheng/tg)

## Install
Via PIP

``` bash
$ pip3 install -r requirements.txt 
```

## Usage

You need to run telegram-cli first:
``` bash
$ ./bin/telegram-cli -R -W -P 4458 --json
```
Then you can run this script
```bash
$ ./tg-stalker.py
```

## License

The MIT License (MIT). Please see [License File](LICENSE.md) for more information.
