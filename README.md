# fabfile for Arch Linux

## task list

```sh
cd fabfile
fab --list
```

## Usage

First, `vagrant up` and check its private_network IP.

```sh
fab -H 127.0.0.1 -u vagrant --port 2222 base.all ruby.base haskell.all
# password: vagrant
```

In case of failure to install Arch base-devel package,

```sh
# run the pacman with -Syu
fab -H 127.0.0.1 -u vagrant --port 2222 base.all_withSysUpgrade ruby.base haskell.all
# password: vagrant
```
